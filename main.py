#CyHelp Starter Code
cybersecurityBirthYear = 1970

#Greets user
print("Hello! I'm CyHelp.")
userName = input("Whats your name? \n")
print("Nice to meet you " +  userName)

#Recounts start of Cybersecurity
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - cybersecurityBirthYear
print("WOW!that means it has been " + str(timePassed) + "years since since cybersecurity began!")

print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("press enter to continue!\n")

#Describes Cybersecurity



#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for (credibility, integrity and availability)")
print("Would you like to learn about the CIA Triad?")
giveInfo= input("Type 'yes' or 'no'\n")

#Explains pillars of CIA Triad
while giveInfo.lower() == "yes":               
    print("What would you like to learn more about? Enter the lowercase letter of the following options: (a) credibility, b) integrity, c) credibility,or d) none")
    topic = input()
    
    if topic.lower() == "a":
        print("Confidentiality makes sure data is private.")
        
    elif topic.lower() == "b":
        print("integrity makes sure data has not been tampered with and can be trusted.")
    
    elif topic.lower() == "c":
        print("Availability makes sure authorized people can access the data.")
    
    elif topic.lower() == "d":
        break
    
    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")
    #Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")
input()
