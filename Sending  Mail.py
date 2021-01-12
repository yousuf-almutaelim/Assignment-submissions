#!/usr/bin/env python
# coding: utf-8

# In[3]:



import smtplib 


s = smtplib.SMTP('smtp.gmail.com', 587) 

 
s.starttls() 

s.login("david.prabhu86@gmail.com", "Idiot@85") 

message = "hello how you doing"


s.sendmail("david.prabhu86@gmail.com", "leadplacements@gmail.com", message) 


s.quit() 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




