"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
while not score < 0 or score>100:
    if score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")
    score = float(input("Enter score: "))
print('Invalid score')
