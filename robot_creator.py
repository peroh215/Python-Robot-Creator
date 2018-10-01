# /usr/bin/python
#-*- coding: utf-8 -*-

print("Loading...")

# Variables
usr = ''
helplist = '''--- Commands ---
!create - Creates a new robot
!list - Displays a list of created robots
!show - Shows information about a specific robot
!about - Displays information about the program'''
robots = []
rid = 1
aboutmsg = '''
===============================
File name: robot_creator
Version: 1.0
Author: Blackman White                     
Date created: 9/30/2018              
Date last modified: 9/30/2018        
Python Version: 3.7
=================================
'''

# Functions
class Robot:
    def __init__(self, name, color):
        global rid
        self.name = name
        self.color = color
        self.id = rid
        rid += 1

    def info(self):
        print("\n----- {}'s information -----".format(self.name))
        print("Name:", self.name)
        print("Color:", self.color)
        print("ID:", self.id)
        print("------------------------------")

def menu():
    global usr
    usr_i()

    if usr == "!help":
        print(helplist)
        menu()
    elif usr == "!create":
        create_r()
        menu()
    elif usr == "!list":
        list_r()
        menu()
    elif usr == "!show":
        show_r()
        menu()
    elif usr == "!about":
        print(aboutmsg)
        menu()
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
    a = input("Name: ")
    b = input("Color: ")
    r = Robot(a,b)
    robots.append(r)

def list_r():
    global robots
    if not robots:
        print("There are no robots existent, type !create to create a robot")
        return None
    print("------ Robots ------\n")
    for robot in robots:
        print("[{}] {}".format(robot.id,robot.name))
    print("\n--------------------")

def show_r():
    global robots
    if not robots:
        print("There are no robots existent, type !create to create a robot")
        return None
    usr = input("Enter robot name: ")
    robot_found = False
        
    for robot in robots:
        if usr == robot.name:
            robot_found = True
            robot.info()
            return None
        
    if robot_found == False:
        print("Robot not found")
    
# Main
print("===== Menu =====")
print("Type !help to see commands")
menu()

