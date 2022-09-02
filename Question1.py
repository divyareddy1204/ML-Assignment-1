ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()  # sorting the ages array
print(ages)  # printing the sorted array ages
print("Maximum age is", max(ages))  # printing the maximum of ages
print("Minimum age is", min(ages))  # printing the minimum of ages
ages.append(max(ages))  # adding the maximum of ages to the ages array
ages.append(min(ages))  # adding the minimum of ages to the ages array
l = len(ages)
if l % 2 == 0:   # if the length of array ages is even, the median will be the average of middle 2 elements
    median1 = ages[l // 2]
    median2 = ages[l // 2 - 1]
    median = (median1 + median2) / 2
else:    # if the length of array ages is odd, the median is the middle element
    median = ages[l // 2]
print("Median age is", median)  # prints the median age
Sum_of_ages = sum(ages)  # adding all the elements in the array ages
average = Sum_of_ages / l  # calculating average by dividing Sum_of_ages by the length of array
print("Average age is", average)  # prints the average age
range1 = max(ages) - min(ages)  # finding the range of the list of numbers
print("Range of the list is", range1)  # prints the range of the array
