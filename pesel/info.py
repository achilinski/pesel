class Info:
    def __init__(self, pesel: str):
        self.pesel = str(pesel)
        self.year = 0
        self.month = 0
        self.day = 0
        self.men=[1, 3, 5, 7, 9 ]
        self.gender = None

    def gender_getter(self):
        if int(self.pesel[9]) in self.men:
            self.gender = 'men'
        else:
            self.gender = 'women'
        return self.gender

    def number_lister(self):
        self.pesel = [int(x) for x in self.pesel]

    def birth_date(self):
        self.number_lister()
        self.month = self.pesel[3]
        self.day = int(self.pesel[4]) * 10 + int(self.pesel[5])
        if int(self.pesel[2]) <= 1:
            self.year = 1900 + int(self.pesel[0]) * 10 + int(self.pesel[1])
            return self.year, self.month, self.day
        if 1 < int(self.pesel[2]) <= 3:
            self.year = 2000 + int(self.pesel[0]) * 10 + int(self.pesel[1])
            return self.year, self.month, self.day
        if 3 < int(self.pesel[2]) <= 5:
            self.year = 2100 + int(self.pesel[0]) * 10 + int(self.pesel[1])
            return self.year, self.month, self.day
        if 5 < int(self.pesel[2]) <= 7:
            self.year = 2200 + int(self.pesel[0]) * 10 + int(self.pesel[1])
            return self.year, self.month, self.day
        if 7 < int(self.pesel[2]) <= 9:
            self.year = 1800 + int(self.pesel[0]) * 10 + int(self.pesel[1])
            return self.year, self.month, self.day
