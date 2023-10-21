import math
import random


class AffineCipher:
    def __init__(self):
        self.__numsDic__ = {}
        self.__charsDic__ = {}
        # This loop will create a dictionary to store the equivalent numeric values of the 26 English letters
        for i in range(65, 91):  # for capital letters
            self.__numsDic__[chr(i)] = i - 65
            # capital letters will have index from (i - 65) = 0 to 25

        for i in range(97, 123):  # for small letters
            self.__numsDic__[chr(i)] = i - 71
            # small letters index from 26 to 51

        # This loop will create a dictionary to store the equivalent English letters to the first 26 natural numbers
        for j in range(26):
            self.__charsDic__[j] = chr(j + 65)
        for j in range(26, 52):
            self.__charsDic__[j] = chr(j + 71)

    def encrypt(self, message, num1, num2):

        message = message.replace(" ", "")
        assert math.gcd(num1, 26) == 1, "The first number must be a coprime with 26"

        encryptedMsg = ""
        for index in range(len(message)):
            if message[index] in self.__numsDic__:
                # checks if characters of the message are found in the dictionary,
                # i.e. if it is one of the english letters, and if yes encrypts it, else it ignores it

                charNum = self.__numsDic__[message[index]]
                if charNum < 26:  # if it is capital
                    encryptedCharNum = ((num1 * charNum) + num2) % 26
                    encryptedMsg += self.__charsDic__[encryptedCharNum]

                else:  # if it is small letter
                    encryptedCharNum = (((
                                                 num1 * charNum) + num2) % 26) + 26  # we add 26 because small letters index began from 26
                    encryptedMsg += self.__charsDic__[encryptedCharNum]

            else:  # if the character is not in the dictionary we just add it to the encrypted message without chamging it
                encryptedMsg += message[index]
        print(f"encrypted message: {encryptedMsg}")

    def decrypt(self, message, num1, num2):
        assert math.gcd(num1, 26) == 1, "The first number must be a coprime with 26"

        inverse = pow(num1, -1, 26)

        decryptedMsg = ""
        for index in range(len(message)):
            if message[index] in self.__numsDic__:
                charNum = self.__numsDic__[message[
                    index]]  # if the character is in the dictionary which maps natural numbers to their equivalent english letters

                if charNum < 26:  # if capital
                    decryptedCharNum = (inverse * (
                            charNum - num2)) % 26  # the same process as encryption except we change the modulo
                    decryptedMsg += self.__charsDic__[decryptedCharNum]
                else:
                    decryptedCharNum = ((inverse * (charNum - num2)) % 26) + 26
                    decryptedMsg += self.__charsDic__[decryptedCharNum]
            else:
                decryptedMsg += message[index]

        print(f"decrypted message: {decryptedMsg}")


class TranspositionCipher:
    def encrypt(self, message, key):  # key = block length
        encryptedMsg = ""
        message = message.replace(" ", "")
        pointer = 0
        point = key
        permuteDic = {}
        for i in range(point):
            # we store each permutation in the permuteDic dictionary so that we can use it multiple times without
            # asking the user to input it everytime
            initial, final = (
                input(f"Enter the {i + 1}th permutation (separate between the initial\nand final by a "
                      f"whitespace), only numbers between 1 and {point} are allowed\nto exit write the "
                      f"same number twice: ").split(" "))
            initial = int(initial) - 1
            final = int(final) - 1
            if initial == final:  # i.e. exit
                for j in range(i, point):
                    permuteDic[i + 1] = f"{initial} {final}"
                break
            assert initial < point and final < point, "Invalid input"
            permuteDic[i + 1] = f"{initial} {final}"
        while key < len(message):
            block = message[pointer: key]
            myList = [None] * point
            for i in range(point):
                initial, final = permuteDic[i + 1].split(" ")
                initial = int(initial)
                final = int(final)
                myList[final] = block[initial]  # we make the initial element of block, the final element of the list
            block = ""
            for char in myList:
                block += char  # add the transposed elements from myList into block
            encryptedMsg += block + " "
            pointer = key
            key += point
        if pointer < len(message):  # checks if there is any omitted elements from the message and encrypts them
            block = message[pointer:]
            randomChars = []
            while len(block) < point:  # we add a random letter to make len(block) == point
                randomChar = chr(random.randint(67, 92))
                block += randomChar
                randomChars.append(randomChar)
            for i in range(point):
                initial, final = permuteDic[i + 1].split(" ")
                initial = int(initial)
                final = int(final)
                myList[final] = block[initial]
            block = ""
            for char in myList:
                if char not in randomChars:
                    block += char
            encryptedMsg += block

        print(f"encrypted message: {encryptedMsg}")

    def decrypt(self, message, key):
        # most of the decryption processes are the same as the encryption ones except some minor changes
        decryptedMsg = ""
        message = message.replace(" ", "")
        pointer = 0
        point = key
        permuteDic = {}
        for i in range(point):
            initial, final = (
                input(f"Enter the {i + 1}th permutation (separate between the initial\nand final by a "
                      f"whitespace), only numbers between 1 and {point} are allowed\nto exit write the "
                      f"same number twice: ").split(" "))
            initial = int(initial) - 1
            final = int(final) - 1
            if initial == final:
                for j in range(i, point):
                    permuteDic[i + 1] = f"{initial} {final}"
                break
            assert initial < point and final < point, "Invalid input"
            permuteDic[i + 1] = f"{initial} {final}"
        while key < len(message):
            block = message[pointer: key]
            myList = [None] * point
            for i in range(point):
                initial, final = permuteDic[i + 1].split(" ")
                initial = int(initial)
                final = int(final)
                myList[initial] = block[final]
            block = ""
            for char in myList:
                block += char
            decryptedMsg += block + " "
            pointer = key
            key += point
        if pointer < len(message):
            block = message[pointer:]
            randomChars = []
            while len(block) < point:
                randomChar = chr(random.randint(67, 92))
                block += randomChar
                randomChars.append(randomChar)
            for i in range(point):
                initial, final = permuteDic[i + 1].split(" ")
                initial = int(initial)
                final = int(final)
                myList[initial] = block[final]
            block = ""
            for char in myList:
                if char not in randomChars:
                    block += char
            decryptedMsg += block

        print(f"decrypted messasge: {decryptedMsg}")


