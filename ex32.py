the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this fist kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range fuction to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append is a function that lists Understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"elements was: {i}") 
