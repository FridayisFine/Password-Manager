"""
    password_manager.py

    This python module defines the PasswordManager class, which provides core functionality
    for managing passwords in a user-friendly manner. The PasswordManager class supports
    creating, storing, retrieving, and deleting passwords for various services, and ensures
    data is persisted in a CSV file. 

    The PasswordManager class includes the following key functionalities:
        - Master Account Management: Ensures that only authenticated users can access and
                                     manage stored passwords by implementing a master account
                                     system.
        - Password Generation: Supports generating secure passwords with customizable length,
                               inclusion of numbers, symbols, and excludes specific invalid
                               characters.
        - Data Persistence: Saves and loads password data to and from a CSV file.
        - Validation: Ensures that passwords adhere to defined rules, including exclusion of 
                      specified invalid characters, and handles user input errors gracefully.

    Usage Example:
        >>> from password_manager import PasswordManager
        >>> pm = PasswordManager("passwords.csv", [',', '=', ' '])
        >>> pm.create_master_account("admin", "password123!")
        >>> pm.add_password("Fake", "email@example.com", "password123!")
        >>> pm.save_passwords()

    Classes:
        - PasswordManager: Main class for managing the password-related functionality, 
                           including account creation, password generation, and file
                           operations.

    Exceptions:
        - ValueError: Raised due to invalid parameters.
"""

################## TODO ##################
# Add Modules
################## TODO ##################

import csv
import os
import string
import random

class PasswordManager:
    """
        A class to manage usernames and passwords for various services.

        Attributes:
            filename (str): The name of the file to save/load passwords.
            invalid_chars (list): List of invalid characters for passwords.
            master_account (dict): The master account containing the username
                                   and password.
            password_entries (dict): A dictionary of stored passwords for
                                     different services.
    """

    DEFAULT_FILENAME = "passwords.csv"
    DEFAULT_LENGTH = 8

    def __init__(self, filename=None, invalid_chars=None):
        """
            Initializes the PasswordManager with an optional filename and/or
            invalid password characters.

            Args:
                filename (str, optional): The filename to load passwords from.
                                          Defaults to "passwords.csv" if not
                                          provided.
                invalid_chars (list, optional): List of invalid characters
                                                that should not be included
                                                in passwords. Defaults to an
                                                empty list if not provided.

            Raises:
                ValueError: If invalid_chars is not list.
        """
        ################## TODO ##################
        # Validate filename and invalid characters
        # I did not include an invalid list of characters, leaving the list empty.
        ################## TODO ##################

        if invalid_chars is None:
            invalid_chars = []
        if not isinstance(invalid_chars, list):
            raise ValueError("the invalid_chars list is not working as intended. It should be empty and not causing errors.")
            
        self.filename = filename if filename is not None else self.DEFAULT_FILENAME
        self.invalid_chars = invalid_chars
        self.master_account = {}
        self.password_entries = {}
        self.load_passwords()
            
    def validate_password(self, password):
        """
            Validates if password contains any invalid characters.

            Args:
                password (str): The password to validate.

            Raises:
                ValueError: If passwords contains invalid characters.

            Returns:
                None
        """
        ################## TODO ##################
        # Validate the password
        ################## TODO ##################
        
        if any(char in password for char in self.invalid_chars):
            raise ValueError("Password contains an invalid character. This shouldn't be happening, because the invalid list is empty. How did this break happen?")

    def create_master_account(self, username, password):
        """
            Creates the master account.

            Args:
                username (str): The username for the master account.
                password (str): The password for the master account.

            Raises:
                ValueError: If passwords length is less than 1.

            Returns:
                None
        """
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

    def authenticate_master_account(self, username, password):
        """
            Authenticates the master account using the provided username and
            password.

            Args:
                username (str): The username of the master account.
                password (str): The password of the master account.

            Returns:
                bool: True if authentication is successful, False otherwise.
        """
        ################## TODO ##################
        # Validate master password
        ################## TODO ##################
        
        return self.master_account.get('username') == username and self.master_account.get('password') == password

    def load_passwords(self):
        """
            Loads passwords from the specified file.

            Raises:
                ValueError: For invalid file format with master account.

            Returns:
                None
        """
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
        """
            Saves the current passwords to the specified file.

            Returns:
                None
        """
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
            write.writerow({
                'service': service,
                'username': data.get('username'),
                'password': data.get('password')
            })
    def add_password(self, service, username, password):
        """
            Adds a new password entry or prompts to overwrite if the service
            already exists.

            Args:
                service (str): The name of the service.
                username (str): The username or email associated with the
                                service.
                password (str): The password for the service.

            Raises:
                ValueError: For input parameter validation.

            Returns:
                None
        """
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
        """
            Deletes a password entry by service name.

            Args:
                service (str): The name of the service whose password entry
                               should be deleted.

            Returns:
                bool: True if password successfully deleted, False otherwise.
        """
        ################## TODO ##################
        # Delete password entry
        ################## TODO ##################
        
        if service in self.password_entries:
            del self.password_entries[service]
            return True
        return False

    def generate_password(self, length=DEFAULT_LENGTH, include_numbers=True, include_symbols=True):
        """
            Generates a random password.

            Args:
                length (int, optional): The length of the password to
                                        generate. Defaults to 8.
                include_numbers (bool, optional): Whether to include numbers
                                                  in the password. Defaults to
                                                  True.
                include_symbols (bool, optional): Whether to include symbols
                                                  in the password. Defaults to
                                                  True.

            Raises:
                ValueError: If passwords length is less than 1.

            Returns:
                str: Randomly generated password.
        """
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