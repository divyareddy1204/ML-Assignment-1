weights = []  # creating a list called weights
N = int(input("Enter number of students "))  # taking the input
for i in range(N):
    weights.append(int(input("Enter the weight of the student  " + str(i + 1) + " :")))
KGs = []  # creating a list KGs
for i in weights:
    KGs.append(float(i / 2.2086))  # converting pounds to kilograms
print("converted list: ", KGs)  # printing the converted list
