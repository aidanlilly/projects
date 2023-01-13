#Aidan Lilly
#January 20, 2022
#Gradient descent linear regression model

import matplotlib.pyplot as plt
import numpy as np



def mean_normalization(array): #Condense all numbers to values closer
  mean = np.mean(array)#get mean of array
  std = np.std(array)#get standard deviation

  return (array-mean)/std#normalized range


def gradient_descent(x,y):
  global theta0_curr
  global theta1_curr
  theta1_curr = theta0_curr = 0
  iterations = 1000                                                                       
  m = len(x)
  learning_rate = 0.08

  for i in range(iterations):
    y_predicted = theta1_curr * x + theta0_curr#Y=mx+b form of function
    cost = (1/m) * sum([val**2 for val in (y-y_predicted)])#Square error function
    theta1d = -(2/m)*sum(x*(y-y_predicted))#Derived square errror function
    theta0d = -(2/m)*sum(y-y_predicted)#derived square error function
    theta1_curr = theta1_curr - learning_rate * theta1d#update theta values with reference to alpha value
    theta0_curr = theta0_curr - learning_rate * theta0d
    print ("theta1 {}, theta0 {}, cost {} iteration {}".format(theta1_curr,theta0_curr,cost, i))


 


def predict_y(x):
  y = theta1 * x + theta0#Use theta values to determine value
  plt.plot(x, y, 'go', markersize=10)
  print(y)


x = np.array([1,2,3,4,5])  #The "known" values being given to program
y = np.random.randint(1,26,5)
                                                                                                                                                                                            

y = mean_normalization(y)

gradient_descent(x,y)


theta0 = theta0_curr
theta1 = theta1_curr

x1 = np.linspace(1,5,100)
y1 = theta0 + theta1 * x1

predict_y(4.3) #Predicting where 4.3 will fit amongst the known values from arrays x and y


plt.plot(x, y, 'rx')#Show data
plt.plot(x1,y1, '-b')
plt.show()
  </code>
</pre>

<style type="text/css">
pre code {
  background-color: #eee;
  border: 1px solid #999;
  display: block;
  padding: 20px;
}