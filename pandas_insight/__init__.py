#import numpy as np
import pandas as pd
import statsmodels.formula.api as sm
#import statsmodels.formula.api as smf
#dat = sm.datasets.get_rdataset("Guerry", "HistData").data
#results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()
#print(results.summary())

def compare_dataframes(df1, df2, rsquared_t = 0.9, f_pvalue_t = 0.1):
	clm_map1 = {}
	clm_map2 = {}


	similar_columns = []
	for column1 in df1.columns:
		clm_freq1 = df1[column1].value_counts()
		df_clm1 = pd.DataFrame(clm_freq1)
		for column2 in df2.columns:
			clm_freq2 = df2[column2].value_counts()
			df_clm2 = pd.DataFrame(clm_freq2)
			merged_df = df_clm2.reset_index().merge(df_clm1.reset_index(), how="inner")
			
			result = sm.ols(data=merged_df, formula='%s ~ %s' % (column2, column1) ).fit()
			#import pdb; pdb.set_trace()
			
			rsquared = result.rsquared
			f_pvalue = result.f_pvalue
			if( (rsquared > rsquared_t) and (f_pvalue < f_pvalue_t) ):
				similar_columns.append( (column1, column2) )
	return similar_columns

if __name__ == "__main__":
	import numpy as np
	#arr = [{"a": 1, "b": 2}, {"a": 11, "b": 6}, {"a": 3, "b": 3}, {"a": 2, "b": 2}]
	#arr2 = [{"aa": 1, "bb": 2}, {"aa": 11, "bb": 25}, {"aa": 2, "bb": 5}]
	df1 = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
	df2 = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
	#df1=pd.DataFrame(arr)
	#df2=pd.DataFrame(arr2)
	sim_clmns = compare_dataframes(df1, df2)
