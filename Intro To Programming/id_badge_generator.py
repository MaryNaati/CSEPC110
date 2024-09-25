#Individual Activity: ID Badge Generator

#Assignment
##Write a program to propmt the user for the following:

#First Name     X
#Last Name      X
#Email Address  X
#Phone Number   X
#Job Title      X
#ID Number      X

#Additional requirements
##The last name should be converted from whatever the user types to be displayed in ALL CAPS.     X
##The job title should be displayed so that the first letter is Capitalized.                      X
##The email address should be displayed in all lowercase.                                         X

print('Please enter the following information:')

#Basic Information Required
first_name = input('First Name: ')
last_name = input('Last Name: ')
email_address = input('Email Address: ')
phone_number = input('Phone Number: ')

#Testing how to get a phone number to come out like (123)456-7890
area_code = phone_number[:3]
central_office = phone_number[3:6]
station_code= phone_number[6:]

job_title = input('Job Title: ')
id_number = input('ID Number: ')

#Stretch Additional Information
hair_color = input('Hair Color: ')
eye_color = input('Eye Color: ')
month_started = input('Month Started: ')
completed_advanced_training = input('Completed Advanced Training: ')

#Basic Output
print('\n')
print('The ID Card is: ' + '\n')

print(last_name.upper() + ', ' + first_name.capitalize())
print(job_title.capitalize())
print(id_number + '\n')

print(email_address.lower())

#Phone number out put
phone_number = "(" + area_code  + ") " + central_office + ' - ' + station_code 
print(phone_number + '\n')


#Stretch Output
print(hair_color.lower() + '\t' + eye_color.lower())
print(month_started + '\t' + completed_advanced_training)

#STRETCH CHALLENGE
## 1. Add hair color and eye color and put them both on the same line in the display.                 X
## 2. Add a field for the name of the month they started and 
# also a yes/no field for whether they have completed advanced training.
# Put these both on the same line in the display.                                                     X
## 3. For the two lines that you just added, 
# make it so that the second columns align, regardless of how many letters are in the responses.      X
# To complete this one, you may need to search the internet for something like, 
# "python spacing format" or something similar to see if you get any ideas.