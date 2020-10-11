
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]


names_and_heights = zip(names, heights)
print(names_and_heights)

print(list(names_and_heights))

#Example

dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = (list(names_and_dogs_names))

print(list_of_names_and_dogs_names)

#Exercises

first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

age = []

all_ages = age + [32, 41, 29]

all_ages.append(42)

name_and_age = zip(first_names, all_ages)

ids = range(4)