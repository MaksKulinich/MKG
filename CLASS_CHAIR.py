class CHAIR():
    name = ""
    color = ""
    price = 0.0
    material = ""
    def init(self,nm, cl, pr, mt):
        self.name = str(nm)
        self.color = str(cl)
        self.price = float(pr)
        self.material = str(mt)
    def new(self, new_price):
        self.price = float(new_price)
x = CHAIR()
y = x.init("Стілець", "Сірий", 999.99, "Метал")
print("Початкова ціна ", x.price) 
z = x.new(1199.99)
print("Нова ціна ", x.price)     