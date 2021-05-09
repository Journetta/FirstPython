# Copyright Maisy Jones, Following The Tutorial By Mosh: https://www.youtube.com/channel/UCWv7vMbMWH4-V0ZXdmDpPBA
# Chapter 1
print('© Maisy Jones - 2021 ')
# this is a dog aparently?
print('o----')
print(' ||||')
# This takes * and copies it 10 times (e.g **********)
print('*' * 10)

# Chapter 2
# Defining Variables
price = 10
rating = 4.9
name = 'Maisy'
# underscores for multiplewords in variables
# defining variables should always be lowercase, but Python variables need to have capital F (e.g False not false)
is_published = False
print(price * rating)

# Hospital Patient Example
# Check in a patient named john smith, 20 years old and is a new patient
patient = 'John Smith'
age = '20'
is_new_patient = True

namer = input('What is your name? ')
colour = input('What is your favourite colour? ')
# Calculating Age
birth_year = input('Birth Year: ')
weight = input('What is your weight? In Pounds? ')
# Always Convert a string into a interger (int)
yearage = int = (2021) - int(birth_year)
weightkg: float = float(weight) / float(2.205)
print(
    'Hi ' + namer + ' According To My Records your Favourite Colour Is ' + colour + ' And You were born in ' + birth_year + ' Which Makes you ' + str(
        yearage) + ' Years Old. ' + ' You Weigh ' + str(weightkg) + ' Kilograms')
input("Press enter to exit;)")

#Doesn't work for some reason
if float(weightkg) < 60: print('You weight more than 60KG')
