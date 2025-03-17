'''
The Beatles were one of the most popular music group of the 1960s, and the best-selling band in history. Some people consider them to be the most influential act of the rock era. Indeed, they were included in Time magazine's compilation of the 20th Century's 100 most influential people.

The band underwent many line-up changes, culminating in 1962 with the line-up of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).


Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.
By the way, are you a Beatles fan? (The Beatles is one of Greg's favorite bands. But wait...who's Greg...?)


'''

'''
# Step 1: Create an empty list named beatles
beatles = []
print("Step 1:", beatles)

# Step 2: Add John Lennon, Paul McCartney, and George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3: Prompt the user to add Stu Sutcliffe and Pete Best
for _ in range(2):  # Loop twice to add two members
    member = input("Enter a band member: ")
    beatles.append(member)
print("Step 3:", beatles)

# Step 4: Remove Stu Sutcliffe and Pete Best
del beatles[-2:]  # Removes the last two elements (Stu Sutcliffe and Pete Best)
print("Step 4:", beatles)

# Step 5: Add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Testing the list length
print("The Fab", len(beatles))


'''

'''
my_list = ["white", "purple", "blue", "yellow", "green"]

for _ in range(2):

    new_color = input("add more colors: ")

    my_list.append(new_color)
     
print(my_list)

del my_list[0]

print("Updated List: ", my_list)

'''

'''
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
print(lst)
del lst[0]
print(lst)
lst.append(1)

print(lst)


'''

#sorting
lst=[5,3,1,2,4]
lst.sort()
lst.reverse()
print(lst)

