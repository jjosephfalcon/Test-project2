
# # # Create a function that takes one parameter: a list of elements. 
# # # Function should loop through the list and check if there is a string in the list. 



 


# # # example of checking if an element is a string. 
# # # a = 100
# # # b = "word"
# # # type(a) == str --> False
# # # type(b) == str --> True

# # # If the list parameter does not have any strings in it, we return False.
# # # If the list has any strings in it, return True. 



# # # I'll define the function name and parameter to get going. 


# # list1 = [1, 2, 3, 4, 5, "magic", 7, 8]

# # list2 = [6,7,8,9]

# # list3 = [2,3,4,5,6, "world", 99]


  
# # def hasStrings(someList):
# #   for i in someList:
# #     if type(i) == str:
# #       return True
# #   # Outside the loop, if the loop finished and no True was returned, we return False
# #   return False


# # print(hasStrings(list1))
# # print(hasStrings(list2))
# # print(hasStrings(list3))



# # # Print the types of each variable 

# # var1 = 100
# # var2 = False 
# # var3 = "word"
# # # --------
# # print("var1:", type(var1)) # ---> int
# # print("var2:", type(var2)) # ---> bool 
# # print("var3:", type(var3)) # ---> str

# # # Write a if statement to check if var1 is a int:
# # if type(var1) == int:
# #   print("var1 is an int")
# # else:
# #   print("var1 is not an int")

# # # Write a if statement to check is var2 is a bool.
# # if type(var2) == bool:
# #   print("var2 is a boolean")
# # else:
# #   print("var2 is not a boolean")

# # #----------------------------------------------------------------------#

# # mixed = [100, "world", False, "hello", 923, "world", 12,False, "cat", "hotdog", "another", "key", 23, "bat", "lion", 232,True]

# # # Loop through the mixed list and print the data type of each element. 

# # str_list = []
# # int_list = []
# # bool_list = []


# # for i in mixed:
# #   if type(i) == int:
# #     int_list.append(i)
# #   elif type(i) == str:
# #     str_list.append(i)
# #   elif type(i) == bool:
# #     bool_list.append(i)

# # print(int_list)
# # print(str_list)
# # print(bool_list)


# # # ----------
# # # Complete the function so that it prints "a Boolean was found" if there is a bool in the list parameter.
# # def hasBool(someList):
# #   for i in mixed:
# #     if type(i) == bool:
# #       return "A Boolean was found"
  
# #   return False
    
  
    












# # # Loop through chars list and check if the character is a Naruto anime character. If it is, print the name + " is a character from the Naruto anime!" else print name + " is not from Naruto"

# # chars = ["vegeta", "sasuke", "itachi", "goku", "kakashi", "blitz", "kenpachi", "thorfell"]







# # for i in chars:
# #   if i == "sasuke":
# #     print(i + " is a character from the Naruto anime!")
# #   elif i == "itachi":
# #     print(i + " is a character from the Naruto anime!")
# #   elif i == "kakashi":
# #     print(i + " is a character from the Naruto anime!")
# #   else:
# #     print(i + " is not from Naruto.")

   

# # HomeWork: 
# # Here we have a list of characters from Haikyu!
# haikyu = ["shoyo", "kenma", "tobio", "toru", "yu", "tetsuro", "kei", "kiyoko", "kotaro", "daichi", "koshi", "ryunosuke"]

# # Here are the three lists we will test using our hasHaikyu function to see if any characters from the haikyu list are in the list parameter.
# char_list1 = ["naruto", "jiraya", "minato", "toru", "krillin", "master roshi"]
# char_list2 = ["goku", "bulma", "vegeta", "trunks", "gohan", "chichi"]
# char_list3 = ["ichigo", "kenpachi", "aizen", "tetsuro", "kotaro"]
# # Hints: Use the 'in' operator to check if a element exists inside of haikyu.
# # Example if "shoyo" in haikyu:


# # Complete the function below: 
 
# def hasHaikyu(someList):
#   for i in someList:
#     if i in haikyu:
#       return True
#   # When the loop is done and it never returned True, then we return false. (Outside the loop)
#   return False

#   # if "toru" in char_list1 and char_list2 and char_list3:
#   #   print("toru is in the list parameter")
  

 


# print(hasHaikyu(char_list3))


# # Lets make a function that takes a list as a parameter, and loops through that list to print each element. 

# def printAll(someList):
#   for i in someList:
#     print(i)

# # Use the printAll function to print from char_lists (1,2 and 3)



# printAll(char_list1)
# printAll(char_list2)
# printAll(char_list3)


# # Define the function (make it first, so you can use it later)
# def addTwo(a, b):
#   return a + b 

# # Execute the function, and provide two parameters as we defined in our function above
# print(addTwo(12, 14))
# print(addTwo(23, 23))
# print(addTwo(101, 201))
# print(addTwo(9, 9))






 
                           
 
# _----^----___________------^--_     
#[-----------------------------)]= 
# -________-----------_________-__     
#   /     / \\  |     |           |--
#  /     /______|     |___________|--
#  |     |
#  |     |
#   -----


