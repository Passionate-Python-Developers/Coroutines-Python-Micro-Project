import time as t


def NameSearcher():
    names = ["Sannidhya", "Akash", "Rohan", "Haris", "Nikhil", "Abdul",
             "Vivek", "Rony", "Albert", "Newton", "Bill", "Shalini", "SkillF"]
    t.sleep(4)
    while True:
        text = (yield)
        if text in names:
            print("Your name is in the list")
        else:
            print("The name is not in the list.")


search = NameSearcher()
next(search)
search.send(input("Enter the name to search"))
print("Thank You for using our system. Do visit again :)")
search.close()
