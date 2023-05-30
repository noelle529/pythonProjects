#number sorter
numList = []
num = []
def listSorter():
    sumList = sum(numList)
    print('The sum the of this list is:  '+ str(sumList))

    avgList = sum(numList) / len(numList)
    print('The average of this list is:  '+ str(avgList))

    maxList = max(numList)
    print('The max number is: ' + str(maxList))

    minList = min(numList)
    print('The smallest number is: ' + str(minList))

    removeDuplicates = list(set(numList))
    print('No repeats: ' + str(removeDuplicates))

try:
    while True:
        num = input("Enter a number (or 'done' to stop): ")
        numList.append(float(num))
        if num == 'done':
            print('see you later!')
        listSorter()

except ValueError:
	print("Invalid input. Please enter a valid number or 'done'.")