def greeting(whatYouWantToSay):
  print(whatYouWantToSay)


 

test1 = "hello"
test2 = "This is literally printing whatever I say? MIND BLOWN to SMITHEREANS! SOMEONE CALL AN AMBERLAMPS!"
test3 = "hi"
test4 = "I think my names is kemal...maybes"

# Whenever we repeat a name of a variable Python will pick the last one you mentioned.

test4 = """ 


 _----^----___________------^--_     
[-----------------------------)]= 
 -________-----------_________-__     
   /     / \\  |     |           |--
  /     /______|     |___________|--
  |     |
  |     |
   -----
   
   """
#test4 = "(+.[   ]::)"
#test4 = "\(^_^)/"
#test4 = "\(-_-)/"

# ---- PRINT BELOW THIS LINE ------

# greeting(test4) 



# Write a function that doesn't have any parameters

def example():
  print("I am the example, and I dont need any parameters!")


# Write a function that takes a string and prints after saying "here is your string: "

def example2(someStr):
  print("Here is your string: " + someStr)






coolStr = """
─────────▀▀▀▀▀▀──────────▀▀▀▀▀▀▀
──────▀▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀▀▀▀▀▀▀
────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────▀▀▀
───▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────────▀▀
──▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀─────▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀───▀▀▀▀▀▀▀▀──────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
──▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀
───▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀▀
─────▀▀▀▀▀▀▀▀▀▀▀▀▀───────────────▀▀▀
──────▀▀▀▀▀▀▀▀▀▀▀───▀▀▀────────▀▀▀
────────▀▀▀▀▀▀▀▀▀──▀▀▀▀▀────▀▀▀▀
───────────▀▀▀▀▀▀───▀▀▀───▀▀▀▀
─────────────▀▀▀▀▀─────▀▀▀▀
────────────────▀▀▀──▀▀▀▀
──────────────────▀▀▀▀
───────────────────▀▀

"""

coolStr2 = """
..... (¯`v´¯)♥
.......•.¸.•´
....¸.•´
... (
☻/
/▌♥♥
/ \ ♥♥

"""

coolStr3 = "( ͡🔥 ͜ʖ ͡🔥)"

coolStr4 = """
..(\ /)
..(•.•)  
c(")(“) 
"""

coolStr4 ="""
░░░░░███████ ]▄▄▄▄▄▄▄▄
▂▄▅█████████▅▄▃▂              ☻
███████████████████].       / ▌\╦─  
@@@@@@@@@@@@@@@@@@@         /  \     
"""
 
coolStr5 = """
╭━━━━━━━━━━━━━━
┃　　● ══　     ┃
┃██████████████┃
┃██████████████┃
┃██████████████┃
┃██████████████┃
┃██████████████┃
┃██████████████┃
┃██████████████┃
┃██████████████┃
┃　　 　O　  　  ┃
╰━━━━━━━━━━━━━━
"""
 

obamo = """
░░█▀░░░░░░░░░░░▀▀███████░░░░ 
░░█▌░░░░░░░░░░░░░░░▀██████░░░ 
░█▌░░░░░░░░░░░░░░░░███████▌░░ 
░█░░░░░░░░░░░░░░░░░████████░░ 
▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ 
░▌▄███▌░░░░▀████▄░░░░▀████▌░░ 
▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ 
▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ 
▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ 
▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ 
░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ 
░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ 
░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ 
░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ 
░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ 
░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ 
░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ 
░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ 
░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ 
▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ 
░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ 
░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ 
░░▄▌████████▄▄▄███████▌░░░░░▄ 
░▄▀░██████████████████▌▀▄░░░░ 
▀░░░█████▀▀░░░▀███████░░░▀▄░░ 
░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ 
░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ 
░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ 
░╔╗║░╔═╗░═╦═░░░░░╔╗░░╔═╗░╦═╗░ 
░║║║░║░║░░║░░░░░░╠╩╗░╠═╣░║░║░ 
░║╚╝░╚═╝░░║░░░░░░╚═╝░║░║░╩═╝░ 
"""

