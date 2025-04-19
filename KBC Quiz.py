print("\tWelcome to KBC Quiz\n")

questions = [
["1. Which planet is closest to the Sun?", "Earth", "Mercury", "Mars", "Jupiter", "b"],
['2. Which musician is known as the "King of Rock and Roll"?', "Chuck Berry", "Elvis Presley", "Little Richard", "Jerry Lee Lewis","b"],
['3. Which chemical element has the symbol "H"?', "Helium", "Oxygen", "Nitrogen", "Hydrogen", "d"],
["4. Which country is the largest in Scandinavia?", "Sweden", "Norway", "Denmark", "Finland", "a"],
['5. Which author wrote "To Kill a Mockingbird"?', "Harper Lee", "F. Scott Fitzgerald", "Jane Austen", "J.K. Rowling", "a"],
["6. Which sport is played on ice with a puck and sticks?", "Soccer", "Basketball", "Tennis", "Hockey", "d"],
["7. Which artist painted the Mona Lisa?", "Michelangelo", "Leonardo da Vinci", "Raphael", "Caravaggio", "b"],
["8. Which country is home to the ancient city of Machu Picchu?", "Chile", "Argentina", "Brazil", "Peru", "d"],
["9. Which actor played Luke Skywalker in the original Star Wars trilogy?", "Harrison Ford", "Carrie Fisher", "Alec Guinness", "Mark Hamill", "d"],
["10. Which element is essential for human respiration?", "Carbon dioxide", "Oxygen", "Nitrogen", "Helium", "b"],
["11. Which ancient civilization built the Great Library of Alexandria", "Egyptians", "Greeks", "Romans", "Babylonians", "a"],
["12. Which scientist developed the theory of evolution through natural selection?", "Galileo Galilei", "Isaac Newton", "Charles Darwin", "Albert Einstein", "c"],
["13. Which novel by George Orwell is set in a dystopian future?", "1984", "Animal Farm", "Brave New World", "The Handmaid's Tale", "a"],
['14. Which artist created the sculpture "David"?', "Donatello", "Raphael", "Leonardo da Vinci", "Michelangelo", "d"]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 10000000,]

# Game function
def game():
    for i in range(0, len(questions)):
        question = questions[i]
        print("\nQuestion for Rs.", levels[i])
        print(question[0])
        print("a. ",question[1],    "b. ",question[2],)
        print("c. ",question[3],    "d. ",question[4],)
        reply = input("Enter your choice: ")
        if (reply == question[-1]):
            money = 0
            money += levels[i]
            print("Correct answer! You have won Rs.", money, "\n\n")
            if (i >= 4):
                money = 10000
            elif (i >= 9):
                money = 320000
            elif(i >= 14):
                money = 10000000
            else:
                money = 0
        else:
            print("Wrong answer!")
            if (i >= 4):
                money = 10000
            elif (i >= 9):
                money = 320000
            elif(i >= 14):
                money = 10000000
            else:
                money = 0
                
            print("Your take home money is", money, "\n\n")
            break
            
# menu
def menu():
    print('Enter "S" to start the game\nEnter "A" to chech the answer section\nEnter "Q" to quit the game')
    
    
# Answer section
def answer():
    for i in range (len(questions)):
        answer = questions[i]
        print("Answer for Q.", i+1 , "is", answer[5])
        i += 1
    
    
# Quit
def quit():
    quiting = input("Are you sure? ")
    if (quiting == "yes" or quiting == "Yes"):
        print("Okay Bye!")
        exit()
    else:
        print(" ^_^ --> Okay???")

# Security Checkup
def security():
    password = input("Enter the secret password: ")
    if (password == "KBC$()"):
        print("Correct password...")
        sec = input("Do you want to check answers? (Yes/No) ")
        if (sec == "Yes" or sec == "yes"):
            print("Below are the answers...\n")
            answer()
        elif (sec == "No" or sec == "no"):
            print("Okay fine...\n")
        else:
            print("Invalid command!")
    else:
        print("Incorrect password...\n")



# Calling Functions (Final Step)...
while True:
    menu()
    mn = input("Enter your choice: ")
    if (mn == "s" or mn == "S"):
        asking_ready = input("Are you ready? ")
        if (asking_ready == "yes" or asking_ready == "Yes"):
            print("Okay let's go...!\n\n")
            game()
        elif (asking_ready == "no" or asking_ready == "No"):
            print("Get ready first...\n")
        else:
            print("Invalid response!\n")
            
    elif (mn == "a" or mn == "A"):
        security()
    elif(mn == "q" or mn == "Q"):
        quit()
    else:
        print("Invalid response!\n")