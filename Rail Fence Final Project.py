#Import libraries
from itertools import permutations
import PySimpleGUI as gui
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

#Define function encrypt that takes in a plaintext and key
def encrypt(string,key):
    global encrypted_text
    """
    Empty list to form a list of lists that will contain the plain text seperated into columns
    depending on the length of the key
    """
    lst=[]
    #Appends a list to have the columns prepared
    for i in range(len(key)):
        lst.append([])
        j=0
    #appends each letter in the plaintext to its corresponding column
    for i in range(len(string)):
        lst[j].append(string[i])
        j = (j+1) % len(key)
    
    #creates a list of the key
    key_numbers = []
    for number in key:
        number = int(number)
        key_numbers.append(number)
    
    #Appends a list to have the columns prepared
    encrypted_list = []
    for i2 in range(len(key)):
        encrypted_list.append([])
    
    
    #creates a list of the plaintext shifted into its proper place depending on the key position
    for y in key_numbers:
        encrypted_list[y].append(lst[0])
        lst.pop(0)
    
    #finally we get every letter in the encrypted list of lists and add it to an empty string
    encrypted_text = ""
    for x in encrypted_list:
        for z in x:
            for z2 in z:
                encrypted_text += z2
    #prints encrypted word
    print("Encrypted Rail Fence Text: " + encrypted_text)


#define decipher3 function that takes in a ciphered list and the permutation of the key used
def decipher3(cipher_list,permutation):
    #sets total length equal to 0 for later addition
    total_len = 0
    #for loop that will give us the total length of our ciphertext
    for i in range(len(cipher_list)):
        total_len += len(cipher_list[i])
    #empty string
    string =""
    i=0
    #while loop that will end once the length of our is equal to the length of total length
    while len(string)<total_len:
        #appends first letter from first word split in the cipher list
        string+=cipher_list[i][0]
        #removes the letter we just appended
        cipher_list[i].pop(0)
        #sets i equal i + 1 modulo length of our cipher list so that we can iterate back to 0
        i=(i+1)%len(cipher_list)
    #finally prints our key permutation being used and the decrypted message
    print("Using key:", permutation)
    print("Your decrypted message:",string)
    
#defines function decipher2 that takes in the ciphertext, the grouping of the word split, and 1 permutation of the key
def decipher2(ciphertext,grouping,permutation):
    permutation_key = permutation
    columns =[]
    grouping2 = []
    #prepares empty lists within the lists above to append to later
    for i in range(len(grouping)):
        columns.append([])
        grouping2.append([])
    #for loop to reshuffle the grouping word split into the key's position
    for i in range(len(grouping)):
        grouping2[permutation[i]] = grouping[i]
    #sets a low and high variable equal to 0 for later addition
    low=0
    high=0
    #for loop that will give us the proper word split for the cipher text and will append it to columns
    for i in range(len(grouping2)):
        high += grouping2[i]
        string=ciphertext[low:high]
        columns[i].append(list(string))
        #set low equal to high to have proper word splitting
        low=high

    dec = []
    dec2 = []
    #for loop to organize the word splits we have prepared in columns to append it to dec list in the position of the key
    for i in range(len(columns)):
        dec.append(columns[permutation[i]])
    for i in dec:
        for x in i:
            dec2.append(x)
    #calls for decipher 3 function
    decipher3(dec2,permutation_key)
        
