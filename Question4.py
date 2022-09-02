it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("length of set it_companies", (len(it_companies)))
# add twitter to the it_companies
it_companies.add("Twitter")
# To add set of companies in it_companies
print("it_companies are: ", it_companies)
companies = {'Alphabet', 'Intel', 'Netflix'}
it_companies.update(companies)
print("Updated it_companies are: ", it_companies)
it_companies.remove("Alphabet")  # Removing the company Alphabet from the it_companies list
print("Updated list: ", it_companies)

# Remove vs Discard:
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
print("A union B is: ", A.union(B))  # prints the set A union B
print("Intersection of A and B is: ", A.intersection(B))  # prints the intersection of A and B
print("Is A subset of B: ", A.issubset(B))  # Checking whether A is subset of B
print("Are A and B disjoint sets: ", A.isdisjoint(B))  # checking whether A and B are disjoint sets
# Joining A with B and B with A -
print("joining B with A", B.union(A))
print("joining A with B", A.union(B))
# The symmetric difference between A and B -
print("symmetric difference between A and B", A.symmetric_difference(B))
print(A.clear())  # deleting the set A completely
print(B.clear())  # deleting the set B completely
# Converting the ages to a set and comparing the length of the list and the set - age_set = set(age)
print("set of ages:", set(age))  # creating set of ages
print("length of set of list is: ", len(set(age)))
print("length of set is :", len(age))
print("Maximum of list and set is: ", max(len(age), len(set(age))))
