#import numpy as np
import pandas as pd
import statsmodels.api as sm
#import statsmodels.formula.api as smf
#dat = sm.datasets.get_rdataset("Guerry", "HistData").data
#results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()
#print(results.summary())

def compare_dataframes(df1, df2, rsquared_t = 0.9, f_pvalue_t = 0.1):
	clm_map1 = {}
	clm_map2 = {}


	similar_columns = []
	for column1 in df1.columns:
		clm_freq1 = df1[column1].value_count()
		df_clm1 = pd.DataFrame(clm_freq1)
		for column2 in df2.columns:
			clm_freq2 = df2[column2].value_count()
			df_clm2 = pd.DataFrame(clm_freq2)
			merged_df = df_clm2.reset_index().merge(df_clm1.reset_index(), how="inner")
			result = sm.OLS(merged_df, '%s ~ %s' % (column2, column1) )
			rsquared = result.rsquared
			f_pvalue = result.f_pvalue
			if( (rsquared > rsquared_t) and (f_pvalue < f_pvalue_t) ):
				similar_columns.append( (column1, column2) )
	return similar_columns




