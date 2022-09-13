# Todo just use conda environment instead of Virtual, no need reinstall packages

import pandas as pd
import seaborn as sns
import datetime as dt
import pandas_datareader.data as reader
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 1. Set up target assets, period, and desired data columns
end = dt.datetime.now()
start = dt.datetime(end.year - 5, end.month, end.day)
tickers = ['AAPL', '^GSPC']
# 2. Convert daily return to monthly return
df = reader.get_data_yahoo(tickers, start, end)['Adj Close']
mly_ret = df.resample('M').mean().pct_change().dropna()
# 3. Collect risk-free rate
rf = reader.DataReader('F-F_Research_Data_Factors','famafrench', start,end)[0].RF
rf = rf[1:]
sup_index = pd.PeriodIndex(['2022-07','2022-08'],freq='M')
sup_data = pd.Series([0.07,0.08], index=sup_index)
rf = rf.append(sup_data)
# 4. Subtract rf
mly_ret['AAPL-rf'], mly_ret['^GSPC-rf'] = mly_ret['AAPL']-rf.values, mly_ret['^GSPC']-rf.values
# 5. Build the regression model and fit
y= mly_ret['AAPL-rf']
x= mly_ret['^GSPC-rf']
x_sm = sm.add_constant(x)
model=sm.OLS(y,x_sm)
result = model.fit()
# 6. Visualize the results
# in Pycharm, need to add plt.show() to show the sns plot object
print(result.summary())
sns.regplot(data=mly_ret, x='^GSPC-rf', y='AAPL-rf').set(title = 'AAPL Beta')
plt.show()
