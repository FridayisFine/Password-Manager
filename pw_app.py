## My modules begin here. I am importing the csv, os, password_manager, and PasswordManager modules. 
## os allows my program to work along side the operating system.
## csv allows my program to work with and understand csv formatting.
## Password_Manager is a package that includes the resources for the passwordmanager class.

import os
import csv
from password_manager import PasswordManager

################## TODO ##################
# Check if a master username/password exists. 
# If no master account exists, prompt the user to create one. 
# If a master account exists, attempt to log in with username and password.

#figure out how to stop the programming from breaking when no input is entered.

################## TODO ##################

def pw_menu(pm):
  pm.load_passwords()
  authenticated = False
  while not authenticated: #This loop and try block prevents logging in with no entries or bad passwords/usernames
    if not os.path.exists(pm.filename):
      print("\nThat account was not found. Let's make that account now using the file name you just entered.\n")
      try:
        master_user = input("What do you want the user name to be for your account?\n")
        master_pass = input("What password do you want to use to access your account?\n")
        pm.create_master(master_user, master_pass)
        print("Great! You've created your account's file name and password.\n")
        authenticated = True
      except ValueError as bad:
        print("Oh no, that didn't work. Instead this happened: {bad}\n\n Let's try again, alright?\n")
    else:
      print("\nLog in to your account by entering your user name and password.\n")
      master_user = input("Username: ")
      master_pass = input("Password: ")
      if pm.login(master_user, master_pass):
        print("You are now logged in!")
        authenticated = True
      else:
        print("That isn't right, but you can try again!")

#Previous code block for logging in. commenting out in case while loop breaks the program. Can be removed at a later date as desired. 
#This code block would error if pw was left empty and would sometimes allow logins with bad pws.
#    master_user = input("What do you want your user name to be for this password manager? Enter it here: ")
#    master_pass = input("Good name! Now, what do you want your password to be? Enter it here: ")
#    pm.create_master(master_user, master_pass)
#    print("Success! You created your main account!")
#
#  else: 
#    print("Please log into your account.")
#    while True: #loop added to prevent logging in without a password
#      master_user = input("Username: ")
#      master_pass = input("Password: ")
#      if pm.login(master_user, master_pass):
#        print("Great, you're logged in!")
#        break
#      else:
#        print("That wasn't right. You can try again.")

# Main Password Manager application logic

  while True:
    print("\n--- Password Manager ---")
    print("1. View Passwords")
    print("2. Add Password")
    print("3. Delete Password")
    print("4. Exit\n")
    choice = input("Enter your choice: ")

    if choice == '1':
      pm.load_passwords()
      if pm.password_entries: #This ensures that there will be a response even if there is no passwords saved.
        print("\nHere are your saved passwords:\n")
        for service, details in pm.password_entries.items():
          print(f"Website: {service}")
          print(f"Username: {details['username']}")
          print(f"Password: {details['password']}\n")
      else: 
        print("\nThere are no passwords saved yet. Select option 2 to add a new password.")

    elif choice == '2':
      web_address = input("\nWhat website will this login in be for? ")
      username = input("What is your username for this website? ")
      password = input("What is your password for this website? ")
      pm.add_password(web_address, username, password)
      pm.save_passwords() #this should save the file after adding the new password.
      print("\nYour username and password are now saved!")

    elif choice == '3':
      web_address = input("\nWhich website do you want to forget?")
      pm.delete_password(web_address)
      pm.save_passwords() #this will save the 'delete' request to the file!
      print(f"\n{web_address} is forgotten! It has been deleted.")

    elif choice == '4':
      pm.save_passwords() #this is a 'save on exit' option.
      print("\nYour changes, if any, were saved! This program has finished its task.\n")
      break

    else:
      print("\nThat's not one of the options today. Please enter either: 1, 2, 3, or 4!")

def main(): #This is the log in part of the program. A while loop was added to prevent logging in without a pw or crashing from a bad entry
  
  filename = input("\nOpen your password manager or create a new password manager.\nTo open your password manager enter the name your saved file.\nTo make a new password manager enter a name for your new file.\nYour file name should be one word without spaces.\n\nEnter the file name here:")
  pm = PasswordManager(filename)
  pw_menu(pm) 
  return 0

if __name__ == '__main__':
  main()