import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np

twitter_data = pd.read_csv('results_olympics.csv')

print(twitter_data.corr())

twitter_data_subjectivity =twitter_data[twitter_data['subjectivity'] > 0.4]
print(twitter_data_subjectivity.corr())

plt.scatter(twitter_data.polarity, twitter_data.subjectivity)

y = twitter_data.subjectivity
x = twitter_data.polarity
x = sm.add_constant(x)                  # linear modelng 
 
lr_model = sm.OLS(y,x).fit()            # linear regression model ordianry linear 

print(lr_model.summary())

# artifically generated data
x_prime = np.linspace(x.polarity.min(), x.polarity.max(), 10)
x_prime = sm.add_constant(x_prime)

y_hat = lr_model.predict(x_prime)           # prediction
plt.scatter(x.polarity, y)
plt.xlabel("polarity")
plt.ylabel("subjectivity")
plt.plot(x_prime[:,-1],y_hat)