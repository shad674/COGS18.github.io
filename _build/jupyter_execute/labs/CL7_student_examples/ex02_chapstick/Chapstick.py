#!/usr/bin/env python
# coding: utf-8

# ### Module Import

# In[4]:


import YOLO as chap

a = [chap.Chapstick('a brand'), chap.Chapstick('b brand'), 
     chap.Chapstick('c brand'), chap.Chapstick('d brand')]

chap.rate_chapsticks(a)

b = chap.Chapstick('good brand')
chap.use_alot_of_chapstick(b)

