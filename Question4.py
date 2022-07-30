#4.1
# from hmac import digest
# import string 
# import random #allows you to select chars, and numbers randomly

# #define list of letters, digits 
# Upper = list(string.ascii_uppercase) 
# Lower = list(string.ascii_lowercase) 
# Digits = list(string.digits) 

# print('###################################')
# print('#             WELCOME             #')
# print('###################################')


# def generatePassword(): #Function to generate password
#     PasswordLength = input('Please enter your password length: ') #Asking User to enter his pw length
#     #Try, Catch if the pw length is int and > 14
#     while True:
#         try:
#             PasswordLength = int(PasswordLength) #If password length is int value
#             if PasswordLength < 14: #Check condition if the pw lenth is less than 14
#                 print('Your password must be at least 8 characters')
#                 PasswordLength = int(input('Please re-enter your password length again: '))
#             break #Stop Loop if condition TRUE
#         except:
#             print('Please Enter Numeric Value') #error handling
#             PasswordLength = int(input('Please enter your password length: '))

#      #define list of password
#     password = [] 
#     random.shuffle(Upper) 
#     random.shuffle(Lower)  
#     random.shuffle(Digits) 

#     #append letterrs into password
#     for i in range(round(PasswordLength * 0.4)):
#         password.append(Upper[i]) #'i' is the number of value inside the index 
#     #append digits into password
#     for i in range(round(PasswordLength * 0.3)): 
#         password.append(Lower[i]) #'i' is the number of value inside the index 
#     #append special chars into password
#     for i in range(round(PasswordLength * 0.3)):
#         password.append(Digits[i]) #'i' is the number of value inside the index 
       
#     password = "".join(password[0:]) #to print password as a string from 0 index to the last index
#     print(f"Your generated password is: \n {password}")

# generatePassword()

