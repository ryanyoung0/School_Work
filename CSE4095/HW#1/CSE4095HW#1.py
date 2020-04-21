#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as mpl
def calc_g(theta, X):
    theta = theta.T
    z = theta.dot(X)
    return (1 / (1 + np.exp(-z)))

def grad_theta(theta, X, Y):
    output = np.array([0, 0, 0])
    for i in range(len(X)):
        grad_theta = np.multiply(X[i], Y[i] - calc_g(theta, X[i]))
        output = np.add(output, grad_theta)
    return output

def grad_asc(theta, alpha, gradient):
    return theta + np.multiply(alpha, gradient)

def calc_prob(X, Y, theta):
    cg = calc_g(theta, X) ** Y
    cg2 = (1 - calc_g(theta, X)) ** (1 - Y)
    return cg * cg2

def main(alpha, tol, plot):
    X = np.loadtxt("C:/Users/rYans/Documents/CSE 4095/HW_1/q1x.dat")
    Y = np.loadtxt("C:/Users/rYans/Documents/CSE 4095/HW_1/q1Y.dat")
    Vec_Ones = np.ones((99, 1)) # constant feature 1 matrix
    X = np.concatenate((Vec_Ones, X), axis = 1) # Adding the constant feature 1 to the feature set
    print("Finding Gradient Ascent with an alpha of: ", alpha," and tolerance of: ", tol)
    theta = np.array([0, 0, 0])
    step_num = 0
    while True:
        d1_theta = grad_theta(theta, X, Y)
        if np.linalg.norm(d1_theta, 2) < tol:
            break
        else:
            theta = grad_asc(theta, alpha, d1_theta)
            step_num += 1
    if plot == True:
        o_plotted = False
        one_plotted = False
        for i in range(len(X)):
            if Y[i] == 0:
                if not o_plotted:
                    mpl.plot(X[i][1], X[i][2], 'ks', label = 'Y = 0')
                    o_plotted = True
                else:
                    mpl.plot(X[i][1], X[i][2], 'ks')
            else:
                if not one_plotted:
                    mpl.plot(X[i][1], X[i][2], 'ro', label ='Y = 1')
                    one_plotted = True
                else:
                    mpl.plot(X[i][1], X[i][2], 'ro')
        x = np.linspace(-3,11,100)
        y = (-1*(theta[0]+theta[1]*x)) / theta[2]
        mpl.plot(x, y, '-b', label='Decision Boundary')
        mpl.legend(loc ='upper right')
        mpl.axis([0, 10, -10, 10])
        mpl.grid()
        mpl.show()
    #return theta NEED TO TOGGLE FOR LATER QUESTIONS
    print("Number of steps run: ", step_num, "| With a theta of: ", theta)
#Answering Question 3c    
print("Exercise 2, Question 3c i:")
main(0.01, 10**-6, False)
print("Exercise 2, Question 3c ii:")
#main(0.01, 10**-6, False)
print("It never finished, might be too big of a step!")
print("Exercise 2, Question 3c iii:")
main(0.001, 10**-6, False)


# In[13]:


print("Exercise 2, Question 3d:")
main(0.01, 10**-6, True)
main(0.001, 10**-6, True)


# In[12]:


print("Exercise 2, Question 3e:")
theta = main(0.01, 10 ** -6, False)
proby0 = calc_prob(np.array([1, 2, 1]), 0, theta)
proby1 = calc_prob(np.array([1, 2, 1]), 1, theta)
print("Probability 0:", proby0, "Proability 1:", proby1)


# In[ ]:




