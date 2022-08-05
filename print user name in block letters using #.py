#code to print user name in block letters using # (5x6 grid)

name = input("Enter The Name: ")
print(name)

length = len(name)


for i in range(0, length):
	a = name[i]
	a = a.upper()
	
	if (a == "A"):
		print("######\n#    #\n######", end = " ")
		print("\n#    #\n#    #\n\n")
		
	elif (a == "B"):
		print("######\n#    #\n#####", end = " ")
		print("\n#    #\n######\n\n")
		
	elif (a == "C"):
		print("######\n#      \n#      ", end = " ")
		print("\n#     \n######  \n\n")
		
	elif (a == "D"):
		print("##### \n#    #\n#    #", end = " ")
		print("\n#    #\n##### \n\n")
		
	elif (a == "E"):
		print("######\n#       \n##### ", end = " ")
		print("\n#      \n######\n\n")
		
	elif (a == "F"):
		print("######\n#     \n##### ", end = " ")
		print("\n#     \n#     \n\n")
		
	elif (a == "G"):
		print("######\n#     \n# ####", end = " ")
		print("\n#    #\n###### \n\n")
		
	elif (a == "H"):
		print("#    #\n#    #\n######", end = " ")
		print("\n#    #\n#    #\n\n")
		
	elif (a == "I"):
		print("######\n  ##  \n  ##  ", end = " ")
		print("\n  ##  \n######\n\n")
		
	elif (a == "J"):
		print("######\n  ##  \n  ##  ", end = " ")
		print("\n# ##  \n####  \n\n")
		
	elif (a == "K"):
		print("#   # \n#  #  \n##    ", end = " ")
		print("\n#  #  \n#   # \n\n")
		
	elif (a == "L"):
		print("#     \n#     \n#     ", end = " ")
		print("\n##    \n######\n\n")
		
	elif (a == "M"):
		print("#    #\n##  ##\n# ## #", end = " ")
		print("\n#    #\n#    #\n\n")
		
	elif (a == "N"):
		print("#    #\n##   #\n# #  #", end = " ")
		print("\n#  # #\n#   ##\n\n")
		
	elif (a == "O"):
		print("######\n#    #\n#    #", end = " ")
		print("\n#    #\n######\n\n")
		
	elif (a == "P"):
		print("######\n#    #\n######", end = " ")
		print("\n#     \n#     \n\n")
		
	elif (a == "Q"):
		print("######\n#    #\n# #  #", end = " ")
		print("\n#  # # \n######\n\n")
		
	elif (a == "R"):
		print("######\n#    #\n# ## ", end = " ")
		print("\n#   # \n#    #\n\n")
	
	elif (a == "S"):
		print("######\n#     \n######", end = " ")
		print("\n     #\n######\n\n")
		
	elif (a == "T"):
		print("######\n  ##  \n  ##  ", end = " ")
		print("\n  ##  \n  ##  \n\n")
		
	elif (a == "U"):
		print("#    #\n#    #\n#    #", end = " ")
		print("\n#    #\n######\n\n")
		
	elif (a == "V"):
		print("#    #\n#    #\n#    #", end = " ")
		print("\n #  # \n  ##  \n\n")
		
	elif (a == "W"):
		print("#    #\n#    #\n# ## #", end = " ")
		print("\n##  ##\n#    #\n\n")
		
	elif (a == "X"):
		print("#    #\n #  # \n  ##  ", end = " ")
		print("\n #  # \n#    #\n\n")
		
	elif (a == "Y"):
		print("#    #\n #  # \n  ##  ", end = " ")
		print("\n  ##  \n  ##  \n\n")
		
	elif (a == "Z"):
		print("######\n    # \n   #  ", end = " ")
		print("\n  #   \n######\n\n")
		
	elif (a == " "):
		print("       \n       \n       ", end = " ")
		print("\n       \n\n")
Exit = input("Press Enter To Exit.")
		
