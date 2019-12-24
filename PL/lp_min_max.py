#!/usr/bin/env python
# coding: utf-8

# # Linear Programming using PuLP

# ##  Minimization Problems

# ### Exercice 1

# <img src="img/Screenshot_1.png"/>

# #### Solution

# In[1]:


from pulp import *
# Create a LP minimization problem
prob = LpProblem("Giapetto", LpMinimize)  

# Create variables
x0 = LpVariable("x0", lowBound=0, cat='Integer') 
x3 = LpVariable("x3", lowBound=0, cat='Integer')
x6 = LpVariable("x6", lowBound=0, cat='Integer') 
x9 = LpVariable("x9", lowBound=0, cat='Integer')
x12 = LpVariable("x12", lowBound=0, cat='Integer') 
x15 = LpVariable("x15", lowBound=0, cat='Integer')
x18 = LpVariable("x18", lowBound=0, cat='Integer') 
x21 = LpVariable("x21", lowBound=0, cat='Integer')

# Objective function
prob += 36*x0 + 36*x3 + 36*x6 + 25*x9 + 25*x12 + 25*x15 + 30*x18 + 30*x21  

# Sub constraints
prob += x0 + x18 + x21 >= 6 
prob += x0 + x3 + x21 >= 4 
prob += x0 + x3 + x6 >= 12
prob += x3 + x6 + x9 >= 20 
prob += x6 + x9 + x12 >= 20
prob += x9 + x12 + x15 >= 24 
prob += x12 + x15 + x18 >= 14
prob += x15 + x18 + x21 >= 14

# Display the LP problem
print('LP problem:')
print(prob)

# Solve with the default solver
status = prob.solve()
# Print the solution status
print('solution status:')
print(LpStatus[status])

# Print the solution
print('\nsolution:')
print('x0 =',value(x0))
print('x3 =',value(x3))
print('x6 =',value(x6))
print('x9 =',value(x9))
print('x12 =',value(x12))
print('x15 =',value(x15))
print('x18 =',value(x18))
print('x21 =',value(x21))
print('Optimal Z = ', value(prob.objective))


# ### Exercice 2

# <img src="img/Screenshot_2.png"/>

# #### Solution

# In[2]:


from pulp import *
# Create a LP minimization problem
prob = LpProblem("Giapetto", LpMinimize)  

# Create variables
x = LpVariable("x", lowBound=0, cat='Integer') 
y = LpVariable("y", lowBound=0, cat='Integer')

# Objective function
prob += 2000*x + 3600*y

# Sub constraints
prob += x + 3*y >= 30
prob += 3*x + 2*y >= 40 
prob += 4*x + 6*y >= 90
prob += 2000*x + 3600*y <= 50000

# Display the LP problem
print('LP problem:')
print(prob)

# Solve with the default solver
status = prob.solve()
# Print the solution status
print('solution status:')
print(LpStatus[status])

# Print the solution
print('\nsolution:')
print('x =',value(x))
print('y =',value(y))
print('Optimal Z = ', value(prob.objective))


# ### Exercice 3

# <img src="img/Screenshot_3.png"/>

# #### Solution

# In[3]:


from pulp import *
# Create a LP minimization problem
prob = LpProblem("Giapetto", LpMinimize)  

# Create variables
xA = LpVariable("xA", cat='Binary')
xB = LpVariable("xB", cat='Binary') 
xC = LpVariable("xC", cat='Binary') 
xD = LpVariable("xD", cat='Binary') 
xE = LpVariable("xE", cat='Binary') 
xF = LpVariable("xF", cat='Binary') 

# Objective function
prob += xA + xB + xC + xD + xE + xE

# Sub constraints
prob += xA + xE == 1
prob += xA + xC + xD + xF >= 1
prob += xA + xC + xB + xE >= 1
prob += xA + xC + xD + xF <= 2
prob += -xA + xB - 3*xD + xF >= 0
prob += -2.5*xA - 0.5*xB - 0.5*xC + 1.5*xD + 1.5*xE - 1.5*xF >= 0
prob += xA + xB <= 1
prob += xA + xC <= 1

# Display the LP problem
print('LP problem:')
print(prob)

# Solve with the default solver
status = prob.solve()
# Print the solution status
print('solution status:')
print(LpStatus[status])

# Print the solution
print('\nsolution:')
print('xA =',value(xA))
print('xB =',value(xB))
print('xC =',value(xC))
print('xD =',value(xD))
print('xE =',value(xE))
print('xF =',value(xF))

print('Optimal Z = ', value(prob.objective))


# ##  Maximization Problems

# ### Exercice 1

# <img src="img/Screenshot_4.png"/>

# #### Solution

# In[4]:


from pulp import *
# Create a LP maximization problem
prob = LpProblem("Giapetto", LpMaximize)  

# Create variables
x1 = LpVariable("x1", cat='Integer')
x2 = LpVariable("x2", cat='Integer') 

# Objective function
prob += 0.5*x1 + 0.4*x2 

# Sub constraints
prob += 2*x1 + 1.5*x2 <= 600
prob += x1 + x2 <= 600
prob += x1 <= 400
prob += x2 <= 350
prob += x1 >= 50

# Display the LP problem
print('LP problem:')
print(prob)

# Solve with the default solver
status = prob.solve()
# Print the solution status
print('solution status:')
print(LpStatus[status])

# Print the solution
print('\nsolution:')
print('x1 =',value(x1))
print('x2 =',value(x2))

print('Optimal Z = ', value(prob.objective))


# ### Exercice 2

# <img src="img/Screenshot_5.png"/>

# #### Solution

# In[5]:


from pulp import *
# Create a LP maximization problem
prob = LpProblem("Giapetto", LpMaximize)  

# Create variables
x1 = LpVariable("x1", cat='Integer')
x2 = LpVariable("x2", cat='Integer')
x3 = LpVariable("x3", cat='Integer') 

# Objective function
prob += 180*x1 + 60*x2 + 40*x3 

# Sub constraints
prob += 8*x1 + 6*x2 + x3 <= 240
prob += 4*x1 + 2*x2 + 1.5*x3 <= 100
prob += 2*x1 + 1.5*x2 + 0.5*x3 <= 40
prob += x2 >= 5
prob += - 4*x2 + x3 >= 0

# Display the LP problem
print('LP problem:')
print(prob)

# Solve with the default solver
status = prob.solve()
# Print the solution status
print('solution status:')
print(LpStatus[status])

# Print the solution
print('\nsolution:')
print('x1 =',value(x1))
print('x2 =',value(x2))
print('x3 =',value(x3))

print('Optimal Z = ', value(prob.objective))

