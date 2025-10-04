#task 1 instructions for the lab

#read the text file called dna_raw.txt
#each sequene is composed of two lines of data: the first line beginning with > sign is the sequence ID, while the following line is the actual sequence
#the actual sequence is not case-sensitive, which means that lower and upper case letters are treated the same
#letters that need to be scanned for are A, C, G and T

#for each sequence, create a dictionary to count the number of each DNA letter in that sequence
#for each sequence, graph the frequency of DNA letters for each sequence


#all of the above is the instructions for this lab, I copied into here so I don't have to constantly switch windows and lose track of where I was

#the dictionary
dna_letters = dict(
    A = 0, 
    C = 0, 
    G = 0, 
    T = 0
    )



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



while True:
     
     #opening menu
     DNA_menu()
     dna_menu = input("which file would you like to check? ")
     if dna_menu == "1":
        DNA_menu_raw()
        break
        
    
     elif dna_menu == "2":
         DNA_menu_complicated()
         break
    
     elif dna_menu == "3":
         print("ok ending program")
         break
     #breaking the whole loop for now until the dictonary is up and running






