#!/usr/bin/env python
# coding: utf-8

# # first method  
# 
# ### In this way, we first add the libraries we use, then we need the house data to find the best line
#   

# In[55]:


import pandas


# In[56]:


import numpy as np


# In[ ]:





# ### We import house data using the Panda Library
# 

# In[58]:


data = pandas.read_csv(r"C:\users\yashar-zb\desktop\kc_house_data.csv")


# #### In this first method, simple linner regression, we calculate a house data using house metrics and two values of w0 and w1 that are coefficients of the regression function of the house price.
# 

# In[59]:


def model(sqft_living , w0 , w1):
   method = w0 + w1 * sqft_living
   return method


# #### The RSS function calculates and finds the best or best possible line. In this method, we get all the states and then we find the minimum value in the next step and The lower the RSS content, the better.
# 

# In[60]:


def RSS(Y , Yhat):
    a = pow(Y-Yhat,2)
    rss = np.sum(a)
    return np.log(rss)


# In[61]:


result = []


# #### In this part of the code we obtain two values of w0, w1 randomly in the range of 1 to 100, by replacing two Yhat values that are the house price and the total price of the data house and the output value per output. We will save the result presentation
# 

# In[64]:


for w0 in range(1 , 100):
    for w1 in range(1 , 100):
        Yhat = model(data['sqft_living'] , w0 , w1)
        rss = RSS(data['price'] , Yhat)
        result.append(rss)


# #### At least we get the result value
# 

# In[65]:


min = np.min(result)
min


# # The second method of derivation 

# #### In the second method, which is the best, most important and easiest way to find the best possible line, we can derive the function and set the derivative to zero to obtain the variable value.

# #### To make things easier, we can use the sympy libraries used to perform math operations.

# In[91]:


from sympy import Symbol, Derivative,Eq
from sympy.solvers import solve


# #### We define two famous mathematical symbols x, y

# In[92]:


x= Symbol('x')
y= Symbol('y')


# #### The feed we want is the RSS function.
# #### Define the RSS function that is the sum of the squares
# 

# In[93]:


function= pow(x - y,2)


# #### At this point we write a method that performs the derivation of the desired function.
# #### But since our function has two unknown values we have to derive once for x and once for y.
# #### Then, after we get the derivatives, we have to give X once and get Y. And once we have the value of Y, we get X.

# In[94]:


def RSSDerivative(input1,input2):
    function= pow(x - y,2)
    deriv= Derivative(function, x)
    derivy= Derivative(function, y)
    deriv.doit()
    derivy.doit()
    dd = deriv.doit().subs({x:input1})
    dd2 = derivy.doit().subs({y:input2})
    sol1 = solve([dd2,dd], dict=True)
    xs =sol1[0]
    for key, value in xs.items():
        
        return value
#     return print(sol)


# #### In this section, just like the first step, we give two values of rss, yhat to the RSSDerivative function in the range of 100 to 1000 and give us the calculated value of X and Y

# In[103]:


result2 = []
for w0 in range(1 , 100):
    for w1 in range(1 , 100):
        Yhat = model(data['sqft_living'] , w0 , w1)
        rss = RSS(data['price'] , Yhat)
        c = RSSDerivative(Yhat,rss)
        
        result2.append(c)
#         print(np.min(result2))


# In[104]:


min = np.min(result2)
min


# In[ ]:




