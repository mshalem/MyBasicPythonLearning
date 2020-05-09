male = False
if male:
    print("you aare a male")
else:
    print("you are not a male")

###########################################
male = True
tall= True
if male or tall:
    print("you aare a male or tall or both")
else:
    print("you are neither a male nor tall")

###############################################
male = True
tall= True
if male and tall:
    print("you aare a male and tall")
else:
    print("you are either not male or tall or both")
    #####################################
male = True
tall= True
if male and tall:
    print("you aare a male and tall")
elif male and not(tall):
    print("you are a short male")
else:
    print("you are either not male or tall or both")
####################################################
male = True
tall= True
if male and tall:
    print("you aare a male and tall")
elif male and not(tall):
    print("you are a short male")
elif not(male) and tall:
    print("you are not a male but tall")
else:
    print("you are not a male and not tall")