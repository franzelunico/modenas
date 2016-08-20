

class Conversor(object):
    nombre = ""
    liquido_pagable = 0
    entero = 0
    decimal = 0
    desperdicio = 0
    centavos = {"10": 0, "20": 0, "50": 0}

    def __init__(self, nombre, liquido_pagable):
        self.nombre = nombre
        self.liquido_pagable = round(liquido_pagable, 2)
        x = self.liquido_pagable
        self.entero = int(x)
        self.unidad = self.entero % 10
        self.entero = self.entero - self.unidad

        decimal = round(abs(x) - abs(int(x)), 2)
        self.decimal = int(decimal*10)*10
        self.desperdicio = int(decimal*100) - int(decimal*10)*10

    def mostrar(self):
        print "liquido_pagable:", self.liquido_pagable
        print "entero:", self.entero
        print "unidad:", self.unidad
        print "decimal:", self.decimal
        print "desperdicio", self.desperdicio

    def getBilletes(self):
        billetes = {"10": 0, "20": 0, "50": 0, "100": 0, "200": 0}
        valores = [0, 0, 0, 0, 0]
        x = self.entero
        if x >= 200:
            num = x/200
            x = x % 200
            billetes["200"] = num
            valores[4] = num
        if x >= 100:
            num = x/100
            x = x % 100
            billetes["100"] = num
            valores[3] = num
        if x >= 50:
            num = x/50
            x = x % 50
            billetes["50"] = num
            valores[2] = num
        if x >= 20:
            num = x/20
            x = x % 20
            billetes["20"] = num
            valores[1] = num
        if x >= 10:
            num = x/10
            x = x % 10
            billetes["10"] = num
            valores[0] = num
        return valores

    def getMonedas(self):
        monedas = {"1": 0, "2": 0, "5": 0}
        valores = [0, 0, 0]
        x = self.unidad
        if x >= 5:
            num = x/5
            x = x % 5
            monedas["5"] = num
            valores[2] = num
        if x >= 2:
            num = x/2
            x = x % 2
            monedas["2"] = num
            valores[1] = num
        if x >= 1:
            num = x/1
            x = x % 1
            monedas["1"] = num
            valores[0] = num
        return valores

    def getCentavos(self):
        centavos = {"10": 0, "20": 0, "50": 0}
        valores = [0, 0, 0]
        x = self.decimal
        if x >= 50:
            num = x/50
            x = x % 50
            centavos["50"] = num
            valores[2] = num
        if x >= 20:
            num = x/20
            x = x % 20
            centavos["20"] = num
            valores[1] = num
        if x >= 10:
            num = x/10
            x = x % 10
            centavos["10"] = num
            valores[0] = num
        return valores

    def getCabezera(self):
        encabezado = ["Nombre", "Liquido Pagable"]
        encabezado += ["Billetes:", 10, 20, 50, 100, 200]
        encabezado += ["Monedas:", 1, 2, 5]
        encabezado += ["Centavos:", 10, 20, 50]
        encabezado += ["Desperdicio:", 0]
        return encabezado

    def getDatos(self):
        datos = [self.nombre, self.liquido_pagable]
        datos += self.getBilletes()
        datos += self.getMonedas()
        datos += self.getCentavos()
        datos += [self.desperdicio]
        return datos
# conversor = Conversor("franz", 1597.90)
