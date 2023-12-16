from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not re.match(r"^\d{10}$", value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = None
        for p in self.phones:
            if p.value == phone:
                phone_to_remove = p
                break
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {', '.join([str(p) for p in self.phones])}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Create new address book
book = AddressBook()

# Create record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

# Create record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)


# Print all records in the address book
for record in book.data.values():
    print(record)

# Find and add new phone for John record in the address book
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

#Find some phone record in the address book
found_phone = john.find_phone("5555555555")
if found_phone:
    print(f"{john.name}: {found_phone}")

#Delete record Jane
book.delete("Jane")
