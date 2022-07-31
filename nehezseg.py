import pyconio

def nehezseg():
    print("E. easy\t M. medium\t H. hard")
    print("Válasszon nehézségi fokozatot:")
    valasztottnehezseg = pyconio.getch()
    nehezseglista = []
    if (valasztottnehezseg == 69 or valasztottnehezseg == 101):
        nehezseglista.append(1)
        nehezseglista.append(2)
        nehezseglista.append(3)
        nehezseglista.append(4)

    elif (valasztottnehezseg == 77 or valasztottnehezseg == 109):
        nehezseglista.append(5)
        nehezseglista.append(6)
        nehezseglista.append(7)

    elif (valasztottnehezseg == 72 or valasztottnehezseg == 104):
        nehezseglista.append(8)
        nehezseglista.append(9)
        nehezseglista.append(10)
    return nehezseglista