# sueldoB = float(input("ingrese sueldo bruto : "))
F = 25.64 + Cafp
vutm = 47729.00
def comision():
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

def Utm(p):
    sueldo = float(p/vutm)
    return sueldo
def pesos(L):
    vpesos = L*vutm
    print(vpesos)
    return vpesos
# sueldo = Utm(sueldoB)
def CalcuL(sueldo):
    # sueldo = Utm(sueldoB)
    # sueldo = Utm(sueldoB)
    # if sueldoB <= 646920.00:
    sI = sueldo*(1-(F/100))
    if sI <= 13.554:
        # si = sueldo*(1-F)
        L = sI
        pesos(L)
        # print(L)
    # if sueldoB >= 646920.01 and sueldoB <= 2396000.00:
    if sI >= 13.554023397 and sI <= 50.200088:
        # si = sueldo*(1-F)
        L = sI*(1-(4.52/100))
        pesos(L)
        # print(L)
    # if sueldoB >=  2396000.01 and sueldoB <= 3354400.00:
    if sI >=  50.20008821 and sI <= 70.2801232:
        # si = sueldo*(1-F)
        L = sI*(1-(7.09/100))
        pesos(L)
        # print(L)
    # if sueldoB >= 3354400.01 and sueldoB <= 4312800.00:
    if sI >= 70.2802341 and sI <= 90.36015839:
        # si = sueldo*(1-F)
        L = sI*(1-(10.62/100))
        pesos(L)
        # print(L)
    # if sueldoB >= 4312800.01 and sueldoB <=  5750400.00:
    if sI >= 90.3601586 and sI <=  120.4802112:
        # si = sueldo*(1-F)
        L = sI*(1-(15.57/100))
        pesos(L)
        # print(L)
    # if sueldoB >= 5750400.01:
    if sI >= 120.4802114:
        # si = sueldo*(1-F)
        L = sI*(1-(16.01/100))
        pesos(L)
        # print(L)
def pesos(L):
    vpesos = L*vutm
    print(vpesos)

if __name__ == "__main__":
    sueldoB = float(input("ingrese sueldo bruto : "))
    comision()
    p = Utm(sueldoB)
    CalcuL(p)
