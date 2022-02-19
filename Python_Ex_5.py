import string
with open ("SAMPLE.txt") as data:
    datas = data.read()
    datas = datas.lower()  #Μετατροπή των κεφαλαίων σε μικρά γράμματα
    datas = datas.translate(str.maketrans('', '', string.punctuation))  #Αφαίρεση των σημείων στίξης
    datas = datas.translate(str.maketrans('', '', string.digits))  #Αφαίρεση των αριθμών
    datas = " ".join(datas.split())  #Διαμόρφωση του κειμένου ΜΟΝΟ με μικρά γράμματα και κενά (spaces)
    datas = datas.split(" ") # Διάσπαση του κειμένου σύμφωνα με το κενό
    containerWORDS = []    #Απάντηση του i) ερωτήματος
    containerTIMES = []
    for i in datas:
        if i in containerWORDS:
            posit = containerWORDS.index(i) #Συγκέντρωση των φορών εμφάνισης κάθε λεξής
            containerTIMES[posit] += 1
        else:
            containerWORDS.append(i)
            containerTIMES.append(1)
    for i in range (10):  #Εξαγωγή των δημοφιλέστερων λέξεων
        position = containerTIMES.index(max(containerTIMES)) #Αν κάποιες δημοφιλέστερες λέξεις εμφανίζονται ίδιο αριθμό φορών
                                                             #τότε πρώτες επιλέγονται αυτές που είναι αριστερότερα στη λίστα containerWORDS
        print("Η ", i+1, "η συνιθέστερη ΛΕΞΗ είναι η \"", containerWORDS.pop(position), "\"")
        containerTIMES.pop(position)
    
    def startletters(num): #Υπολογιστής συνηθέστερης αρχικής 2αδας ή 3αδας
     containerLETTERS = []
     containerTIMES = []
     for i in datas:         #Συγκέντρωση των φορών εμφάνισης των num πρώτων αρχικών γραμμάτων   
       if len(i[0:num]) == num: #Συγράτηση των αρχικών γραμμάτων ΜΟΝΟ από λέξεις με μήκος τουλάχιστον num
         if i[0:num] in containerLETTERS:
            posit = containerLETTERS.index(i[0:num])
            containerTIMES[posit] += 1
         else:
            containerLETTERS.append(i[0:num])
            containerTIMES.append(1)
     for i in range (3):   #Εξαγωγή των συνιθέστερων αρχικών συνδυασμών γραμμάτων
        position = containerTIMES.index(max(containerTIMES))
        print("Η ", i+1, "η", num,"αδα αρχικών ΓΡΑΜΜΑΤΩΝ είναι η \"", containerLETTERS.pop(position), "\"")
        containerTIMES.pop(position)
    print("-------------") #Γραμμές για την καλύτερη εμφάνιση των αποτελεσμάτων
    startletters(2)  #Απάντηση  ii) ερωτήματος
    print("-------------")
    startletters(3)  #Απάντηση iii) ερωτήματος
