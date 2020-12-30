import pandas
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from scipy import stats

data = pandas.read_csv('iphone_price.csv')
model = LinearRegression()
model.fit(data[['version']],data[['price']])

user_input_version = int(input("Enter the version of Iphone:"))
predict_result = model.predict([[user_input_version]])
final_result = str(predict_result)[2:-2] 

print('The expecting price of Iphone ',user_input_version ,'is',final_result,'$' )

plt.scatter(data['version'], data['price'], color='red')
plt.plot(data['version'], data['price'], color='blue') 
plt.title("Current Iphone Price vs Version") 
plt.xlabel("version of Iphone") 
plt.ylabel("Price of Iphone")
plt.show()



