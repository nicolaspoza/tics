def comision():    #Funcion que permite seleccionar AFP
    print("1)Habitat")
    print("2)Capital")
    print("3)Cuprum")
    print("4)Modelo")
    print("5)Planvital")
    print("6)Provida")
    op = input("seleccione su afp : ")
    if op is "1":
        Cafp = 1.27
    if op is "2":
        Cafp = 1.44
    if op is "3":
        Cafp = 1.44
    if op is "4":
        Cafp = 0.77
    if op is "5":
        Cafp = 1.16
    if op is "6":
        Cafp = 1.45
    return Cafp
F = 25.64 + Cafp #F = sumatoria de descuentos + comision por AFP
vutm = 47729.00
def Utm(p): #Funcion para convertir de pesos a UTM
    sueldo = float(p/vutm)
    return sueldo
def pesos(SL):#Funcion para convertir de UTM a pesos
    vpesos = SL*vutm
    print(vpesos)
    return vpesos
def CalcuL(sueldo):#Funcion para calcular de sueldo bruto a liquido
    SI = sueldo*(1-(F/100)) #recibe un sueldo bruto en UTM
    if (SI <= 13.554):
        SL = SI
        pesos(SL)
    if (SI >= 13.554023397 and SI <= 50.200088):#Tramos entre los que
        SL = SI*(1-(4.52/100))                 #esta un sueldo
        pesos(SL)
    if (SI >=  50.20008821 and SI <= 70.2801232):
        SL = SI*(1-(7.09/100))
        pesos(SL)
    if (SI >= 70.2802341 and SI <= 90.36015839):
        SL = SI*(1-(10.62/100))
        pesos(SL)
    if (SI >= 90.3601586 and SI <=  120.4802112):
        SL = SI*(1-(15.57/100))
        pesos(SL)
    if (SI >= 120.4802114):
        SL = SI*(1-(16.01/100))
        pesos(SL)
def sueldoBruto():
    SL = float(input("introduzca su sueldo liquido: "))

    if(SL >= 0 and SL <=  29.57788766): #Se calculan los rangos de sueldo líquido cada dos rangos ya que se tiene
        SI = SL + 0.54216514             # un margen de error. Esto se arregla con los if que se tienen dentro de
        if(SI > 0 and SI <= 13.554): # los intervalos antes mencionados.
            SI = SL - 0.54216514
            SB = (SI * 100)
            SB = SB / (100 - F)
            print (SB)
        elif(SI > 13.554 and SI <= 30.12005280):
            SB = (SI * 100)
            SB = SB / (100 - F)
            print(SB)

    elif(SL >= 13.01185862 and SL <= 29.57788766):
        SI = SL + 1.74696725
        if(SI > 30.12005280 and SI <= 50.20008800):
            SB = (SI * 100)
            SB = SB / (100 - F)
            print(SB)

    elif(SL >= 28.37308555 and SL <= 65.77215110):
        SI = SL + 4.50797209
        if(SI 50.20008800 >  and SI <= 70.28012320):
            SB = (SI * 100)
            SB = SB / (100 - F)
            print(SB)

    elif(SL >= 45.69211590 and SL <= 791.75578789):
        SI = SL + 11.18458380
        if(SI >  70.28012320 and SI <= 90.36015839):
            SB = (SI * 100)
            SB = SB / (100 - F)
            print(SB)

    elif(SL >= 59.09553940 and SL <= 102.60897987):
        SI = SL + 17.87123133
        if(SI > 90.36015839 and SI <= 120.48021119):
            SB = (SI * 100)
            SB = SB / (100 - F)
            print(SB)

    elif(SL > 120.48021119):
        SI = SL + 23.41331266
        if(SI >= 97.06689853):
            SB = (SI * 100)
            SB = SB / (100 - F)
            print(SB)

if __name__ == "__main__":
    sueldoB = float(input("ingrese sueldo bruto : "))
    comision()
    sueldo = sueldoBruto()
    p = Utm(sueldoB)
    CalcuL(p)
