#Mad Libs
#The other day, I was really in trouble. It all started when I saw a very
#[adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
#I could think to do was to [verb] over and over. Miraculously,
#that caused it to stop, but not before it tried to [verb]
#right in front of my family.

#adjective = a word that describes a noun or pronoun
#animal = a noun
#verb_one = an action word
#exclamation = examples- Hooray! Yay! Ouch!
#verb_two = another action word
#verb_three = another action word

print("Let's create a fun story together. Please fill in the following information:" + '\n')
#I used "double quotes" ^above because the sentence has a single quote

adjective = input('An adjective (a descriptive word): ')
animal = input('An animal: ')
verb_one = input('A verb (action word): ')
exclamation = input('An exclamation (e.g.: Hooray! Ouch!): ')
verb_two = input('Another verb: ')
verb_three = input('Another verb: ')

print('\n' + "Here's your fun story:" + '\n')

print("The other day, I was really in trouble. It all started when I saw a very " + adjective + ' ' + animal + ' ' + verb_one + " down the hallway.")
print('"' + exclamation.upper() + '!"' + ' I yelled. But all I could think to do was to ' + verb_two + ' over and over. ')
print('Miraculously, that caused it to stop, but not before it tried to ' + verb_three + ' right in front of my family.')


