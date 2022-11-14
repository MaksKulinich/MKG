class Nat():
    Value = 10
    Divs = [1, 2, 5, 10]
    def init(self, vl, dv):
        self.Value = int(vl)
        self.Divs = dv
    def CalcDivs(self, x):
        self.Value = int(x)
        sp = []
        for i in range(1, x+1):
            if x%i==0:
                sp.append(i)
        self.Divs = sp
    def DisplayValue(self):
        print(self.Value)
    def SetValue(self, numb):
        self.Value = int(numb)
    def DisplayDivs(self):
        rd = ''
        for i in self.Divs:
            rd+= str(i) + " "
        self.Divs = rd
#x = Nat()
#y = x.CalcDivs(66)
#print(x.Divs)
#p = x.DisplayDivs()
#print(x.Divs)
#print("Число", x.Value, "та його дільники", x.Divs)