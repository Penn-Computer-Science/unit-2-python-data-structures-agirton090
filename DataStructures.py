#Part 1: Lists
1. #Create a list of 10 numbers.
2. #Print the first, last, and middle number.
3. #Add a new number to the end of the list.
4. #Replace the third number with 99.
5. #Loop through the list and print only the even numbers.
print("------------------------------------")
numbers = list(range(1, 11))

print("First Number: ", numbers[0])
print("Last Number: ", numbers[-1])
print("Middle Number: ", numbers[6])

numbers.append(11)

numbers[2] = 99

print("Even Numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

#---

#Part 2: Dictionaries
#1. Create a dictionary of 5 countries and their capitals.
#2. Print the capital of 2 countries.
#3. Add a new country-capital pair.
#4. Change the capital of one country.
#5. Loop through and print all countries and capitals.
print("------------------------------------")
countries = {
"USA": "Washington D.C. ",
"Germany": "Berlin ",
"France": "Paris ",
"Japan": "Tokyo ",
"India": "New Delhi "
}

print("Capital of France: ", countries["France"])
print("Capital of Japan: ", countries["Japan"])

countries["Italy"] = "Rome"

countries["Japan"] = "Kyoto"

print("All countries and capitals:")
for country, capital in countries.items():
    print(country, "-", capital)
#---
#Part 3: Sets
#1. Create a set of your favorite fruits.
#2. Add a new fruit, then remove one.
#3. Create another set of fruits your friend likes.
#4. Print:
  # - Fruits you both like (intersection).
   #- Fruits only you like (difference).
   #- All fruits either of you like (union).
print("------------------------------------")
fruits = {"Apple", "Mango", "Banana", "Grapes"}

fruits.add("Orange")

fruits.remove("Banana")

friend_fruits = {"Mango", "Peach", "Orange", "Strawberry"}

print("Fruits we both like: ", fruits & friend_fruits)

print("Fruits I only like: ", fruits - friend_fruits)

print("All fruits either of us like: ", fruits | friend_fruits)
#---

#Part 4: Tuples
#1. Create a tuple of 5 colors.
#2. Print the first and last color.
#3. Loop through the tuple and print each color.
#4. Try to change one color (note the error).
print("------------------------------------")
colors = ("Red", "Blue", "Green", "Yellow", "Purple")

print("First color: ", colors[0])
print("Last color: ", colors[-1])

print("All colors in the tuple: ")
for color in colors:
    print(color)

print("Trying to change a color in a tuple: ")
colors[2] = "Black"

#This doesn't work since tuples are immutable.