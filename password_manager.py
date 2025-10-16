################## TODO ##################
# Add Modules


import csv #tells python how to work with csv
import os #tells python how to look for the password file
import string #needed for generate_password
import random #needed for generate_password 

class PasswordManager:
  DEFAULT_FILENAME = "passwords.csv"
  DEFAULT_LENGTH = 8

  def __init__(self, filename=None, invalid_chars=None):
    if invalid_chars is None:
      invalid_chars = [] #Tried to set up an invalid list but had issues getting it to work. Leaving the list blank does not hurt the rest of the code. If I can figure this out before turning in the project then this comment will be removed. 
    if not isinstance(invalid_chars, list):
      raise ValueError("There are no invalid characters. Check Class Password manager over in password_manager.py to see what might have gone wrong.")

    self.filename = filename if filename is not None else self.DEFAULT_FILENAME
    self.invalid_chars = invalid_chars
    self.master_account = {}
    self.password_entries = {}
    self.load_passwords()

  def validate_password(self, password):

################## TODO ##################
# Validate the password
################## TODO ##################

    if any(char in password for char in self.invalid_chars):
      raise ValueError("Password contains an invalid character. This shouldn't be happening, because the invalid list is empty. How did this break happen?")

  def create_master(self, username, password):

################## TODO ##################
# Create master password
################## TODO ##################

    if not username or not password:
      raise ValueError("You left a feild blank, try again!")

    self.validate_password(password)

    self.master_account = {
      'username' : username,
      'password': password
    }

  def login(self, username, password):

################## TODO ##################
# Validate master password
################## TODO ##################

    return self.master_account.get('username') == username and self.master_account.get('password') == password

  def load_passwords(self):

################## TODO ##################
# Load password entries from file
################## TODO ##################

    try:
      with open(self.filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

      if not rows:
        return

      master_row = rows[0]
      if master_row.get('service') != 'master':
        raise ValueError("File format does not match master account, try again.")

      self.master_account = {
        'username' : master_row.get('username'),
        'password' : master_row.get('password')
      }

      self.password_entries = {}
      for row in rows[1:]:
        if 'service' in row and 'username' in row and 'password' in row:
          self.password_entries[row['service']] = {
            'username' : row['username'],
            'password' : row['password']
          }
    except FileNotFoundError:
      pass
    except Exception:
      raise ValueError("Oh no! Something went wrong. Check above line 201 for a password loading error.")

  def save_passwords(self):

################## TODO ##################
# Save password entry
################## TODO ##################

    with open(self.filename, mode='w', newline='') as file:
      fieldnames = ['service', 'username', 'password']
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()

      if self.master_account:
        writer.writerow({
        'service': 'master',
        'username' : self.master_account.get('username'),
        'password' : self.master_account.get('password')
        })

      for service, data in self.password_entries.items():
        writer.writerow({
          'service': service,
          'username': data.get('username'),
          'password': data.get('password')
        })
  def add_password(self, service, username, password):

################## TODO ##################
# Add password entry
################## TODO ##################

    if not service or not username or not password:
      raise ValueError("Website, username, and password cannot be empty.")

    self.validate_password(password)

    self.password_entries[service] = {
      'username': username,
      'password': password
    }

  def delete_password(self, service):

################## TODO ##################
# Delete password entry
################## TODO ##################

    if service in self.password_entries:
      del self.password_entries[service]
      return True
    return False

  def generate_password(self, length=DEFAULT_LENGTH, include_numbers=True, include_symbols=True):

################## TODO ##################
# Generate a random password
################## TODO ##################

    if length < 1:
      raise ValueError("Passwords must be at least 1 character.")

    characters = string.ascii_letters
    if include_numbers:
      characters += string.digits
    if include_symbols:
      symbols = [s for s in string.punctuation if s not in self.invalid_chars]
      characters += "".join(symbols)

    if not characters: 
      raise ValueError("Something went wrong with your character inputs")

    password = "".join(random.choice(characters) for _ in range(length))
    self.validate_password(password)
    return password