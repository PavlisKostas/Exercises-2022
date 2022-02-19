with open ("SAMPLE.txt") as data:
    datas = data.read()
    sums = ""
    for k in datas:
        local = bin(ord(k))[2:] #Μετατροπή σε δυαδικό και συλλογή των 2 πρώτων και 2 τελευταίων bit κάθε στοιχείου
        local = local.zfill(7)
        newnum = local[:2] + local[5:]
        sums += newnum   #Δημιουργία ενός ενιαίου στοιχείου που περιέχει τα αποτελέσματα της παραπάνω επεξεργασίας
    n = 16  #Διαχωρισμός του "sums" σε αυτόνομες 16αδες bit 
    collector = [sums[i:i+n] for i in range(0, len(sums), n)] #Αν δεν υπάρχει ολοκληρωμένη τελική 16αδα bit κρατάει
                                                              #και υπολογίζει τον αριθμό ΜΟΝΟ με τα διαθέσιμα bit
    zigoi = 0
    pol3 = 0
    pol5 = 0
    pol7 = 0
    rings = 0
    for k in collector:
        selection = int(k, 2)  #Μετατροπή κάθες 16άδας bit σε δεκαδικό αριθμό και επεξεργασία αυτών των αριθμών
        if selection%2 == 0:
            zigoi += 1
        if selection%3 == 0:
            pol3 += 1
        if selection%5 == 0:
            pol5 += 1
        if selection%7 == 0:
            pol7 += 1
        rings += 1
    POSzigoi = zigoi/rings*100
    POS3pol = pol3/rings*100
    POS5pol = pol5/rings*100
    POS7pol = pol7/rings*100
    print("Είναι Ζυγοί το "+str(int(POSzigoi))+"%")  #Εμφανίζεται μόνο το ακέραιο μέρος του ποσοστού με το int
    print("Είναι Πολλαπλάσιο του 3 το "+str(int(POS3pol))+"%")
    print("Είναι Πολλαπλάσιο του 5 το "+str(int(POS5pol))+"%")
    print("Είναι Πολλαπλάσιο του 7 το "+str(int(POS7pol))+"%")
