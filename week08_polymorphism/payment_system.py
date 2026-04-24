class Payment_jcs:
    def pay_jcs(self_jcs):
        print("Processing payment")

class CashPayment_jcs(Payment_jcs):
    def pay_jcs(self_jcs):
        print("Payment made using cash")

class CardPayment_jcs(Payment_jcs):
    def pay_jcs(self_jcs):
        print("Payment made using credit card")

payments_jcs = [CashPayment_jcs(), CardPayment_jcs()]
for p_jcs in payments_jcs:
    p_jcs.pay_jcs()