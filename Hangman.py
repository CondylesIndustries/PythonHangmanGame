print("Hangman Style Game")
print("Written in Python")
print("Author: Sebastian Condyles, 14 Years of Age")
print("Condyles Industries\n")
print("Rules for playing: No spaces, no caps\nIf you " +
"know what the word is, feel free to type it in!\n\n")



import random
import time
word = random.choice(['unitedstates', 'canada', 'russia', 'mexico',
'belgium', 'england','germany', 'belgium', 'france', 'spain',
'portugal', 'brazil', 'china', 'australia', 'india', 'peru',
'japan', 'argentina', 'egypt', 'denmark', 'saudiarabia', 'mongolia'])
#word = 'canada'
#print(word)
usedchars = []
wordspaces = []
changewordspaces = []
True3 = False
True4 = False

def InitializeGhostLetters(n):
    global word
    length = len(n)
    global wordspaces
    for x in range(0, length):
        wordspaces.append("_")
        print(wordspaces[x], end = " ")

def Hangman():
    global word
    global length
    global wordspaces
    global usedchars
    global changewordspaces
    global True3
    global True4
    tries = 7
    tries1 = 10
    length = len(word)
    #def changewordspaces1():
    #    for u in range(0, len(changewordspaces)):
    #            if changewordspaces[u] == input1:
    #                print("\nthat letter has already been used")
    #                True3 = True
    #                break
    
            
    #changewordspaces1()



                




    n = 0
    while n < tries1 + 1:
        print("\nPlease input only one letter. Please use no repeating letters.")
        global input1
        input1 = input()
        #break

        
        def completer():
            if input1 == word:
                True4 = True
                #print("\nCongrats! You've won the game and the word is " + str(word))
        def UppertoLower():
                input1 = input1.lower()


            
        #UppertoLower()
        #completer()
        #break

        def input2(a):
            global True4
            global True3
            global input1
            
            #changewordspaces1()
            #UppertoLower()
            #completer()


            
            for u in range(0, len(changewordspaces)):
                if changewordspaces[u] == input1:
                    print("\nthat letter has already been used")
                    True3 = True
                    break



                
            input1 = input1.lower()
            if input1 == word:
                True4 = True
            if len(a) != 1 and True4 == False:
                print("\nPlease input only one letter.")
                input1 = input()
                input2(input1)
            if True3 == True and True4 == False:
                print("\nPlease no repeating letters.")
                input1 = input()
                input2(input1)
            if len(a) != 1 and True3 == True and True4 == False:
                print("\nPlease input only one letter. Please use no repeating letters.")
                input1 = input()
                input2(input1)



        input1 = input1.lower()


        
        for u in range(0, len(changewordspaces)):
            if changewordspaces[u] == input1:
                print("\nthat letter has already been used")
                tries1 += 1
                True3 = True
                break


            
        #input1 = input1.lower()
        
        if input1 == word:
            True4 = True
        if True4 == True:
            print("\nCongrats! You've won the game and the word is " + str(word))
            break
        if len(input1) != 1 and True4 == False:
            input2(input1)
        if True3 == True and True4 == False:
            input2(input1)
        if len(input1) != 1 and True3 == True and True4 == False:
                print("\nPlease input only one letter. Please use no repeating letters.")
                #input1 = input()
                input2(input1)
        #if True4 == True:
        #    print("\nCongrats! You've won the game and the word is " + str(word))
        #    break












        if word.find(input1) != -1:
            print("letter found")
            t = -1
            changewordspaces = []
            while True:
                try:
                    count = 0
                    t = word.index(input1, t+1)
                    changewordspaces.append(t)
                    wordspaces[t] = input1
                    count += 1
                except ValueError:
                    break

            for i in range(0, length):   #prints my array in a good way
                print(wordspaces[i], end = " ")
            print("\n\tUsed Characters: " + str(usedchars) + "\t Tries: " + str(tries))
            n += 1
            True2 = False
            for t in range(len(wordspaces)):
                if wordspaces[t] == '_':
                    True2 = True
                    break
            if True2 == False:
                print("\nCongrats! You've won the game and the word is " + str(word))
                time.sleep(8)
                break
            

        else:
            True1 = False
            print("\nletter not found")
            for v in range(0, len(usedchars)):
                if usedchars[v] == input1:
                    print("\nthat letter has already been used")
                    tries1 += 1
                    True1 = True
                    break
            if True1 == False:
                tries -= 1
                usedchars.append(input1)
            for i in range(0, length):   #prints my array in a good way
                print(wordspaces[i], end = " ")
            print("\n\tUsed Characters: " + str(usedchars) + "\t Tries: " + str(tries))
        if tries == 0:
            print("\nyou didn't save the guy in time. You lose")
            print("The word was " + str(word))
            time.sleep(8)
            break
        else:
            continue
            
InitializeGhostLetters(word)
Hangman()
