# pandas-insight
The tool uses Ordinary Least Square (OLS) to find similar columns between two dataframes

## Installation
### From source

Download the source code by cloning the repo or by pressing 'Download ZIP' on this page. Install by navigating to the proper directory and running

    python setup.py install
## Usage

The profile result will capture the similar columns

### Jupyter Notebook (formerly IPython)

We recommend generating reports interactively by using the Jupyter notebook. 

Start by loading in your pandas DataFrame, e.g. by using
```python
from pandas_insight import compare_dataframes
import numpy as np
import pandas as pd
        
df1 = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df2 = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        
sim_clmns = compare_dataframes(df1, df2)
print(sim_clmns)

```
