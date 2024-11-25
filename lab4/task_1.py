class Bank:
    def __init__(self, name="", num_clients=0, num_loans=0, budget= 1000000):
        # Приватні поля
        self.__name = name
        self.__num_clients = num_clients
        self.__num_loans = num_loans
        self.__budget = budget
        # Публічні поля
        self.rating = 0.0 
        self.country = ""

    def get_name(self):
        return self.__name

    def get_num_clients(self):
        return self.__num_clients

    def get_num_loans(self):
        return self.__num_loans
    
    def get_budget(self):
        return self.__budget

    def set_name(self, name):
        self.__name = name

    def set_num_clients(self, num_clients):
        self.__num_clients = num_clients

    def set_num_loans(self, num_loans):
        self.__num_loans = num_loans

    def set_budget(self, a):
        self.__budget -= a

    def __str__(self):
        return f"Bank(name={self.__name}, clients={self.__num_clients}, loans={self.__num_loans}, rating={self.rating}, country={self.country})"

    def __repr__(self):
        return f"Bank(name={self.__name!r}, clients={self.__num_clients!r}, loans={self.__num_loans!r}, rating={self.rating!r}, country={self.country!r})"

    def __del__(self):
        print(f"Bank {self.__name} is being destroyed")

def main():
    bank1 = Bank("Bank of America", 5000, 200)
    bank1.rating = 4.5
    bank1.country = "USA"

    bank2 = Bank("PrivatBank", 10000, 1500)
    bank2.rating = 4.8
    bank2.country = "Ukraine"

    bank3 = Bank()
    bank3.set_name("HSBC")
    bank3.set_num_clients(8000)
    bank3.set_num_loans(300)
    bank3.rating = 4.2
    bank3.country = "UK"
    bank1.set_budget(100000)
    bank2.set_budget(900000)
    bank3.set_budget(200000)

    print(bank1)
    print(bank2)
    print(bank3)
    bank_list = [bank1,bank2,bank3]
    min_bank = bank_list[0]
    for bank in bank_list:
        if bank.get_budget() < min_bank.get_budget():
            min_bank = bank
    print("Найбідніший банк:",min_bank.get_name())
# if __name__ == "__main__":
main()
