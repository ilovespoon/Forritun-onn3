# Andri Snær Didriksen Ásmundsson
# 10.11.2017

from math import*
import random

#-----------------------------Liður 1 class------------------------------
class Trapisa:   
    def __init__(self,a=0,b=0,c=0,d=0):
        if a>=0 or b>=0 or c>=0 or d>=0:
            self.a=a
            self.b=b
            self.c=c
            self.d=d
        else:
            print("Villa...")
     
    def ummaltrapisu(self):
        ummal=self.a+self.b+self.c+self.d
        return ummal

    def flatarmaltrapisu(self):
        s=(self.a+self.b+self.c+self.d)/2
        reikn=((self.a+self.c)/(self.a-self.c))*(sqrt((s-self.c)*(s-self.a)*(s-self.c-self.b)*(s-self.c-self.d)))
        return reikn
    def flatarmaltrapisu2(self):
        H=sqrt(self.d**2+(self.a-self.c)**2)
        reikn2=H*((self.a+self.b)/2)
        return reikn2
    def trapisujafnarma(self):
        if self.d == self.b:
            return True
        else:
            return False
    def lestumig(self):
        return Trapisa.__doc__
#-----------------------------Liður 2 class------------------------------
class Frog:
    def __init__(self, sex, num):
        self.sex = sex
        self.num = num
    def printInfo(self):
        print("Þetta er froskur númer:", self.num,"og kyn er",self.sex)
        num=2
        dagar=0
        listikarl=[]
        listikona=[]
        froskur=Frog("Karl",1)
        listikarl.append(froskur)
        fro=Frog("Kerling",2)
        fjoldi = 2
        listikona.append(fro)
        fjoldi = 0
#-----------------------------Liður 3 class------------------------------
class bill:
    def __init__(self, tegund, argerd,hradi,bensin,eidsla):
        self.tegund = tegund
        self.argerd = argerd
        self.hradi = hradi
        self.bensin = bensin
        self.eidsla = eidsla
        
#------------------------------------------------------------------------
val = " "
while val != 5:
    print("\n------------------Verkefni 5----------------------")
    print("Liður 1 = Liður 1")
    print("Liður 2 = Liður 2")
    print("Liður 3 = Liður 3")
    print("Liður 4 = Hætta")
    print("--------------------------------------------------")
    val = int(input("Sláðu inn tölu til þess að velja lið: "))


    if val == 1:
        print("Velkominn")
        print("Liður 1")
        print("Trapisa eða hálfsmíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða.")
        m=0
        while m==0:
            
            val2=int(input("Sláðu inn tölu liðs 1-5... : "))
            a=int(input("Sláðu inn tölu "))
            b=int(input("Sláðu inn tölu "))
            c=int(input("Sláðu inn tölu "))
            d=int(input("Sláðu inn tölu "))
            trap1=Trapisa(a,b,c,d)
            if val2 == 1:
                print("Liður 1 Vol.2")
                print(trap1.ummaltrapisu())
            if val2 == 2:
                print("Liður 2 Vol.2")
                print(trap1.flatarmaltrapisu())
            if val2 == 3:
                print("Liður 3 Vol.2")
                print(trap1.flatarmaltrapisu2())
            if val2 == 4:
                print("Liður 4 Vol.2")
                print(trap1.trapisujafnarma())
            if val2==5:
                print("Liður 5 Vol.2")
                trap1=Trapisa()
                print(trap1.lestumig())

    if val == 2:
        print("Velkominn")
        print("Liður 2")
        num=2
        dagar=0
        listikarl=[]
        listikona=[]
        froskur=Frog("Karl",1)
        listikarl.append(froskur)
        fro=Frog("Kerling",2)
        fjoldi = 2
        listikona.append(fro)
        fjoldi = 0
        while fjoldi <10:
            if len(listikarl) <= len(listikona):
                for froskur in listikarl:
                    val = random.randint(0,1)
                    num +=1
                    fjoldi+=1
                    if val == 0:
                        nyrfroskur = Frog("Kerling",num)
                        listikona.append(nyrfroskur)
                    else:
                        nyrfroskur = Frog("Karl", num)
                        listikarl.append(nyrfroskur)
                    dagar=dagar+2
            else:
                pass
            for froskur in listikarl:
                froskur.printInfo()
            for froskur in listikona:
                froskur.printInfo()

    
        
