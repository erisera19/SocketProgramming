import socket

print("Nese deshironi te ndryshoni emrin e serverit dhe numrin e portit shtypni PO (Shtypni komandat tjera per te vazhduar normalisht): ")
pergjigja=input().upper()
try:
    if(pergjigja=="PO"):
        print("Jepeni emrin e deshiruar: ")
        serverName=input().lower()
        print("Jepnei numrin e portit: ")
        port=input()
        serverPort=int(port)
    else:
        serverName='localhost'
        serverPort=13000
except:
    print("Porti i dhene nuk eshte valid")

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socc=(serverName, serverPort)

print("Zgjidheni operacionin qe deshironi te performohet, beni kujdes ne drejtshkrimin e kerkeses" + 
"\nOperacionet jane: \n1: IPADDRESS \n2: PORT \n3: COUNT \n4: REVERSE{hapsire}tekst \n5: PALINDROME{hapesire}tekst"+ 
"\n6: TIME \n7: GAME \n8: GCF{hapesire}Numer1{hapesire}Numer2 \n9:CONVERT{hapesire}Opsioni{hapesire}numer \n10:sum_divisor{hapesire}numer \n11: swap{hapsire}numer1{hapesire}numer2 ")

while True:

    opsioni=input("Mundeni te vazhdoni me kerkesen tuaj ose te shtypni END per te perfunduar.")
    opsioni=opsioni.upper()
    if(opsioni == "END"):
        s.close()
        break
    else:
        s.sendto(str.encode(opsioni),socc)
        r=s.recvfrom(128)

        pergjigja = r[0].decode("utf-8")
        print(pergjigja)
   



