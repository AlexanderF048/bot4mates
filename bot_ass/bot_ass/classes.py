from collections import UserDict
from dateutil import parser
from datetime import *


class Field:
	def __init__(self, value):
		self.value = value
		self._value = value


class Name(Field):
	pass

class Phone(Field):
	def __checkValue(x):
		if x.isnumeric():
			return True
		return False

	@property
	def value(self):
		return self._value


	@value.setter
	def value(self, x):
		if Phone.__checkValue(x):
			self._value = x
		elif x.startswith('+'):
			self._value = x[1:]
		else:
			return ('This phone format is unacceptable!')


class Birthday(Field):

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, x):
		if '-' in x or ':' in x or '/' in x or '.' in x:
			self._value = x
		elif ' ' in x:
			x = x.replace(' ', '-')
			self._value = x
		else:
			raise ValueError('This birthday format is unacceptable!')


class Email(Field):

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, x):
		self._value = x


class Address(Field):

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, x):
		self._value = x



class Record:
	def __init__(self, name):
		self.name = Name(name)
		self.phones = []
		self.birthday = None
		self.email = None
		self.address = None


	def add_phone(self, phone):
		self.phones.append(Phone(phone))

	def add_birthday(self, birthday):
		self.birthday = Birthday(birthday)

	def add_email(self, email):
		self.email = Email(email)

	def add_address(self, address):
		self.address = Address(address)

	def remove_phone(self, phone_to_remove):
		for phone in self.phones:
			if phone.value == phone_to_remove:
				self.phones.remove(phone)

	def edit_phone(self, phone_old, phone_new):
		for phone in range(len(self.phones)):
			if self.phones[phone].value == phone_old:
				self.phones[phone] = Phone(phone_new)


	def remove_birthday(self, name):
		if self.name.value == name:
				self.birthday = None

	def remove_address(self, name):
		if self.name.value == name:
				self.address = None

	def remove_email(self, name):
		if self.name.value == name:
				self.email = None

	def edit_birthday(self, name, birthday_new):
		if self.name.value == name:
				self.birthday = Birthday(birthday_new)

	def edit_address(self, name, address_new):
		if self.name.value == name:
				self.address = Address(address_new)

	def edit_email(self, name, email_new):
		if self.name.value == name:
				self.email = Email(email_new)


	def days_birthday(self):
		birth_day = parser.parse(self.birthday.value)
		birth_day = date(year = date.today().year, month = birth_day.month, day = birth_day.day)
		today = date.today()
		return (birth_day - today).days

class AddressBook(UserDict):
	def add_record(self, record):
		self.data[record.name.value] = record


	def search_contacts(self, text):
		if self.data:
			result = []
			for record in self.data.values():
				if (text in record.name.value) or (text in record.birthday.value) \
				or (text in record.address.value) or (text in record.email.value):
					result.append([record.name.value, record])
				for phone in record.phones:
					if text in phone.value:
						result.append([record.name.value, record])
			if result:
				return result
			else:
				return f'The contact(s) with "{text}" such data is not found'
		else:
			return "Adress Book is empty"