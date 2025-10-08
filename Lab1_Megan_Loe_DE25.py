#task 1 instructions for the lab

#read the text file called dna_raw.txt
#each sequene is composed of two lines of data: the first line beginning with > sign is the sequence ID, while the following line is the actual sequence
#the actual sequence is not case-sensitive, which means that lower and upper case letters are treated the same
#letters that need to be scanned for are A, C, G and T

#for each sequence, create a dictionary to count the number of each DNA letter in that sequence
#for each sequence, graph the frequency of DNA letters for each sequence


#all of the above is the instructions for this lab, I copied into here so I don't have to constantly switch windows and lose track of where I was

#this is here just in case, I need to use it
import re

import linecache




#this area is for the menus
#this is the opening menu
def DNA_menu():
    print("1. dna txt file")
    print()
    print("2. the more complicated dna txt file")
    print()
    print("3. end")
    print()
    print()

#menu for the first txt file
def DNA_menu_raw():
    print("sequence 1")
    print()
    print("sequence 2")
    print()
    print("sequence 3")
    print()
    print("sequence 4")
    print()
    print()

#menu for the second txt file
def DNA_menu_complicated():
    print("sequence 1")
    print()
    print("sequence 2")
    print()
    print("sequence 3")
    print()
    print("sequence 4")
    print()
    print()

#dna counting, its counts! partially. . .
def dna_count(DNA):
    #the dictionary for the letters that need to be found
    dna_letters = {
        "A" : 0, 
        "C" : 0, 
        "G" : 0, 
        "T" : 0}
    
    #to count the letters
    for letters in DNA:
        dna_letters ["A"] += 1
        dna_letters ["C"] += 1
        dna_letters ["G"] += 1
        dna_letters ["T"] += 1
        print(dna_letters)
    
    #need to do an if statement in this function

#the loop
while True:
     
     #opening menu
     DNA_menu()
     dna_menu = input("which file would you like to check? ")
     if dna_menu == "1":
        DNA_menu_raw()
        
    
     elif dna_menu == "2":
         DNA_menu_complicated()
         break
    
     elif dna_menu == "3":
         print("ok ending program")
         break

        #the menu to select sequence for the first file
     if dna_menu == "1":
         dna_seq_1 = input("which sequence would you like to run? ") #selects the sequence to read

        #opens the file
         dna_raw = open("dna_raw.txt")


         if dna_seq_1 == "1":
             seq1_raw = linecache.getline("dna_raw.txt", 2)
             print(seq1_raw)
             break
         
         elif dna_seq_1 == "2":
             seq2_raw = linecache.getline("dna_raw.txt", 4)
             print(seq2_raw)
             break
         
         elif dna_seq_1 =="3":
             seq3_raw = linecache.getline("dna_raw.txt", 6)
             print(seq3_raw)
             break
         
         elif dna_seq_1 =="4":
             seq4_raw = linecache.getline("dna_raw.txt", 8)
             print(seq4_raw)
             break



     








