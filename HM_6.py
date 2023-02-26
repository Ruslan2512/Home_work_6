from collections import UserDict
from datetime import datetime
import re


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        
    
    def iterator(self, N):
        for i in self.data:
            while N:
                print(i)
                N -= 1
class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass
    


class Phone(Field):
    @property
    def set_phone(self):
        return self.value
    
    
    @set_phone.setter
    def set_phone(self):
        self.phone = re.findall(r'[+]*[0-9]{10,12}', self.value)
        if self.phone:
            return self.phone
        else:
            return None



class Birthday(Field):
    @property
    def set_birthday(self):
        return self.value
    
    
    @set_birthday.setter
    def set_birthday(self):
        self.birth = re.findall(r'[0-9]{4}[-]{1}[0-9]{2}[-]{1}[0-9]{2}', self.value)
        if self.birth:
            try:
                self.birth
            except ValueError:
                return None
        else:
            return None


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
            
    def days_to_birthday(self, day_of_birthday):
        if day_of_birthday:
            self.day_of_birthday = day_of_birthday.split('-') 
            self.birthday = datetime(int(self.day_of_birthday[0]), int(self.day_of_birthday[1]), int(self.day_of_birthday[2]))
            self.current_datetime = datetime.now()
            return self.current_datetime.date() - self.birthday.date()
        else:
            return None
    
    
    
    