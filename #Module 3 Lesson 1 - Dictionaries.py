#Module 3 Lesson 1 - Dictionaries
#Task 1
#Given:
from idlelib.pyshell import restart_line
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#Add a new category called "Beverages" and add 2 items

restaurant_menu['Beverages'] = {'Coffee: 4.95', 'Soda: 3.35'}

print(restaurant_menu)

#Update Steak to 17.99

restaurant_menu["Main Course"]["Steak"] = "17.99"
print(restaurant_menu)

#Remove "Bruschetta" from "Starters"


print(restaurant_menu.keys("Starters")())