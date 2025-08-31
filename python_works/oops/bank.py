class Bank:

    bank_name : str

    person_name : str

    account_no : int

    balance : int

    def set_customer_detail(self,person_name,account_no,balance):

            self.bank_name = "SBI"

            self.person_name = person_name

            self.account_no = account_no

            self.balance = balance


    def bal_enq(self):

          print(f"dear {self.bank_name} customer your acc{self.account_no} avl balance is {self.balance}")
    
    def deposit(self,amount):

        self.balance += amount

        print(f"dear {self.bank_name} acc{self.account_no} has been credited with amount {amount} available balance is {self.balance}")
    

    def withdraw(self,amount):

        if self.balance>amount:

            self. balance -= amount

            print(f"dear {self.bank_name} acc{self.account_no} has been debited with amount {amount} available balance is {self.balance}")
          
        else:

            print("not sufficient")
   

bank_instance = Bank()

bank_instance.set_customer_detail("hari",1234,25000)

# bank_instance.deposit(1000)

bank_instance.withdraw(500)

# bank_instance.bal_enq(3000)
    