#task 1 instructions for the lab

#read the text file called dna_raw.txt
#each sequene is composed of two lines of data: the first line beginning with > sign is the sequence ID, while the following line is the actual sequence
#the actual sequence is not case-sensitive, which means that lower and upper case letters are treated the same
#letters that need to be scanned for are A, C, G and T

#for each sequence, create a dictionary to count the number of each DNA letter in that sequence
#for each sequence, graph the frequency of DNA letters for each sequence


#all of the above is the instructions for this lab, I copied into here so I don't have to constantly switch windows and lose track of where I was

#the imported functions
import linecache

import matplotlib.pyplot as plt

#this area is for the menus
#this is the opening menu
def DNA_menu():
    print()
    print("1. dna txt file")
    print()
    print("2. the more complicated dna txt file, DOES NOT WORK CURRENTLY")
    print()
    print("3. end")
    print()
    print()

#menu for the first txt file
def DNA_menu_raw():
    print()
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
def DNA_menu_comp():
    print()
    print("sequence 1")
    print()
    print("sequence 2")
    print()
    print("sequence 3")
    print()
    print("sequence 4")
    print()
    print()

#dna counting, it counts!
def dna_count(DNA):
    
    #the dictionary for the letters that need to be found
    dna_let = {
        "A" : 0, "C" : 0, 
        "G" : 0, "T" : 0}

    #to count the letters
    for letters in DNA:
        if letters == "a" or letters == "A":
            dna_let["A"] += 1
            
        elif letters == "c" or letters == "C":
            dna_let ["C"] += 1
            
        elif letters == "g" or letters == "G":
            dna_let ["G"] += 1
             
        elif letters == "t" or letters == "T":
            dna_let ["T"] += 1

    print(dna_let)

def dna_graph(DNA): #this is the graph output
    x = ["A", "C", "G", "T"]

    y = [0, 0, 0, 0]

    for letters in DNA: #copied this from the dna count, but now it adds to y
        if letters == "a" or letters == "A":
            y[0] += 1
        
        elif letters == "c" or letters == "C":
            y[1] += 1
        
        elif letters == "g" or letters == "G":
            y[2] += 1
        
        elif letters == "t" or letters == "T":
            y[3] += 1
    
    plt.bar(x, y)
    plt.show()


#the loop
while True:
     
     #opening menu
     DNA_menu()
     dna_menu = input("which file would you like to check? ")
     if dna_menu == "1":
        DNA_menu_raw()
        
     elif dna_menu == "2":
         DNA_menu_comp()
         break
         
     elif dna_menu == "3":
         print("ok ending program")
         break

        #the menu to select sequence for the first file
     if dna_menu == "1":
         dna_seq_nr = input("which sequence would you like to run? ") #selects the sequence to read

        #opens the file
         dna_raw = open("dna_raw.txt")

        #the menu to select sequences
         if dna_seq_nr == "1": #sequence 1
             seq1_raw = linecache.getline("dna_raw.txt", 2) #fetches the sequence
             print(seq1_raw)
             dna_count(seq1_raw) #counts the letters in the sequence
             dna_graph(seq1_raw) #shows the graph for the sequence
             dna_raw.close()
             break
         
         elif dna_seq_nr == "2": #sequence 2
             seq2_raw = linecache.getline("dna_raw.txt", 4)
             print(seq2_raw)
             dna_count(seq2_raw)
             dna_graph(seq2_raw)
             dna_raw.close()
             break
         
         elif dna_seq_nr =="3": #sequence 3
             seq3_raw = linecache.getline("dna_raw.txt", 6)
             print(seq3_raw)
             dna_count(seq3_raw)
             dna_graph(seq3_raw)
             dna_raw.close()
             break
         
         elif dna_seq_nr =="4": #sequence 4
             seq4_raw = linecache.getline("dna_raw.txt", 8)
             print(seq4_raw)
             dna_count(seq4_raw)
             dna_graph(seq4_raw)
             dna_raw.close()
             break
     

             
