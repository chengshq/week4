class BankAccount():

	def __init__(self):
		self.balance = 0.00

	def deposit(self, deposit_amount):
		self.balance += deposit_amount
		return self.balance

	def withdraw(self, withdraw_amount):
		if self.balance >= withdraw_amount:
			self.balance -= withdraw_amount

	def transfer(self, transfer_amount, receiver):
		if self.balance >= transfer_amount:
			self.balance -= transfer_amount
			receiver.balance += transfer_amount
