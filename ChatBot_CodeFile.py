import random

cmd_Greet = ["hello",
             "wake up",
             "you there",
             "hey",
             "hi",
             "help me"]
rply_Greet = ["Hello admin welcome back !",
              "Always there for you admin !",
              "How can i help you ?",
              "Welcome back admin how can i help you",
              "Hi admin Is there any task for me ? ",
              "Hey there ! how are you admin ?",
              "Hope you missed me ! How can I help you ?",
              "Hi admin how are you ? "]

cmd_Leave = ["bye",
             "go and sleep",
             "sleep"]
rply_Leave = ["Ok admin Bye",
              "Nice meeting you. Bye",
              "Have greate day admin Bye",
              "Meet you soon admin Bye",
              "Take Care of yourself admin Bye",
              "Hope I Help you very well. Bye"]

cmd_Angry = ["angry",
             "irritated",
             "annoyed",
             "mad",
             "frustrated"]
rply_Angry = ["Dear admin Take your headphone out and listen some music. this may help you to calm down",
              "Dear admin Talk with your best friend this will surely make you calm",
              "Dear admin why You always become angry on small incident",
              "Dear admin What's the problem with you ? you have to learn that becoming angry is not the solution !"]

cmd_Sad = ["bad",
           "sad",
           "not feeling well",
           "unhappy",
           "depressed",
           ]
rply_Sad = ["admin to feel ypu i have solution. sleep now ",
            "admin talk to with your best friend this will absolutely make you happy",
            "admin take a hot water bath and this makes you relax",
            "admin simply shut down the laptop and take a small nap"]

cmd_Happy = ["happy",
             "good",
             "joyful",
             "calm",
             "greate",
             "amazing",
             "awesome"]
rply_Happy = ["OHHH admin sound greate",
              "OHHH admin sound good. you have to share the reason of your happiness with your best friend this make a memory moment",
              "OHHH admin glad to hear that you are happy"]

cmd_Bored = ["bor",
             "bored",
             "bore",
             "nothing to do"]
rply_Bored = ["Watch some stand up comedy video",
              "Install a new game but don't addict to it",
              "Install Momix or pikashow and watch some new series or short movies",
              "Install Discovery plus and watch some adventurous shows",
              "Take a small nap",
              "Check out some amazing small coding tips",
              "Check out google widget list"]

cmd_mor = ["good morning",
           "morning"]
rply_mor = ["Good Morning Admin",
            "Good morning What are you doing up so early?",
            "Morning! Can't wait to see you later",
            "Hey cutie",
            "Good morning handsome"]

cmd_aft = ["good Afternoon",
           "afternoon"]
rply_aft = ["Good Afternoon admin",
            "Good Afternoon, So what are you doing now ?"]

cmd_ngt = ["good night",
           "night"]
rply_ngt = ["Good Night admin",
            "Good Night admin, before you go to sleep shutdown the system",
            "Good Night admin, to make me sleep say exit"]

def chatingBot(text):
    for word in text.split():
        if word in cmd_Bored:
            prt = random.choice(rply_Bored)
            print(prt.title())
            return prt
        elif word in cmd_mor:
            prt = random.choice(rply_mor)
            print(prt.title())
            return prt
        elif word in cmd_aft:
            prt = random.choice(rply_aft)
            print(prt.title())
            return prt
        elif word in cmd_ngt:
            prt = random.choice(rply_ngt)
            print(prt.title())
            return prt
        elif word in cmd_Leave:
            prt = random.choice(rply_Leave)
            print(prt.title())
            return prt
        elif word in rply_Angry:
            prt = random.choice(rply_Angry)
            print(prt.title())
            return prt
        elif word in cmd_Sad:
            prt = random.choice(rply_Sad)
            print(prt.title())
            return prt
        elif word in cmd_Happy:
            prt = random.choice(rply_Happy)
            print(prt.title())
            return prt
        elif word in cmd_Greet:
            prt = random.choice(rply_Greet)
            print(prt.title())
            return prt


if __name__ == "__main__":

    while True:

        word = input("Enter Command : ").lower()
        chatingBot(word)

'''
After the code run enter the command the output will be display on the screen. 
For adding the new command and their reply 
    cmd_commandName = ["Your command"]
    rply_replyName =  ["Your reply"]
    then, in main method add
        elif word in cmd_commandName:
        prt = random.choice(rply_replyName)
        print(prt.title())
        return prt
'''
