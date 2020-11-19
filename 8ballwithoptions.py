#Kody Lace, 000757994
import os
import time
import random

#Navigate to correct directory to see the responses text file
path=os.getenv("UserProfile") + "\Desktop\KodyLacePythonProject"
os.chdir(path)

gameMode=input("Do you have time to experience the full effect of the magic 8 ball? (yes or no)")

if gameMode == "yes":
    #beginning ASCII art
    print("BEHOLD... ", end = '')
    time.sleep(2)
    print("The magic 8 ball!")
    time.sleep(3)
    print("POOF!")
    print(""" 
                    ,dP9CGG88@b,
                  ,IP  _   Y888@@b,
                 dIi  (_)   G8888@b
                dCII  (_)   G8888@@b
                GCCIi     ,GG8888@@@
                GGCCCCCCCGGG88888@@@
                GGGGCCCGGGG88888@@@@...
                Y8GGGGGG8888888@@@@P.....
                 Y88888888888@@@@@P......
                 `Y8888888@@@@@@@P......
                    `@@@@@@@@@P.......""")

    #Newline
    print("")
    print("")

    #while loop to let the player keep playing if they choose
    keepPlaying = True
    while keepPlaying == True:

        #Get users question
        print("Enter your question...",end='')
        time.sleep(2)
        userAnswer=input(" if you dare: ")
        print("")
        print("""`  ,     '    ` .     '     ,   .       `      ~     ,  `   .   , '     `
                .    `   ,  .     `     ,        `   '    -      ,       `.    '      `
           `   ,  The 8 Ball is finding the answer to your question.     
         `  `  .    `   ,  .     `     ,        `   '    -      ,       `.    '      `
             `  ,     '    ` .     '     ,   .       `      ~     ,  `   .   , '     `""")
        print(" `  `  .    `   ,  .     `     ,        `   '    -      ,       `.    '      `")
        time.sleep(1)
        print("     .    `   ,  .     `     ,        `   '    -      ,       `.    '      `        `")
        time.sleep(1)
        print("")
        time.sleep(2)
        print("The magic 8 ball says: ",end='')

        #Open the text file with the answers       
        openFile=open('responses.txt')
        random_line=random.choice(open('responses.txt').readlines())
        print(random_line)

        keepPlaying=input("Do you want to play again?(yes or no) ")
        print("")
        if keepPlaying == "no":
            print("Until next time...")
            print("   Goodbye.")
            exit
            keepPlaying=False
        elif keepPlaying=="yes":
            keepPlaying=True
        else:
            print("The magic 8 ball cannot decipher your message, try again later") 


#same code, but does not have the sleep timers in so it takes less time to play
else:
    print("Patience is a virtue.")
    #beginning ASCII art
    print("BEHOLD... ", end = '')
    
    print("The magic 8 ball!")
    
    print("POOF!")
    print(""" 
                    ,dP9CGG88@b,
                  ,IP  _   Y888@@b,
                 dIi  (_)   G8888@b
                dCII  (_)   G8888@@b
                GCCIi     ,GG8888@@@
                GGCCCCCCCGGG88888@@@
                GGGGCCCGGGG88888@@@@...
                Y8GGGGGG8888888@@@@P.....
                 Y88888888888@@@@@P......
                 `Y8888888@@@@@@@P......
                    `@@@@@@@@@P.......""")

    #Newline
    print("")
    print("")

    #while loop to let the player keep playing if they choose
    keepPlaying = True
    while keepPlaying == True:

        #Get users question
        print("Enter your question...",end='')
        
        userAnswer=input(" if you dare: ")
        print("")
        print("""`  ,     '    ` .     '     ,   .       `      ~     ,  `   .   , '     `
                .    `   ,  .     `     ,        `   '    -      ,       `.    '      `
           `   ,  The 8 Ball is finding the answer to your question.     
         `  `  .    `   ,  .     `     ,        `   '    -      ,       `.    '      `
             `  ,     '    ` .     '     ,   .       `      ~     ,  `   .   , '     `""")
        print(" `  `  .    `   ,  .     `     ,        `   '    -      ,       `.    '      `")
        
        print("     .    `   ,  .     `     ,        `   '    -      ,       `.    '      `        `")
        
        print("")
        
        print("The magic 8 ball says: ",end='')

        #Open the text file with the answers       
        openFile=open('responses.txt')
        random_line=random.choice(open('responses.txt').readlines())
        print(random_line)

        keepPlaying=input("Do you want to play again?(yes or no) ")
        print("")
        if keepPlaying == "no":
            print("Until next time...")
            print("   Goodbye.")
            exit
            keepPlaying=False
        elif keepPlaying=="yes":
            keepPlaying=True
        else:
            print("The magic 8 ball cannot decipher your message, try again later") 


