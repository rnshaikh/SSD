import json
from customer import Customer
from card import Card
from account import Bank, Account
from atm import ATM

from card_reader import CardReader
from cash_dispenser import CashDispenser
from deposit_slot import CashDepositSlot, ChequeDepositSlot
from printer import Printer
from screen import Screen
from cheque import Cheque


if __name__ == "__main__":
    sc = Screen()
    cr = CardReader()
    cd = CashDispenser()
    cads = CashDepositSlot()
    chds = ChequeDepositSlot()
    pr = Printer()
    atm = ATM(sc, cr, cd,
              chds, cads, pr)
    atm.add_cash(100000000)
    while True:
        card_inp = str(input("enter card detail: by comma seprated\n"))
        card_inp = card_inp.split(",")
        no, cvv, expiry = card_inp[0], card_inp[1], card_inp[2]
        account = atm.card_reader.read_card(atm, no)

        while True:
            ch = atm.screen.print_msg_input(
                """
                    1. enquiry
                    2. deposit
                    3. tranfer
                    4. withdraw
                """)
            ch = int(ch)

            if ch == 1:
                atm.enquiry()

            elif ch == 2:
                dp_ch = atm.screen.print_msg_input("1. deposit by cash \n2. deposit by cheque.")
                dp_ch = int(dp_ch)
                if dp_ch == 1:
                    amount = atm.screen.print_msg_input("Enter cash:")
                    amount = int(amount)
                    atm.cash_deposit_slot.accept(amount)
                    atm.add_cash_customer(amount)

                else:
                    msg = atm.screen.print_msg_input("bearer, amount, customer_name")
                    bearer, amount, account_no = msg.split(",")
                    amount = int(amount)
                    cheque = Cheque(bearer, amount, account_no)
                    atm.cheque_deposit_slot.accept(cheque)
                    atm.add_cash_customer(amount)

            elif ch == 3:
                account_no, amount = input("1.enter account no to transfer, amount").split(",")
                amount = int(amount)
                atm.transfer(account_no, amount)
                print("transfer is successful")

            elif ch == 4:
                amount = atm.screen.print_msg_input(
                """
                    enter amount:
                """)

                amount = int(amount)
                atm.debit_cash(amount)
                atm.screen.print_(atm.cash_dispenser.dispense_cash(amount))
        break