class RSA:
    def __init__(self):
        # we first create a dictionary to map all characters to their equivalent numerical value
        self.__numsMap__ = {}
        for i in range(65, 91):  # add capital letters to the dictionary
            if i - 65 < 10:
                self.__numsMap__[chr(i)] = "0" + str(i - 65)
            else:
                self.__numsMap__[chr(i)] = str(i - 65)

        for i in range(97, 123):  # to add small letters
            self.__numsMap__[chr(i)] = str(i - 71)

        for i in range(33, 65):  # to add special characters
            self.__numsMap__[chr(i)] = str(i + 20)

        for i in range(123, 127):  # to add additional special characters
            self.__numsMap__[chr(i)] = str(i - 39)

        # we also create a dictionary to map numerical values into their equivalent characters
        self.charsMap = {}
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!'#$%&\"()*+,-./0123456789:;<=>?@{|}~"
        for i in range(len(chars)):
            i = str(i)
            if int(i) < 10:
                i = "0" + i
            self.charsMap[i] = chars[int(i)]

    def encrypt(self, message):

        print("Type default if you want an auto generated value")

        prm1 = input("enter first prime: ")
        if prm1.lower() == "default":
            prm1 = self.__generatePrime__(100, 1000)
        else:
            prm1 = int(prm1)

        prm2 = input("enter the second prime: ")
        if prm2.lower() == "default":
            prm2 = self.__generatePrime__(100, 1000)
        else:
            prm2 = int(prm2)

        n = prm1 * prm2
        phi = (prm1 - 1) * (prm2 - 1)

        e = input("enter the value of e: ")
        if e.lower() == "default":
            e = self.__generateE__(phi)
        else:
            assert math.gcd(int(e), phi) == 1, "phi and e must be coprimes"
            e = int(e)

        # The loop below converts the letters in the message into their numerical equivalents
        # by mapping their values in the dictionary

        numWord = ""
        for char in message:
            numWord += self.__numsMap__[char]

        # we used the below loop to know the number of digits of each block
        # the number digits is equal to the largest 2525...25 which is less than n
        # thus we add 2 more digits on every iteration till the num is greater than n
        numsDigit = 0
        num = 0
        while True:
            num = (100 * num) + 25
            if num > n:
                break
            numsDigit += 2

        # The main encryption process happens here we divide the converted message into blocks of numsDigit and
        # calculate each block's m**e mod n and concatenate it to the encrypted message
        pointer = numsDigit
        point = 0
        encryptedNum = ""
        encryptedMsg = ""

        while pointer <= len(numWord):
            sliced = numWord[point: pointer]
            # slices the message into 2N digits
            sliced = int(sliced)
            temp = pow(sliced, e, n)
            while len(str(temp)) < numsDigit:
                temp = "0" + str(temp)
            # we calculate c and concatenate it with the encrypted message
            encryptedNum += str(temp) + " "
            point = pointer
            pointer += numsDigit

        if point < len(numWord):
            # we use the if statement to check if the last slice was omitted due to it being less than 2N if point =
            # len(numWord) the every slice has been encrypted but if not then it means there remains some which
            # hasn't been encrypted
            sliced = numWord[point:]
            sliced = int(sliced)
            temp = pow(sliced, e, n)
            while len(str(temp)) < numsDigit:
                temp = "0" + str(temp)
            encryptedNum += str(temp) + " "

        i = 0
        temp = encryptedNum.replace(" ", "")
        while i <= len(temp) - 2:
            encryptedMsg += self.charsMap[temp[i: i + 2]]
            i += 2

        print(f"n = {n} \ne = {e} \nencrypted number: {encryptedNum} \nencrypted text: {encryptedMsg}")

    def decrypt(self, message):
        prm1 = int(input("Enter the first prime: "))
        prm2 = int(input("Enter the second prime: "))
        e = int(input("Enter the value of e: "))

        n = prm1 * prm2
        phi = (prm1 - 1) * (prm2 - 1)

        d = pow(e, -1, phi)
        # this will return the modular multiplicative inverse of e mod phi which is equal to d

        message = message.replace(" ", "")

        numsDigit = 0
        num = 0
        while True:  # computes the digit length of each block
            num = (100 * num) + 25
            if num > n:
                break
            numsDigit += 2

        pointer = numsDigit
        point = 0
        decryptedNum = ""
        decryptedMsg = ""
        while pointer <= len(message):
            sliced = message[point: pointer]
            # slices the message into 2N digits
            sliced = int(sliced)
            temp = pow(sliced, d, n)
            while len(str(temp)) < numsDigit:
                # since each letter is represented by two numbers we add additional zeros in front of the number
                # until it is equal to numsDigit, which is even
                temp = "0" + str(temp)

            decryptedNum += str(temp)
            point = pointer
            pointer += numsDigit

        if point < len(message):
            sliced = message[point:]
            sliced = int(sliced)
            temp = pow(sliced, d, n)
            while len(str(temp)) < numsDigit:
                temp = "0" + str(temp)

            decryptedNum += str(temp)
        i = 0
        while i <= len(decryptedNum) - 2:
            # change the decrypted numbers into their equivalent letters using the dictionary
            decryptedMsg += self.charsMap[decryptedNum[i: i + 2]]
            # we made the slicing from i to i+2 because we know that every character is expressed by two numbers
            i += 2

        print(f"decrypted number: {decryptedNum} \ndecrypted message: {decryptedMsg}")

    def __generatePrime__(self, init, final):
        isPrime = True
        primesList = []
        for i in range(init, final):
            for j in range(2, int(math.sqrt(i))):
                if i % j == 0:
                    isPrime = False  # by definition of primes
                    break
            if isPrime:
                primesList.append(i)
            isPrime = True
        # after storing all the primes between init amd final we randomly choose an element and return it
        return random.choice(primesList)

    def __generateE__(self, phi):
        eList = []
        for i in range(2, phi):
            if math.gcd(i, phi) == 1:
                eList.append(i)  # store all number between 1 and phi which are coprime with phi

        return random.choice(eList)


def main():
    choice = input("What do you want to do \n1. Encrypt \n2. Decrypt \n3. Exit \nEnter your choice or choice number: ")
    if choice.lower() == "exit" or choice == "3":
        return
    elif choice.lower() == "encrypt" or choice == "1":
        message = input("Enter the text to be encrypted: ")
        encryptionType = input(
            "Choose your encryption method; \n1. Affine Cipher \n2. Transposition Cipher \n3. RSA \n> ")
        if encryptionType == "1":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            obj = AffineCipher()
            obj.encrypt(message, num1, num2)
        elif encryptionType == "2":
            blockLength = int(input("Enter the block length: "))
            obj = TranspositionCipher()
            obj.encrypt(message, blockLength)
        elif encryptionType == "3":
            obj = RSA()
            obj.encrypt(message)
        else:
            raise Exception("Invalid input")
    elif choice.lower() == "decrypt" or choice == "2":
        message = input("Enter the text to be decrypted: ")
        decryptionMode = input("Choose decryption method; \n1. Affine Cipher \n2. Transposition Cipher \n3. RSA \n> ")
        if decryptionMode == "1":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            obj = AffineCipher()
            obj.decrypt(message, num1, num2)
        elif decryptionMode == "2":
            blockLength = int(input("Enter the block length: "))
            obj = TranspositionCipher()
            obj.decrypt(message, blockLength)
        elif decryptionMode == "3":
            obj = RSA()
            obj.decrypt(message)
        else:
            raise Exception("Invalid input")


main()
