# /usr/bin/python
#-*- coding: utf-8 -*-

print("Loading...")

# Variables
usr = ''
helplist = '''--- Commands ---
!create - Creates a new robot
!show - Shows created robots '''
robots = []
rid = 1

# Functions
class Robot:
    def __init__(self, name):
        global rid
        self.name = name
        self.id = rid
        rid += 1

    def robot_info(self):
        print("----- Robot info -----")
        print("Name:", self.name)
        print("ID:", self.id)

def menu():
    global usr
    usr_i()

    if usr == "!help":
        print(helplist)
        menu()
    elif usr == "!create":
        create_r()
    elif usr == "!show":
        show_r()
    else:
        print("Invalid command")
        print("Type !help to see commands")
        menu()
        
def usr_i():
    global usr
    usr = input('\n> ')

def create_r():
    global usr
    print("\n===== Robot Creator =====")
    a = input("Name:")
    r = Robot(a)
    robots.append(r)
    menu()

def show_r():
    print("------ Robots ------\n")
    for robot in robots:
        print("{} - {}".format(robot.id,robot.name))
    print("--------------------")
    menu()
    
# Main
print("===== Menu =====")
print("Type !help to see commands")
menu()