monkey = """
... ... ... ... ... ... ... ... ... ... ... ... ... ...|... ... ... ... ... ... ... ... .._,,-~~~-,-,,_ 
... ... ... ... ... ... ... ... ... ... ... ... ... ...|... ... ... ,,---,,_... ...,-~",-":__-,: : :"-,:::"'~,, 
.,,-~~--,, ... ... ... ... ... ... ... ... ... ... ...|... ... ,~": : --,,:"~,,-"::::/:,-". . ."'~-,,: \,::::_,,"~-,,
/: : : : : : :"'~-,,... ... ... ... ... ... ... ... ... |... ... /: : : : :~"'\,: \::__/:|o--,,. . . . .\,: ¯¯: : : : : :"-, 
\: : : : : : : : : : :""~,,... ... ... ... ... ... ... |... ... .\: : : : : :,,-"~": : : "'~~-,:"'~-,,_|: : :,-"¯¯¯¯"-,:| 
.'~,: : : : : : : : : : : : :"'~-,,_... ... ... ... ...|... ... .."-,_: ,-" : : : : : : : : : : : "~,--~": : (o~--,,_. . |:| 
... ."'~-,,: : : : : : : : : : : : :"-,~--,... ... ... |... ... ... ...,/: : : : : : ,,--,-,~-,,: : :"~-,,: : :"~,___:"-/,/__ 
... ... ...,"~"~--,,_,,-~"`"`": : "-,::"'~~--,,_..| ... ... ... ..|: : : ,: :,-". ,-"./. . . ."-,,_: : :"~-~": : : :"'-,,~,:"-,, 
... ... .,/: : : : --,,:|: : : : : : : : :"-,,::::::::::::"~--,,_... ... \: :  :|: /. .,/. . |. . . ,-".|. "~,,_____,,,,,__:\: : : : | 
... ... .|: : : : : : : "|: : : : : : :,: : : :\:::::::::::::::::::::"'~~-,,"-,:|: |. /. . . .|. .,-". . |. ,-"'. \. . .,/|. . . .",:\: : ,/ 
... ... ..\, : : : : : ,/ : : : : : :  :|: : : ,/::::::::::::::::::::::::::::::::::"\: "-,,___,\,/___,,\/___. |,-". |. . . ,/.|: |,~" 
... ... ... ",-,,,__/: : : : : : :,/,_~"-::::::::::::::::::::::::::::::::… : : : : : : : : : "'~,,,/.,,~". ,/: / 
... ... ... /: : : : :"-,,___,,-": : ,"-,-:::::::::::::::::::::::::::::::::::… : : : : : : : : : : : : : : "-"__,-":,-" 
... ... ... '\,_: : : : : : /-,,___,,"~-----~~~~,~---,,__:::::::::::… : : : : : : : __,,--~"~,,___,,-" 
... ... ... ... ."'~---~"... ... ... ... ... ... ...|---~"::::"'~-::::::::::::::::,/: : : : : : : : : :\"~,, 
... ... ... ... ... ... ... ... ... ... ... ... ... .|::::::::::::::::::::::::::::,,": : : : : : : : : : : |:::::"-,, 
... ... ... ... ... ... ... ... ... ... ... ... ... .|:::::::::::::::::::::::,,-": : : : : : : : : : : : :,|:::::::::"-, 
... ... ... ... ... ... ... ... ... ... ... ... ... .|::::::::::_,,,--~~": : : : : : : : : : : : : : :,/::::::::::::::\, 
... ... ... ... ... ... ... ... ... ... ... ... ... .|----~~" : : : : : : : : : : : : : : : : : : : :,/::::::::::::::::::\, 
... ... ... ... ... ... ... ... ... ... ... ... ... .|: : : : : : : : : : : : : : : : : : : : : : :,-,"::::::::::::::::::::::\ 
... ... ... ... ... ... ... ... ... ... ... ... ... |: : : : : : : : : : : : : : : : : : : _,,~"SL'\,::::::::::::::::::::::\ 
... ... ... ... ... ... ... ... ... ... ... ... ... |: : : : : : : : : : : : : : : : :,,-"... ... ... .\:::::::::::::::::::::::\ 
... ... ... ... ... ... ... ... ... ... ... ... ... |: : : : : : : : : : : :_,,--~"... ... ... ... ...\:::::::::::::::::::::::\
"""

hand = """
...............,´¯­­`,
.........,´¯`,....­­/
....../¯/.../..../
..../../.../..../­­..,-----,
../../.../....//­­´...........`.
./../.../..../­­......../´¯\....\
('.('..('....('....­­...|.....'._.'
.\.................­­...`\.../´...)
...\...............­­......V...../
.....\.............­­............/
.......`•............­­.......•´
..........|.........­­........|
..........▓▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▓
..........▓▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▓
"""

sword = """
    ———————-//\\
    ———————// ¤ \\
    ———————\\ ¤ //
    ———————- \\//
    ——————– (___)
    ———————(___)
    ———————(___)
    ———————(___)_________
——–\_____/\__/—-\__/\_____/
————\ _°_[————]_ _° /
—————-\_°_¤ —- ¤_°_/
——————–\ __°__ /
———————|\_°_/|
———————[|\_/|]
———————[|[¤]|]
———————[|;¤;|]
———————[;;¤;;]
——————–;;;;¤]|]\
——————-;;;;;¤]|]-\
——————;;;;;[¤]|]–\
—————–;;;;;|[¤]|]—\
—————-;;;;;[|[¤]|]|—|
—————;;;;;[|[¤]|]|—|
—————-;;;;[|[¤]|/—/
—————–;;;[|[¤]/—/
——————;;[|[¤/—/
——————-;[|[/—/
——————–[|/—/
———————/—/
——————–/—/|]
——————-/—/]|];
——————/—/¤]|];;
—————–|—|[¤]|];;;
—————–|—|[¤]|];;;
——————\–|[¤]|];;
——————-\-|[¤]|];
———————\|[¤]|]
———————-\\¤//
———————–\|/
————————V
"""
example2(sword)










