def calculate_and_display_statistics(numbers):
    sum_list = sum(numbers)
    print('The sum of this list is: ' + str(sum_list))

    avg_list = sum(numbers) / len(numbers)
    print('The average of this list is: ' + str(avg_list))

    max_list = max(numbers)
    print('The maximum number is: ' + str(max_list))

    min_list = min(numbers)
    print('The smallest number is: ' + str(min_list))

    remove_duplicates = list(set(numbers))
    print('No repeats: ' + str(remove_duplicates))

def get_number_input():
    num_list = []

    while True:
        num = input("Enter a number (or 'done' to stop): ")
        if num == 'done':
            print('See you later!')
            break
        try:
            num_list.append(float(num))
        except ValueError:
            print('Invalid input! Please enter a number.')

    calculate_and_display_statistics(num_list)

get_number_input()
