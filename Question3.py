sisters = ("Deepthi", "Poojitha")  # tuple of sisters
brothers = ("Manohar", "Sumanth")  # tuple of brothers
siblings = sisters + brothers  # creating new tuple called siblings
print("Number of siblings: ", len(siblings))  # printing the total number of siblings
family_members = ("Srinivasulu", "Prameela")  # creating family members tuple
family_members += siblings  # adding family members and siblings tuple
print("family members are: ", family_members)

