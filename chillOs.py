# Define variables, lists, and import functions.


import math
import base64
from datetime import datetime, timedelta, timezone
from prompt_toolkit import prompt
import time


file_name=[]
file_data=[]
sudofile_name=[]
sudofile_data=[]
username = input("Enter a username: ")
pswrd = input("Enter a password: ")
utc_now = datetime.now(timezone.utc)
utc_time = utc_now.strftime("%Y-%m-%d %H:%M:%S")
foreverloop = True
lastcommand = "False"


# function for password attempts


def pswrd_attempt(attempt):
   global is_pswrdcorrect


   if attempt == pswrd:
       is_pswrdcorrect = True
       return "Password correct!"
   else:
       return "Password incorrect."


#define all commands


#files here


def file_create(nam):
   file_name.append(nam)
   file_data.append("")
   print("File created")


def file_edit(na):
   if na in file_name:
       return file_data[file_name.index(na)]
   else:
       print("Not a valid file")


def file_rename():
   na=input("Old name: ")
   if na in file_name:
       new=input("New name: ")
       file_name[file_name.index(na)]=new
   else:
       print("File chosen doesn't exist")


def sudofile_create(nam):
   sudofile_name.append(nam)
   sudofile_data.append("")
   print("File created")


def sudofile_edit(na):
   if na in sudofile_name:
       return sudofile_data[sudofile_name.index(na)]
   else:
       print("Not a valid file")


def sudofile_rename():
   na=input("Old name: ")
   if na in sudofile_name:
       new=input("New name: ")
       sudofile_name[sudofile_name.index(na)]=new
       print("Succesfully renamed")
   else:
       print("File chosen doesn't exist")


# misc here


def list_commands():
   return f"THERE ARE 28 TOTAL COMMANDS.\n\nTYPE: FILES\n\nfile_create\tcreates a new file.\nfile_rename\trenames a file.\nfile_edit\tallows you to write to a file.\nfile_view\tallows you to read a file's contents.\nsudofile_create\tcreates a new private file, which requires a password to read and write to.\nsudofile_rename\trenames a private file.\nsudofile_edit\tallows you to write to a private file, but requires a password.\nsudofile_view\tallows you to read a private file's contents, but requires a password to access.\nsudo_wipe(password)\tdeletes all files and data.\ndir\tshows directory with all filenames.\nstor\tShows amount of storage left (x/5 normal files & y/2 private files)\n\nTYPE: MISC\n\nlist_commands\tlists all available commands.\ndatetimef\treturns the date and time.\nsudo_newpswrd(oldpswrd, newpswrd)\tallows you to create a new password.\nsudo_renameuser(newname, password)\tallows the user to rename themselves.\nsudo_last\tprints the previous command.\npowoff\tshuts down the OS.\n\nTYPE: FUNCTIONAL/CALCULATOR\n\nadd(x, y)\tadds 2 numbers\nsub(x, y)\tsubtracts one number from another\nmult(x, y)\tmultiplies 2 numbers.\ndiv(x, y)\tdivides one number by another.\nsqrt(num)\ttakes the square root of a number\nexp(x, power)\tmultiplies a number by itself a set amount of times.\nmod(x, y)\tfinds the remainder of a division equation.\nbase64(input)\tconverts an input to base64 binary.\n"


def datetimef():
   utc_now = datetime.now(timezone.utc)
   return f"UTC: {utc_now.strftime("%Y-%m-%d %H:%M:%S")}"


def sudo_newpswrd(oldpswrd, newpswrd):
   global pswrd


   if oldpswrd == pswrd:
       pswrd = newpswrd
       return "Success!"
   else:
       return "Sorry, wrong password."


def sudo_renameuser(pswrdcheck, newuser):
   global pswrd
   global username
   if pswrdcheck == pswrd:
       username = newuser
       return f"Password correct.\n\nNew username:\t{username}!"
   else:
       return "password incorrect."


def info():
   return f"chiilOS copyright Zack & Jacob co 2026 Voorhees High School, Glen Gardener, NJ.\n\nJacob: File directories.\n\nZackary: system funtionality and misc commands.\n\nchillOS ver. beta 0.6.1"


# calc commands


def add(a, b):
   return a + b


def sub(a, b):
   return a - b
 
def mult(a, b):
   return a * b


def div(a, b):
   if b == 0:
       return "div by 0 error"
   else:
       a / b




#start OS


print(f"Hello, {username}, the time and date is {utc_time}.\n\nUse ‘list_commands’ for the command list!")


# command checker
command = "False"


while foreverloop ==  True:
    lastcommand = command
    is_pswrdcorrect = False
    command = str(input(f"\nC:/chillOS/{username}@github.codespaces/shell: "))
    print(f"Your command: {command}\n")


    if command == "list_commands":
       print(list_commands())
    elif command == "datetimef":
       print(datetimef())
    elif "sudo_newpswrd(" and ")" in command:
      parts = [part.strip() for part in command[14:].split(",")]
      print(sudo_newpswrd(parts[0], parts[1][:-1]))
    elif "sudo_renameuser(" and ")" in command:
       parts = [part.strip() for part in command[16:].split(",")]
       print(sudo_renameuser(parts[0], parts[1][:-1]))
    elif command == "info":
       print(info())
    elif command == "powoff":
       shutoff = input("Shutting down deletes all data forever. Do you wish to continue? y/n: ")
       if shutoff == "y":
           print("shutting down...\n")
           time.sleep(0.25)
           break
       else:
           print("OK, not shutting off.")
    elif command == "sudo_last":
       print(pswrd_attempt(input("input password: ")))
       if is_pswrdcorrect == True:
           print(lastcommand)
       else:
           print("command cannot run.")
    elif "add(" and ")" in command:
       parts = [part.strip() for part in command[4:].split(",")]
       print(add(int(parts[0]), int(parts[1][:-1])))
    elif "sub(" and ")" in command:
       parts = [part.strip() for part in command[4:].split(",")]
       print(sub(int(parts[0]), int(parts[1][:-1])))
    elif "mult(" and ")" in command:
       parts = [part.strip() for part in command[5:].split(",")]
       print(mult(int(parts[0]), int(parts[1][:-1])))
    elif "div(" and ")" in command:
       parts = [part.strip() for part in command[4:].split(",")]
       print(div(int(parts[0]), int(parts[1][:-1])))
    elif command == "file_create":
       nam=input("File Name: ").lower()
       file_create(nam)
    elif command == "file_edit":
       na=input("File name:")
       if na in file_name:
           file_data[file_name.index(na)]=prompt(default=file_edit(na))
       else:
            print("File entered doesnt exist")
    elif command == "file_view":
       na=input("File name:")
       if na in file_name:
           print(file_data[file_name.index(na)])
       else:
           print("File entered doesnt exist")
    elif command == "file_rename":
       file_rename()
    elif command == "sudofile_create":
       pswrd_attempt(input("Enter password: "))
       sudofile_create(input("File name: "))
    elif command == "sudofile_edit":
       pswrd_attempt(input("Enter password: "))
       na=input("File name: ")
       if na in sudofile_name:
           sudofile_data[sudofile_name.index(na)]=prompt(default=sudofile_edit(na))
       else:
            print("File entered doesnt exist")
    elif command == "sudofile_view":
       pswrd_attempt(input("Enter password: "))
       na=input("File name:")
       if na in sudofile_name:
           print(sudofile_data[sudofile_name.index(na)])
       else:
           print("File entered doesnt exist")
    elif command == "sudofile_create":
       pswrd_attempt(input("Enter password: "))
       sudofile_create(input("File name: "))
    else:
       print("Error: command does not exist.")
