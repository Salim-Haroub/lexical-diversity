#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk
import matplotlib.pyplot as plt


# In[3]:


from nltk.corpus import brown


# In[4]:


print('Genre', 'Lexica Diversity')
for cat in brown.categories():
    words = brown.words(categories = cat)
    print(cat, '{:.3g}'.format(len(set(words))/len(words)))


# In[5]:


from nltk.corpus import names
from nltk import ConditionalFreqDist


# In[6]:


cfdt = ConditionalFreqDist((fileid, name[0]) for fileid in names.fileids() for name in names.words(fileid))


# In[7]:


cfdt.tabulate(conditions = names.fileids())


# In[8]:


cfdt.plot()


# In[9]:


from nltk.corpus import stopwords
from nltk import FreqDist
def most_freq_words(text):
    stopword = stopwords.words('english')
    cleanwords = [w for w in text if w.lower() not in  stopword]
    frqDist = FreqDist(cleanwords)
    return frqDist


# In[10]:


emma = brown.words(categories = 'news')
most_freq_words(emma)


# In[ ]:




