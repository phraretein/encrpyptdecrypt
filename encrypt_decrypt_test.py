#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()


# In[7]:


file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()
print(key)


# In[8]:


file = open('key.key', 'rb')
key = file.read() # The key will be type bytes
file.close()
print(key)


# In[15]:


message = "my deep dark secret".encode()

f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)


# In[17]:


decrypted = f.decrypt(encrypted)
original = decrypted.decode()
print(decrypted)
print(original)


# In[ ]:




