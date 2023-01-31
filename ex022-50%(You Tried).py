#I probably wrote the code in the wrong way, but I tried.
'''name = input('What is your name?')
upper = name.upper()
lower = name.lower()
split = name.split()
len(split[0]), len(split[1]), len(split[2])
length = len(split[0]) + len(split[1]) + len(split[2])
name0 = len(split[0])
print(upper, lower, length, name0)'''
name = str(input('Enter your name:')).strip()
print('Analyzing your name...')
print('Your name in upper is {}.'.format(name.upper()))
print('Your name in lower is {}.'.format(name.lower()))
print('Your name have,altogether,{} letters.'.format(len(name)-name.count(' ')))
#print('Your first name have {} letters.'.format(name.find(' ')))"First Way"
split = name.split()
print('Your first name: {} have {} letters.'.format(split[0], len(split[0])))
#Well, I tried a lot and I hit low things about this exercise. I need keep much attention about what I'm trying to code.