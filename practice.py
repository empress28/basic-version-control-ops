# username=input('what is your name?:\n')
# print('you are welcome', username) 

# hours = int(input('how many hours did you work in a day?:\n')) 
# amount = int(input('how much do you earn per hour?:\n'))
# grosspay = hours*amount
# print('your daily grosspay', grosspay


def maximum(query):
    '''this function returns the maximum number in the list'''
    largest = None 
    for item in query:
        if largest is None or item > largest:
            largest = item
    return largest

tomi_list = [112, 34, -5, -34, 76, 7]
print('largest value in tomi\'s list;',maximum(tomi_list))

# count = 0

# while count < 10:
#     print("count is", count)
#     count += 1