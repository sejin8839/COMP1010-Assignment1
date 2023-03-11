'''
Date: Mar 11, 2023
Author :  Name: SejinYoon
          uID: u1311019
Source code File name: problem3.py
'''


DNA_nucleotide = input("Enter DNA nucleotide sequences: ")

length = (len(DNA_nucleotide))
Percentage_of_A= (DNA_nucleotide.count('A'))/length
Percentage_of_T= (DNA_nucleotide.count('T'))/length
Percentage_of_C= (DNA_nucleotide.count('C'))/length
Percentage_of_G= (DNA_nucleotide.count('G'))/length

print(f"The length of the sequence: {length}")
print(f"Percent of A: {Percentage_of_A:.2f}%")
print(f"Percent of T: {Percentage_of_T:.2f}%")
print(f"Percent of C: {Percentage_of_C:.2f}%")
print(f"Percent of G: {Percentage_of_G:.2f}%")
