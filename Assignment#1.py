#Assignment#1 - Overall Appreciation Application
#grade >= 85 Excellent
#85 > grade  >= 75 very good
#75 > grade >= 65 good
#65 > grade >= 50 pass
#grade < 50 fail
#-----------------------------CODE----------------------------------------#
# grade = int(input('Enter your grade: \n'))

# if grade >= 85 and grade <= 100:
#     print('Excellent')
# elif grade < 85 and grade >= 75:
#     print('Very Good')
# elif grade < 75 and grade >= 65:
#     print('Good')
# elif grade < 65 and grade >= 50:
#     print('Pass')
# elif grade < 50 and grade >= 0:
#     print('Fail')
# else:
#     print('Incorrect')

#-------------------------------------------------------------------------#

#Assignment#2 - FizzBuzz Game
#if num can be divided by 3 then print fizz
#if num can be divided by 5 then print buzz
#if num can be divided by 3 and 5 then print fizzBuzz
#else print number
#-----------------------------CODE----------------------------------------#
# num = int(input('Please Enter Your Number: '))

# if num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')
# elif num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
# else:
#     print(num)

#-------------------------------------------------------------------------#

#Assignment#3 - Check num even or odd
#-----------------------------CODE----------------------------------------#
# num = int(input('Please Enter Your Number: '))

# if num % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

#-------------------------------------------------------------------------#

#Assignment#4 - Check string is palindrome or not
#madam == madam - nafs el kalma law et3kst ttkb nafs el 7aga
#-----------------------------CODE----------------------------------------#
# Word = input('Enter a string: \n')

#method returns a string where all the characters are lower case. will find more matches when comparing two strings
# Word = Word.casefold()
#method returns an iterator that accesses the given sequence in the reverse order.
# revWord = reversed(Word)
#Revrsed method return a reversed list of items present in a sequence object
# if list(Word) == list(revWord):
#     print(Word, ' is Palindrome.')
# else:
#     print(Word, 'is not Palindrome.')

#-------------------------------------------------------------------------#

#Assignment#5 - calc rec area and perimeter
#-----------------------------CODE----------------------------------------#
# Length = float(input('Enter Rectangle Length: \n'))
# Width = float(input('Enter Rectangle Width: \n'))

# Area = Length * Width
# Prei = 2 * (Length + Width)
# print('Area = ', Area)
# print('Perimeter', Prei)