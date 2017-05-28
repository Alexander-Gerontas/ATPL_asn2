# Γέροντας Αλέξανδρος - 321/2015029
from random import shuffle

class Cryptography:

    # Αρχικοποίηση τιμών και κλήση της μεθόδου dictionaryShuffle().
    def __init__(self):
        self.Dictionary = {}
        self.sentence = ''
        self.dictionaryShuffle()

    # Δημιουργία κρυπτογραφημένου αλφάβητου.
    def dictionaryShuffle(self):

        # Δημιουργία λεξικού του λατινικού αλφαβήτου.
        for i in range(ord('a'), ord('z')):
            self.Dictionary[chr(i)] = chr(i)

        # Δημιουργία λίστας με ανακατεμένα λατινικά γράμματα με χρήση των τιμών του λεξικού.
        dictValues = list(self.Dictionary.values())
        shuffle(dictValues)

        # Δημιουργία κρυπτογραφημένου λεξικού με χρήση των κλειδιών του λεξικού
        # και της κρυπτογραφημένης λίστας.
        self.Dictionary = dict(zip(self.Dictionary.keys(), dictValues))

    # Εισαγωγή πρότασης από τον χρήστη.
    def setSentence(self, sentence):
        self.sentence = sentence

    # Τήπωση αρχικής πρότασης
    def printSentence(self):
        print(self.sentence)

    # Τήπωση κρυπτογραφημένου αλφάβητου.
    def printDictionary(self):
        print(str(self.Dictionary).replace("'", ""), '\n')

    # Τήπωση κρυπτογραφημένης πρότασης.
    def cryptSentence(self):

        if self.sentence is '':
            print("Δεν δόθηκε πρόταση\n")
            return

        text = ''

        # Κρυπτογράφηση χαρακτήρων πρότασης με την χρήση του λεξικού και εκχώρηση τους σε νέα συμβολοσειρά.
        # Χαρακτήρες όπως το κενό και τα σημεία στίξης καταχωρούνται όπως είναι.
        for i in range(0, len(self.sentence)):
            if ord(self.sentence[i]) in range(ord('a'), ord('z')):
                text += self.Dictionary[self.sentence[i]]
            else: text += self.sentence[i]

        print(text)

def main():
    crypt = Cryptography()

    while True:
        print('1.Εισαγωγή πρότασης')
        print('2.Τήπωση αρχικής πρότασης')
        print('3.Τήπωση κρυπτογραφημένης πρότασης')
        print('4.Τήπωση κρυπτογραφημένου αλφάβητου')
        print('5.Δημιουργία νέου κρυπτογραφημένου αλφαβήτου')
        print("0.Έξοδος")
        y = input('>>')

        if int(y) is 1: crypt.setSentence(input('Πληκτρολόγησε την πρόταση: '))
        if int(y) is 2: crypt.printSentence()
        elif int(y) is 3: crypt.cryptSentence()
        elif int(y) is 4: crypt.printDictionary()
        elif int(y) is 5: crypt.dictionaryShuffle()
        elif int(y) is 0: exit()

main()