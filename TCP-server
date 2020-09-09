import socket
import threading
from _datetime import datetime
import random
import math
import re


def ipaddress( adresa):
    try:
        return "IP Adresa e klientit eshte: " +str(addr[0])
    except:
        return "Adresa nuk mund te gjenerohet"
def port(adresa):
    try:
        return "Klienti eshte duke perdorur portin: " + str(addr[1])
    except:
        return "Porti nuk mund te gjenerohet"

def count(text):
    text=text.lower()
    v=0
    c=0
    if(text!=""):
        for i in text:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
             or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
             v=v+1
            else:
             c=c+1
        return "Numri i zanoreve eshte "  + str(v)  + " kurse i bashketingelloreve "  + str(c)
    else:
        return "Nuk keni dhene tekst"

def reverse( text):
    if(text==""):
        return "Nuk e keni dhene tekstin qe deshironi te ktheni mbrapsht"
    else:
        x=text[::-1]
        return "teksti i kthyer mbrapsht eshte" + " " + str(x)

def palindrome(text):
    
    text=text.lower()
    reversed_text=text[::-1]
    if(text!=""):
        if(text==reversed_text):
            return str(text) + " " + "eshte palindrome"
        else:
            return str(text) + " " + "nuk eshte palindrome"
    else:
        return "Sigurohuni qe keni dhene tekstin qe doni ta provoni"


def time():
    try:
        koha=datetime.now()
        return koha.strftime("%H:%M:%S-%D")
    except ConnectionAbortedError:
        print("Koha nuk mund te gjenerohet")

def GCF(data):
    data=data.split(" ")
    try:
       num1=int(data[1])
       num2=int(data[2])

       if num1>num2:
          num1, num2 = num2, num1
       for x in range (num1, 0, -1):
           if num1 % x==0 and num2 % x ==0:
              return x
    except:
        return "U paraqit nje gabim, sigurohuni qe keni dhene dy numra"
        


def game():
    a = random.sample(range(1,35), 5)
    a.sort()
    return (str(a))
  


def convert(data):
    data=data.lower()
    data=data.split(" ")
    try:
       if data[1] == "feettocm":
           return round((float(data[2])*30.48), 2)
       elif data[1] == "cmtofeet":
           return round((float(data[2])/30.48), 2)
       elif data[1] == "kmtomiles":
           return round((float(data[2])/1.609), 2)
       elif data[1] == "milestokm":
           return round((float(data[2])*1.609), 2)
       else:
           return "Dicka shkoi gabim! A jeni te sigurt se keni zgjedhur opsione"
           +" (feettocm, cmtofeet, kmtomiles ose milestokm)"
    except:
        return "Ka ndodhur nje gabim"


    
def sum_divisor(data):
    data=data.split(" ")
    divisors = [1]
    try:
         number=int(data[1])
         for i in range(2, number):
             if (number % i)==0:
                divisors.append(i)
         return sum(divisors)
    except:
        return "Ka ndodhur nje gabim. Sigurohuni qe keni dhene numer!"

def swap(data):
    data=data.split(" ")
    try:
        fjala1= data[1]
        fjala2=data[2]
        temp=data[1]
        data[1]=data[2]
        data[2]=temp
        return "Vlera e pare eshte" + " " + str(data[1]) + " " + "e dyta " + str(data[2])
    except:
        return "Dicka nuk shkoi sic duhet"



      
def listenToConns(conns, addr):
    print("Serveri u konektua me klientin " + addr[0] + " ne portin" + " " + str(addr[1]))
    size=128
    while True:
        try:
            choice = conns.recv(size)
            choice = choice.decode("utf-8").lower()
            print("Kerkesa" + " " + addr[0] +" " + "e klientit eshte: " + choice )
            if (choice.startswith("ipaddress")):
                a=ipaddress(addr[0])
            elif choice.startswith("port"):
                a=port(addr[1])
            elif choice.startswith("time"):
                a=time()
            elif choice.startswith("convert"): 
                a=convert(choice)
            elif choice.startswith("game"):
                a=game()
            elif choice.startswith("count"):
                a=count(choice[5:])
            elif choice.startswith("reverse"):
                a=reverse(choice[7:])  
            elif choice.startswith("gcf"):
                a=GCF(choice)
            elif choice.startswith("palindrome"):
                a=palindrome(choice[11:])
            
            elif choice.startswith("sum_divisor"):
                a=sum_divisor(choice)
            
            elif choice.startswith("swap"):
                a=swap(choice)
                    
            else:
                a="Keni zgjedhur metode te gabuar! Ju lutem provoni perseri!"
            a = str(a)
            conns.send(str.encode(a))
            print("Serveri i dergoi klientit me adresen" + " " + addr[0] + " " + "kete pergjigje:"+ " " + a)
        except:
            conns.close()
            return False




serverName = ''
serverPort = 13000
serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverS.bind((serverName,serverPort))

serverS.listen(5)
print('Serveri eshte gati te pranoj kerkesat..')

while True:
    conns, addr = serverS.accept()
    print("Serveri u konektua me klietin  " + addr[0] + "  ne portin  " + str(addr[1]) + "\n")
    threading.Thread(target=listenToConns, args=(conns, addr)).start()
