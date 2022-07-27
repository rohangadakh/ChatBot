# ChatBot

This is the ChatBot.                                                                     
This code is totally based on the Python.                                                                     
                                                                     
for adding new commands and their reply follow these steps:                                                                     
                                                                    
    cmd_commandName = ["Your command"]                                                                     
    rply_replyName =  ["Your reply"]                                                                     
    # then, in main method add this elif statement                                                                    
    elif word in cmd_commandName:                                                                     
        prt = random.choice(rply_replyName)                                                                     
        print(prt.title())                                                                     
        return prt                                                                     
