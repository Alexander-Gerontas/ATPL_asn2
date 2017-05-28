# Γέροντας Αλέξανδρος - 321/2015029
class Dictionary:

    # Ο Δομητής αρχικοπoιεί το λεξικό, ανοίγει το αρχείο και καλεί την συνάρτηση loadWords().
    def __init__(self):
        self.Dict = {}
        self.file = open('dictionary.txt', 'a+')
        self.file.seek(0,0)
        self.loadWords()

    # Διάβασμα αρχείου και εκχώρηση λέξεων στο λεξικό.
    def loadWords(self):
        while True:
            line = self.file.readline()
            if line == '' or line == '\n' : break
            self.Dict[line.split(',')[0]] = line.split(',')[1]

    # Εισαγωγή λέξης από τον χρήστη.
    def wordInput(self):
        word = input("Δώσε μια αγγλική λέξη και την ελληνική μετάφραση : ")

        # Καταχώρηση της λέξης στο αρχείο και στο λεξικό αν δεν είναι ήδη καταχωρημένη.
        if word.split(',')[0] not in self.Dict:
            self.file.write(word+ '\n')
            self.Dict[word.split(',')[0]] = word.split(',')[1]
        else: print('Η λέξη υπάρχει ήδη στο λεξικό')

    # Αναζήτηση μετάφρασης λέξης αν αυτή υπάρχει στο λεξικό.
    def getWordTranslation(self):
        word = input('Δώσε μια αγγλική λέξη: ')
        if word in self.Dict: print ("H λέξη", word, "σημαίνει", self.Dict[word])
        else: print('Η λέξη δεν υπάρχει στο λεξικό\n')

    # Ο αποδομητής κλείνει το αρχείο.
    def __del__(self):
        self.file.close()

def main():

    dictionary = Dictionary()

    while True:
        print("1.Εισαγωγή νέας λέξης.")
        print("2.Αναζήτηση μετάφρασης λέξης.")
        x = input("0.Έξοδος και αποθήκευση αλλαγών. \n>> ")

        if int(x) == 1: dictionary.wordInput()
        if int(x) == 2: dictionary.getWordTranslation()
        if int(x) == 0: break

main()