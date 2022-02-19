import string
with open("SAMPLE.txt") as data:
    datas = data.read()
    datas = datas.translate(str.maketrans('', '', string.punctuation))  #Αφαίρεση των σημείων στίξης
    datas = datas.translate(str.maketrans('', '', string.digits))  #Αφαίρεση των αριθμών
    datas = " ".join(datas.split())  #Τελική Διαμόρφωση του κειμένου ΜΟΝΟ με μικρά γράμματα και κενά (spaces)
    datas = datas.split(" ") #Διάσπαση του κειμένου σύμφωνα με το κενό
                          #ΣΥΛΛΟΓΗ ΑΡΧΙΚΩΝ ΣΤΑΤΙΣΤΙΚΩΝ (ΠΡΙΝ ΤΗΝ ΕΠΕΞΕΡΓΑΣΙΑ)
    def pinakes():
     tableLEN = []   #Τα διαφορετικά μίκοι λέξεων που υπάρχουν
     tableNUM = []   #Οι φορές που επαναλαμβάνεται το κάθε μήκος
     for k in datas:
        if len(k) in tableLEN:
            tableNUM[tableLEN.index(len(k))] += 1
        else:
            tableLEN.append(len(k))
            tableNUM.append(1)
     return tableLEN, tableNUM

    tableLENTH, tableNUMBER = pinakes()
    
    superd = []     
    for k in datas:    #Εκχώρηση των μηκών των λέξεων στην λίστα "superd"
        superd.append(len(k))

    def remover(num): #Αφαιρεί λέξεις συγκεκριμένου ΜΗΚΟΥΣ ανάλογα με το όρισμα num
     p = superd.index(num)
     superd[p] = 0
     datas[p] = ""
     return p

    posi = -1
    for i in tableLENTH:
        posi += 1
        dif = 20 - i #Εύρεση του συμπληρώματος dif για δημιουργία αθροίσματος 20
        if dif in tableLENTH and i != 10:
            y = tableLENTH.index(dif)
            difNEW = tableNUMBER[posi] - tableNUMBER[y] #Το difNEW είναι η διαφορά του πλήθους των λέξεων με άθροισμα 20
            
            if difNEW > 0:
                for j in range(0, tableNUMBER[y]):
                    remover(i)      #Αφαίρεση ζευγών αριθμών με άθροισμα 20
                    remover(dif)
            elif difNEW == 0:
                for j in range(0, tableNUMBER[posi]):  #Αφαίρεση ζευγών αριθμών που έχουν το ίδιο πλήθος στοιχείων με άθροισμα 20
                    remover(i)
        elif i == 10:
              if tableNUMBER[posi] % 2 == 0:
                 for j in range(0, tableNUMBER[posi]):  #Αφαίρεση ζευγών αριθμών μήκους 10 με άθροισμα 20
                      remover(i)
              else:
                 for j in range(0, tableNUMBER[posi]-1):
                      remover(i)

    while("" in datas) :  #Η λίστα datas με τις λέξεις που απέμειναν, 'καθαρή' από τα "" στοιχεία του προγούμενο βρόγχου for
        datas.remove("") 

    tableLENTH, tableNUMBER = pinakes()
    for k in range(len(tableNUMBER)):  #Προβολή των αποτελεσμάτων σε φθήνουσα σειρά του πλήθους λέξεων του κάθε διαφορετικού μήκους (Προσωπική Επιλογή για καλύτερη εμφάνιση)
        position = tableNUMBER.index(max(tableNUMBER))
        print("Υπάρχουν", tableNUMBER.pop(position), "λέξεις των", tableLENTH.pop(position), "γραμμάτων.")
