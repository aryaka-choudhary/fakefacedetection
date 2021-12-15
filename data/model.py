#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[2]:


import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN
from PIL import Image



# In[ ]:





# In[ ]:


path = "train/real/00001.jpg"


# In[20]:


imgg = cv2.imread(path)


# In[21]:


imgg = cv2.resize(imgg,(224,224))


# In[22]:


plt.imshow(cv2.cvtColor(imgg, cv2.COLOR_BGR2RGB))


# In[ ]:




