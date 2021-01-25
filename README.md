# Python-Factor-Generator
Generate all factors of a given number

User enters a number that they wish to see all the factors for. We loop through every number upto to the chosen number and check if each iteration has anything left over. If it doesn't it is a factor.

We then print a summary of all the factors multipled together to equal the chosen number. We do this by taking the length of our factors array and dividing it by 2, to loop halfway through. We print to screen the first index of the array with the last index in the array until the loop is complete.

Finally we ask the user if they wish to run the programme again.

Example output:

Welcome to the Factor Generator App

Enter a number you want to see the factors of: 128

Factors of 128 are: 
1
2
4
8
16
32
64
128

In summary: 
1 * 128 = 128
2 * 64 = 128
4 * 32 = 128
8 * 16 = 128

Would you like to run this again (y/n): n

Thank you for using the Factor Generator App. Goodbye.
