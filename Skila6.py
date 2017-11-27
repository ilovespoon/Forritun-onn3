# Andri Snær Ásmundsson
# 24.12.2017


from math import *


# ---------------------------------------------Dæmi1-------------------------------------------------#
class rummal:
    def upplysingar(self, x = ""):
        return "Ég er klasi sem reiknar út rúmmál hluta {}".format(x)


class rummalkassi(rummal):
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h

    def kassi(self):
        r = self.l * self.h * self.b
        return "þetta er rúmmál kassans" + " " + str(r)

    def upplysingar(self):
        return super().upplysingar('og þetta er kassi')


class pyramidi_rummal(rummal):
    def __init__(self, l, h, b):
        self.l = l
        self.h = h
        self.b = b

    def Pyramídi(self):
        r = self.l * self.h * self.b / 3
        return "þetta er rúmmál pyramídans" + " " + str(r)

    def upplysingar(self):
        return super().upplysingar('og þetta er kassi')


class kularummal(rummal):
    def __init__(self, r):
        self.r = r
        self.v = self.vol()

    def vol(self):
        return (4 / 3 * pi * (self.r))

    def upplysingar(self):
        return super().upplysingar('og þetta er kassi')


# ---------------------------------------------Dæmi2-------------------------------------------------#
class nemi:
    def __init__(self, kt, firstname, lastname, kyn, address, phone, email, braut):
        self.kt = kt
        self.firstname = firstname
        self.lastname = lastname
        self.kyn = kyn
        self.address = address
        self.phone = phone
        self.email = email
        self.braut = braut

    def upplysingar(self):
        return " kennitala: " + self.kt + " fyrsta nafn:" + self.firstname + " síðasta nafn:" + self.lastname + " kyn: " + self.kyn + " address: " + self.address + " sími: " + self.phone


class grunnskolanemi(nemi):
    def __init__(self, kt, firstname, lastname, kyn, address, phone, forradamadur, nafnSkola):
        nemi.__init__(self, kt, firstname, lastname, kyn, address, phone, forradamadur, nafnSkola)
        self.forradamadur = forradamadur
        self.nafnSkola = nafnSkola

    def upplysingar(self):
        return "forráðamaður: " + self.forradamadur + " nafn skóla: " + self.nafnSkola + super().upplysingar()


class framhaldsskolinemi(nemi):
    def __init__(self, kt, firstname, lastname, kyn, address, phone, email, braut):
        nemi.__init__(self, kt, firstname, lastname, kyn, address, phone, email, braut)
        self.braut = braut

    def upplysingar(self):
        return "braut: " + self.braut + super().upplysingar()


class haskolanemi(nemi):
    def __init__(self, kt, firstname, lastname, kyn, address, phone, email, grada):
        nemi.__init__(self, kt, firstname, lastname, kyn, address, phone, email, grada)
        self.grada = grada

    def upplysingar(self):
        return "gáða: " + self.grada + super().upplysingar()


# ---------------------------------------------------------------------------------------------------#



svar = " "
while svar == " ":
    print("1.liður")
    print("2.liður")
    print("3. Hætta")
    val = int(input("Veldu lið: "))

    if val == 1:
        daemi1 = " "
        while daemi1 == " ":
            print("___________________________________________________________")
            print("1.rúmmál kassa")
            print("2.rúmmál pýramída")
            print("3.rúmmál kúlu")
            print("4.hætta")
            vall = int(input("Veldu dæmi: "))
            if vall == 1:
                kassi = rummalkassi(2, 7, 5)
                print(kassi.upplysingar())
                print(kassi.kassi())

            if vall == 2:
                print()
                pyramidi = pyramidi_rummal(6, 7, 8)
                print(pyramidi.upplysingar())
                print(pyramidi.Pyramídi())

            if vall == 3:
                kula = kularummal(2)
                print(kula.upplysingar())
                print("rúmmál þessara kúlu er = ", round(kula.vol(), 2))
            if vall == 4:
                print("---------------------------------------------------------------")
                break

    if val == 2:
        fram = framhaldsskolinemi("1804003030", "Andri", "Ásmundsson", "KK", "Reykjavík", "8993594",
                                  "Andrigaur1@gmail.com", "tölvubraut")
        print(fram.upplysingar())
        grunn = grunnskolanemi("0907003456", "Jens", "Ásgrímsson", "KK", "Reykjavik", "iEatAss@gmail.com", "Mamma",
                               "Rimaskóli")
        print(grunn.upplysingar())
        haskola = haskolanemi("0604004652", "Anni", "Didriksen", "KVK", "Reykjavík", "7845693", "Photographsannie@gmail.com",
                              "BA")
        print(haskola.upplysingar())
        print("_________________________________________________________________________________________")
    # ---------------------------------------------Val4-------------------------------------------------#
    if val == 3:
        print("Takk fyrir að nota mig...")
        break