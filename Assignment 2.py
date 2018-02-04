
# coding: utf-8

# In[44]:

list1 = [3, 21, 98, 203, 17, 9]
Var = 0
Average = sum(list1)/len(list1)
for i in list1:
    Var_Calc = (i - Average) ** 2 / (len(list1) - 1)
    Var += Var_Calc
print (Var)

