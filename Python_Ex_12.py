from urllib.request import Request, urlopen
import json

def grabber(item, selector):  #Συλλέγει το round ή το randomness κατά την εκτέλεση του προγράμματος
  req = Request('https://drand.cloudflare.com/public/'+item, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
  data = urlopen(req).read()
  data = data.decode()
  data = json.loads(data)
  collection = data[selector]
  return collection
receiver = grabber('latest', 'round') #Εντοπισμός του τελευταίου γύρου
first = receiver - 99 #Υπολογισμός εύρους τιμών γύρων για τη συλλογή του randomness
final = receiver + 1
total = ""
#Συλλογή του "randomness" από την παλαιότερη στην πιο πρόσφατη τιμή (latest), δηλαδή από το first στο final
for i in range(first, final):
    giros = str(i)
    receiver = grabber(giros, 'randomness')
    receiver = bin(int(receiver, 16)) #Μετατροπή από δεκαεξαδικό σε δεκαδικό και μετά σε δυαδικό
    receiver = receiver[2:] #Απόρριψη του συστημικού "0b" από τα δυαδικά ψηφία
    total += receiver #Αθροιστής όλων των δυαδικών ακολουθιών

def computer(changer): # "Υπολογιστής" συνεχόμεων ακολουθιών μηδενικών και άσων
 most = 0  #Το most αποθηκεύει τη μεγαλύτερη ακολουθία που κατέγραψε το m
 m = 0  #Το m είναι τοπικός μετρητής συνεχόμενων στοιχείων
 for j in total: 
    if j == changer:
        m += 1
    else:
        if most<m :
            most = m
        m = 0
 if most<m : 
    most = m
 return most

print("Μέγιστα Συνεχόμενα Μηδενικά (0): ", computer("0") ,"| Μέγιστοι Συνεχόμενοι Άσοι (1): ", computer("1"))
