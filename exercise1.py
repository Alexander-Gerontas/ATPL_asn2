# Γέροντας Αλέξανδρος - 321/2015029
def main():

    # Άνοιγμα αρχείου.
    file = open("file.txt", 'r')
    fileLines = file.read().lower()

    # Καταχώρηση αριθμών, φωνηέντων και συμφώνων σε συμβολοσειρές.
    integers = "123456789"
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    # Μέτρημα του πλήθους των χαρακτήρων κάθε συμβολοσειράς που περιέχει το αρχειο. 
    integerSum = sum(fileLines.count(i) for i in integers)
    vowelSum = sum(fileLines.count(i) for i in vowels)
    consonantSum = sum(fileLines.count(i) for i in consonants)

    # Tύπωση αποτελεσμάτων.
    print("Number of integers in the string: ", integerSum)
    print("Number of vowels in the string: ", vowelSum)
    print("Number of consonants in the string: ", consonantSum)
    
    # Κλείσιμο αρχείου.
    file.close()

main()
