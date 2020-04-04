class Validator:
    def __init__(self,pesel):
        self.pesel=pesel
        self.last_digit=0
        self.control_number=0

    def checker(self):
        if len(self.pesel) != 11:
            raise ValueError

        self.last_digit=int(self.pesel[10])
        self.control_number=(9*int(self.pesel[0])+7*int(self.pesel[1])+3*int(self.pesel[2])
                             +int(self.pesel[3])+9*int(self.pesel[4])+7*int(self.pesel[5])
                             +3*int(self.pesel[6])+int(self.pesel[7])+9*int(self.pesel[8])
                             +7*int(self.pesel[9]))
        if self.control_number % 10 != self.last_digit:
            raise ValueError

        if self.pesel == '00000000000' :
            raise ValueError