#Define fucntion decrypt that takes in the ciphertext    
def decrypt(ciphertext):
    cipher_text = ciphertext
    #message length of ciphertext
    msg_size = len(ciphertext)
    #all possible key lengths from 2-5
    possible_keys = [[0,1],[0,1,2],[0,1,2,3],[0,1,2,3,4]]
    #empty list to add how the word will be split up depending on the length of the key
    groups = []
    
    group1 = []
    #this for loop will append to the group1 list how the ciphertext would be split on a key length of 2
    for i in range(len(possible_keys[0])):
        if i == 0:
            #divides the message size of ciphertext into 2
            number1 = (msg_size/len(possible_keys[0]))
            #if we get a non-integer result we will round up to next integer
            if number1.is_integer()==False:
                number1 = ((msg_size//len(possible_keys[0])) + 1)
            #append the first split into the group1 list
            group1.append(int(number1))
        elif i == 1:
            #computes our new message size by substracting our result from the ciphertext length
            new_msg_size1 = msg_size - number1
            #divides the message size of cipher text into 1
            number2 = (new_msg_size1/(len(possible_keys[0]) - 1))
            if number2.is_integer()==False:
                number2 = ((new_msg_size1//(len(possible_keys[0]) - 1)) + 1)
            group1.append(int(number2))
    #appends group1 into list of lists groups for later use
    groups.append(group1)
   
    
    
    # Get all permutations of key length 2
    perm1 = permutations(possible_keys[0])
    perms_of_key1 = [] 
    for i in list(perm1): 
        perms_of_key1.append(list(i))

    #same method we did with group1 but now with a key length of 3
    group2 = []
    for i in range(len(possible_keys[1])):
        if i == 0:
            number1 = (msg_size/len(possible_keys[1]))
            if number1.is_integer()==False:
                number1 = ((msg_size//len(possible_keys[1])) + 1)
            group2.append(int(number1))
        elif i == 1:
            new_msg_size1 = msg_size - number1
            number2 = (new_msg_size1/(len(possible_keys[1]) - 1))
            if number2.is_integer()==False:
                number2 = ((new_msg_size1//(len(possible_keys[1]) - 1)) + 1)
            group2.append(int(number2))
        elif i == 2:
            new_msg_size2 = new_msg_size1 - number2
            number3 = (new_msg_size2/(len(possible_keys[1]) - 2))
            if number3.is_integer()==False:
                number3 = ((new_msg_size2//(len(possible_keys[1]) - 2)) + 1)
            group2.append(int(number3))
    groups.append(group2)
    
    # Get all permutations of key length 3
    perm2 = permutations(possible_keys[1])
    perms_of_key2 = []
    for i in list(perm2): 
        perms_of_key2.append(list(i))
    
    #same method we did with group1 but now with a key length of 4
    group3 = []
    for i in range(len(possible_keys[2])):
        if i == 0:
            number1 = (msg_size/len(possible_keys[2]))
            if number1.is_integer()==False:
                number1 = ((msg_size//len(possible_keys[2])) + 1)
            group3.append(int(number1))
        elif i == 1:
            new_msg_size1 = msg_size - number1
            number2 = (new_msg_size1/(len(possible_keys[2]) - 1))
            if number2.is_integer()==False:
                number2 = ((new_msg_size1//(len(possible_keys[2]) - 1)) + 1)
            group3.append(int(number2))
        elif i == 2:
            new_msg_size2 = new_msg_size1 - number2
            number3 = (new_msg_size2/(len(possible_keys[2]) - 2))
            if number3.is_integer()==False:
                number3 = ((new_msg_size2//(len(possible_keys[2]) - 2)) + 1)
            group3.append(int(number3))
        elif i == 3:
            new_msg_size3 = new_msg_size2 - number3
            number4 = (new_msg_size3/(len(possible_keys[2]) - 3))
            if number4.is_integer()==False:
                number4 = ((new_msg_size3//(len(possible_keys[2]) - 3)) + 1)
            group3.append(int(number4))
    groups.append(group3)
    
    
    # Get all permutations of key length 4
    perm3 = permutations(possible_keys[2])
    perms_of_key3 = []
    for i in list(perm3): 
        perms_of_key3.append(list(i))

    
    #same method we did with group1 but now with a key length of 5
    group4 = []
    for i in range(len(possible_keys[3])):
        if i == 0:
            number1 = (msg_size/len(possible_keys[3]))
            if number1.is_integer()==False:
                number1 = ((msg_size//len(possible_keys[3])) + 1)
            group4.append(int(number1))
        elif i == 1:
            new_msg_size1 = msg_size - number1
            number2 = (new_msg_size1/(len(possible_keys[3]) - 1))
            if number2.is_integer()==False:
                number2 = ((new_msg_size1//(len(possible_keys[3]) - 1)) + 1)
            group4.append(int(number2))
        elif i == 2:
            new_msg_size2 = new_msg_size1 - number2
            number3 = (new_msg_size2/(len(possible_keys[3]) - 2))
            if number3.is_integer()==False:
                number3 = ((new_msg_size2//(len(possible_keys[3]) - 2)) + 1)
            group4.append(int(number3))
        elif i == 3:
            new_msg_size3 = new_msg_size2 - number3
            number4 = (new_msg_size3/(len(possible_keys[3]) - 3))
            if number4.is_integer()==False:
                number4 = ((new_msg_size3//(len(possible_keys[3]) - 3)) + 1)
            group4.append(int(number4))
        elif i == 4:
            new_msg_size4 = new_msg_size3 - number4
            number5 = new_msg_size4
            group4.append(int(number5))
    groups.append(group4)
    
    
    # Get all permutations of key length 5
    perm4 = permutations(possible_keys[3])
    perms_of_key4 = []
    for i in list(perm4): 
        perms_of_key4.append(list(i))
    
    #for loop that iterates through each possible key length
    for length in possible_keys:
        if len(length) == 2:
            #set group to group1 value of a key length of 2
            group = groups[0]
            #set permut as all the permutations of key length 2
            permut = perms_of_key1
        elif len(length) == 3:
            #set group to group1 value of a key length of 3
            group = groups[1]
            #set permut as all the permutations of key length 3
            permut = perms_of_key2
        elif len(length) == 4:
            #set group to group1 value of a key length of 4
            group = groups[2]
            #set permut as all the permutations of key length 4
            permut = perms_of_key3
        elif len(length) == 5:
            #set group to group1 value of a key length of 5
            group = groups[3]
            #set permut as all the permutations of key length 5
            permut = perms_of_key4
        #for loop to iterate through every permutation of the key
        for i in permut:
            #calls for decipher2 function
            decipher2(cipher_text,group,i)
            #asks user if message is legible to read
            decision = input("Is the message legible?: ")
            decision = decision.lower()
            #if yes then the message is decrypted and the loop will break ending the program
            if decision[0]=="y":
                print("Message is decrypted!")
                break
        else:
            continue
        break

#Welcome message
print("Welcome to the Rail Fence Cipher Program!")

#Opens dialog box to choose a file for encryption and reads the file and returns it as a string
def user_select_file():
    file_path = filedialog.askopenfilename()
    f = open(file_path, "r")
    f = f.read()
    #Replaces \n new lines with a empty string to eliminate new lines making encoding stronger
    f = f.replace("\n", "")
    return f

#Opens dialog box to save the ciphered text to a .txt file in a user selected location
def save_ciphered_text(cipherfile):
    f2 = asksaveasfile(mode='w', defaultextension=".txt")
    f2.write(cipherfile)
    f2.close()
    print("Cipher is saved!")
    
def decrypt_window():
    global file_text
    global window3
    #GUI layout
    decrypt_layout = [[gui.Text("Type message to decrypt:"), gui.InputText()],
                      [gui.Text("OR")],
                      [gui.Text("Choose a text file to decrypt:"), gui.Button("Browse")],
                      [gui.Text("-----------------------------------------------------------------")],
                      [gui.Text("Refer to Python IDE command prompt to check for meaningful text.")],
                      [gui.Submit(), gui.Cancel()]]
    window3 = gui.Window("Decryption", decrypt_layout)
    while True:
        event, values = window3.read()
        if event == None or event == "Cancel":
            break
        elif event == "Submit":
            cipher_text1 = str(values[0])
            decrypt(cipher_text1)
            window3.close()
            
        elif event == "Browse":
            cipher_text1 = user_select_file()
            decrypt(cipher_text1)
            window3.close()   
    
    
def encrpyt_window():
    global encrypt_text
    global file_text
    #Layout for encrypt GUI
    encrypt_layout = [[gui.Text("Enter key:"), gui.InputText()],
                       [gui.Text("------------------------------------------------------------------------")],
                       [gui.Text("Type message to encrypt:"), gui.InputText()],
                       [gui.Text("OR")],
                       [gui.Text("Choose a text file to encrypt:"), gui.Button("Browse")],
                       [gui.Submit(), gui.Cancel()]]
                       
    window2 = gui.Window("Encryption", encrypt_layout)
    while True:
        event, values = window2.read()
        if event == None or event == "Cancel":
            break
        elif event == "Submit":
            readable_text = str(values[1])
            encrypt_key = str(values[0])
            encrypt(readable_text, encrypt_key)
            save_ciphered_text(encrypted_text)
            window2.close()
            
        elif event == "Browse":
            file_text = user_select_file()
            encrypt_key = str(values[0])
            encrypt(file_text, encrypt_key)
            save_ciphered_text(encrypted_text)
            window2.close()
    
layout = [[gui.Text("Would you like to:")],
          [gui.Button("Encrypt")],
          [gui.Text("OR")],
          [gui.Button("Decrypt")],
          [gui.Text("---------")]]

window = gui.Window("Rail Fence Cipher", layout)

#User has to choose to either encrypt or decrypt
while True:
    event, values = window.read()
    if event == gui.WINDOW_CLOSED:
        break
    elif event == "Decrypt":
        window.close()
        decrypt_window()
        break
    elif event == "Encrypt":
        window.close()
        encrpyt_window()
        break