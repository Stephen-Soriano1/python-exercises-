#!/usr/bin/env python
# coding: utf-8

# question 1.

# In[1]:


type(99.9)


# In[9]:


type('False') #having '' make it a string even with it being true or false


# In[13]:


type(False)


# In[8]:


type('0')


# In[11]:


type(0)


# In[10]:


type('True')


# In[12]:


type(True)


# In[ ]:


type


# In[16]:


type([{}])


# In[17]:


type({'a': []}
)


# question 2. What data type would best represent the following?

# #A term or phrase typed into a search box - 
# >str

# #Whether or not a user is logged in - booleans

# #A discount amount to apply to a user's shopping cart - float

# #Whether or not a coupon code is valid - bloleans

# #An email address typed into a registration form - str

# #The price of a product - float

# #The email addresses collected from a registration form - list

# #Information about applicants to Codeup's data science program -dict 

# In[ ]:





# 3.For each of the following code blocks:
# 
# Read the expression and predict the evaluated results
# 
# Execute the expression in a Python REPL.

# In[23]:


'1' + 2 # will error out because it can not concatenate str only int 


# In[38]:


6 % 4 # Divides left hand operand by right hand operand and returns remainder


# In[26]:


type(6 % 4) #when put type first it going to tell you the data type


# In[27]:


type(type(6 % 4)) # will come as type the word 


# In[28]:


'3 + 4 is ' 3 + 4 # has invalid syntax for t
# his code to work would need to get rid of quotation


# In[30]:


0 < 0  # it comes out as False


# In[32]:


True == 'True' # comes back as False as well 


# In[34]:


5 >= -5 # comes back as True


# In[36]:


True or "42" # comes back as true always return what not false


# In[37]:


6 % 5 #Divides left hand operand by right hand operand and returns remainder


# In[40]:


5 < 4 and 1 == 1 # comes back as False, once side is false will come back as false 


# In[41]:


'codeup' == 'codeup' and 'codeup' == 'Codeup' # comes back as False cap matter


# In[1]:


4 >= 0 and 1 !== '1' # if the double equal sign was not there then it would run as True but since they are there the code give an error


# In[45]:


6 % 3 == 0 # comes out 2 


# In[46]:


5 % 2 != 0 # comes back as true cause it say not equal to 


# In[47]:


[1] + 2 # comes back as False has not int unless both are in a []list 


# In[48]:


[1] + [2] # comes back as inclose [x] 


# In[50]:


[1] * 2 # come back as inclose [1, 1]


# In[53]:


[] + [] == [] # comes back as True


# In[58]:


{} + {} # unsupported operand type(s) for +: 'dict' and 'dict'


# In[ ]:





# Describe the following scenarios. You will need to create and assign variables and use operators.
# 
# 4. You have rented some movies for your kids:
# The Little Mermaid for 3 days
# Brother Bear for 5 days
# Hercules for 1 day
# 

# In[101]:


the_little_mermaid = 3
brother_bear = 5
hercules= 1

(the_little_mermaid+brother_bear+hercules) * 3


#(3 * 3) + (5 * 3) + (1* 3) # 27


# 5. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.
# 
# They pay you the following hourly rates:
# 
# Google: 400 dollars
# Amazon: 380 dollars
# Facebook: 350 dollars
# This week you worked: 10 hours for Facebook, 6 hours for Google, and 4 hours for Amazon.
# 
# 

# In[102]:


google= 400
amazon= 380
facebook= 350

google_pay=6
amazon_pay=4
facebook_pay=10

(google* google_pay) + (amazon * amazon_pay)+ (facebook * facebook_pay)



# 6. A student can be enrolled in a class only if the class is not full and the class schedule does not conflict with her current schedule.
# 

# In[103]:


is_full = False
schedule_conflict = True


# In[ ]:


can_enroll = not schedule_conflict and not is_full
can_enroll


# In[67]:


class_is_not_full = True
schedule_does_not_conflict = True

if class_is_not_full and schedule_does_not_conflict:
    print("the student can be enrolled in the class")
else :
    print('the students cannot ne enrolled in the class')


# A product offer can be applied only if a customer buys 
# more than 2 items, and the offer has not expired. Premium members 
# do not need to buy a specific amount of products.

# In[11]:


buy_more_than_2 = False

offer_expired = False

is_premium = True



# In[12]:


product_offer = (buy_more_than_2 or is_premium) and not offer_expired
product_offer


# In[128]:


has_more_than_2_item = True
offer_has_not_expired = True
is_premium = False 

if (has_more_than_2_item or is_premium) and offer_has_not_expired:
    print('coupon apply')
else :
    print('coupon not apply')
    


# In[131]:


username = 'codeup'
password = 'notastrongpassword'


# In[99]:


is_valid_password_length =len(password) >= 5 

is_valid_username_length =len(username) <= 20

password_not_same_as_username = password != username

if is_valid_password_length and is_valid_username_length and password_not_same_as_username:
    print('all good')
else:
    print('not good')




# In[132]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




