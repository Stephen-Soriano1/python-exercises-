


user_day = input("Enter a day of the week: ").capitalize()
if user_day == "Monday":
    print("It's Monday!")
else:
    print(f"It's not Monday. It's {user_day}.")




if user_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print(f"{user_day} is a weekday.")
else:
    print(f"{user_day} is a weekend day.")


# In[1]:


hrs_worked = 70
hourly_pay = 45.00


if hrs_worked > 40:
    ot_hrs = hrs_worked - 40 # gets overtime hrs
    ot_pay = ot_hrs * hourly_pay * 1.5 # gets overtime pay
    reg_pay = 40 * hourly_pay
    pay = ot_pay + reg_pay
    
else:
    pay = hrs_worked * reg_pay

print(pay)


# Create an integer variable i with a value of 5. Create a while loop that runs so long as i is less than or equal to 15. Each loop iteration, output the current value of i, then increment i by one.

# In[ ]:


i = 5 
while i <= 15:
    print(i)
    i +=1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
# 

# In[ ]:


i = 0
while i <= 100:
    print(i)
    i +=2


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

# In[1]:


i = 2 
while i < 1000000:
    print(i)
    i = i*i
    


# Write a while loop that uses print to create the output shown below.
# 
# 
# 

# In[5]:


i = 100
while i < 100:
    print(i)
    i -=5


# Write some code using a for loop that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# In[1]:


num = 7

for i in range(1, 11):
    print(num, 'x', i, '=', num*i)


# In[57]:


for i in range(1,10):
    for s in range(i):
        print(i,end='')
    print()
 

    


# In[12]:


for n in range (50):
    if n % 2 == 0:
        print(f'Here is an odd number: {n}')
    if n == 27:
        print(f'skip a number: {27}') 
        continue

        


# In[ ]:





# fizzbuzz

# In[2]:


for num in range(1,101):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)


# In[92]:


n=int(input("Enter the number to print the tables for:"))
for i in range(1,11):
    print(n,"^",i+1,"=",n**i)
input = input("Do you want to continue (yes/no)? ").lower()
if user_input != "yes":
        break


# In[ ]:


cont = 'yes'

while cont == 'yes':
    numb = int(input('Enter an integer: '))

    print(f'number | squared | cubed')
    print(f'-------|---------|-----')

    for i in range(1,numb+1):
           
        print(f'{i:<7}|{i**2}        |{i**3} ')
        
    cont = input('Would you like to continue (yes/no)?')


# Convert given number grades into letter grades.
# 
# Prompt the user for a numerical grade from 0 to 100
# Display the corresponding letter grade
# Prompt the user to continue
# Assume that the user will enter valid integers for the grades
# The application should only continue if the user agrees to
# Grade Ranges:
# 
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# In[ ]:


def numerical_to_letter_grade(grade):
    if 88 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 87:
        return "B"
    elif 67 <= grade <= 79:
        return "C"
    elif 60 <= grade <= 66:
        return "D"
    elif 0 <= grade <= 59:
        return "F"

while True:
    try:
        numerical_grade = int(input("Enter a numerical grade (0-100): "))
        if 0 <= numerical_grade <= 100:
            letter_grade = numerical_to_letter_grade(numerical_grade)
            print(f"The corresponding letter grade is: {letter_grade}")
        else:
            print("Please enter a valid numerical grade between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid numerical grade.")
    
    user_input = input("Do you want to continue (yes/no)? ").lower()
    if user_input != "yes":
        break


# In[ ]:





# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# 
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[ ]:


books = [
    #{key:value, key:value, key:value}
    {'title':'parable of the sower', 'author':'octavia butler', 'genre':'sci fi'},
    {'title':'think and grow rich', 'author':'napoleon hill', 'genre':'self help'},
    {'title':'1984','author':'george orwell','genre':'fiction'},
    {'title':'Don Quixote', 'author':'Miguel de Cervantes', 'genre':'comedy'},
    {'title':'Gone with the Wind', 'author':'Margaret Mitchell', 'genre':'romance'},
    {'title': 'Farenheit 451', 'author':'Ray Bradbury', 'genre': 'sci fi'},
    {'title': 'The Giver', 'author': 'Lois Lowry', 'genre': 'sci fi'}
    


# In[ ]:


for book in books:
    print(book)


# In[ ]:


books['title']


# In[ ]:


books[7]


# In[ ]:


books[6]


# In[ ]:


genre_input = input('Enter a genre: \n\n')

for book in books:
    # print(book) #print out each book aka each dictionary separately
    # print(book['genre']) #have to call the key to get back its value
    if genre_input.lower() == book['genre']:
        print(book['title'])
    else:
        pass
        
        
       


# In[ ]:


books


# In[ ]:




