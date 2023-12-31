## 1. Affine Cipher ##
The Affine Cipher cryptosystem works in such a way that it shifts a character by multiplying its index by a constant and adding 
another constant into the product. In the implementation, we first created a dictionary to store the numerical equivalents of the 
26 english letters. for example, in the dictionary "A" is maped to 0, "B" to 1 and so on. this will help in converting the plain text
into numbers.

We have also created another dicitionary called charsDic to the letters associated with the given natural numbers. for example 1 is mapped 
to "B", 2 is mapped to "C" and so on. we used this dictionary mainly to convert numbers into their equivalent letters.

The encryption in the Affine Cipher works as follows:
first we remove any whitespace from the text. we then iterate every character in the message and check if it is found in the dicitionary.
We then assign the number that the character is mapped to in the dicitionary to a temporary variable called charNum.
for example, if the letter is "E" charNum is assigned the value of 3, which is the mapping of "E" in numsDic.

we then encrypt charNum by multiplying and adding the given number and taking their modulo 26. the number we get from
this operation will be the encrypted numerical value of the character. It is worth noting that we have added a little twist, so that our 
program could identify small and capital letters and thus return the appropriate value. when we first defined the dictionary we made the index
of all small letters greater than 25, thus if initially charNum was greater than 25, then its encryption must also be greater than 25. that is why 
we added the 26, whenever charNum > 25.

If the character is neither small nor capital english letter, we simply add the character without encrypting it.

after encrypting a character, we change it to its letter form and concatenate it in the encrypted messages variable.

the decryption works the same way except that there is a change in the formula to find the decrypted characternumber.
we have also used python's built in pow function to find the inverse of num1 modulo 26.


## 2. Transposition Cipher ##
in the Transposition Cipher we accept two arguments, the message and a key which represents the number of characters each block
should have.

We first ask the user to input the permutation used for encryption. we store this permutations in a dictionary so that we could
use it anytime we want. But if the user exits without inputing all the permutations we simply add a permutation from m to m (for some m)
until we have key number of permutations.

After creating the dictionary we began the encryption process by slicing the given message so that each slice will have
key number of characters. after that we create an empty list and implemnt the permutations on the list. for example, if we arguments
given a permutation from 3 to 1, we make list[1] = message[3] and so on until, the size of the list become equal to the key.
we have also added aditional if statement to ensure that no character has been omitted. if all elements are sliced (i.e. included in the sliced words)
then pointer must equal the size of the message. if not it means that there are some elements left thus we encrypt them using the above 
mentioned technique.

in decryption, we perform the same process except in permutation of the list we interchange the final and initial values. for example, in the above example
we were given the permutation 3 to 1, when we decrypt this we do list[3] = message[1] not list[1] = message[3].


## 3. RSA ##
To implement the RSA cryptosystem we first created a dictionary to map all alphaneumeric characters with their respective numeric values. we have seen how to do that.
we then give the user two options, either he/she inserts the key by him/herself or use an autogenerated values. to generate a prime number we iterate over 
the given interval if all the numbers from 2 to the square root of the number don't divide the number, we conclude that the number is prime. we add this number 
to our list. we then randomly choose a number from that list.

to generate e, we iterate from 2 to phi (since 1 < e < phi) and add to our list those numbers that are relatively prime to phi(i.e. gcd(num, phi) =1).
we then choose a random element from the list.

we then change our message into numbers using the previosly mentioned method of using a dictionary.

to find the number of digits of each partiotion we use the algorithm from line 250 to 254. after that we slice the message by numsDigit amount
and encrypt it using the formula m**e (mod n). then if the result of this operation has a length less than numsDigit we add zeroes in front of it
until it has the same size as numsDigit. we also check if there is any omitted element like we have done earlier. we then 
concatenate the number to our encrypted numbers string. then we can change the numbers back into letters and characters using previosly mentioned 
techniques. 

we note that we used the pow function to compute m**e (mod n) becaused it is very efficient to calculate the modulo of large numbers.

decryption works the same way but instead of m ** e (mod n), we calculate m**d (mod n) where d is the modular multiplicative inverse of 9e mod phi)
