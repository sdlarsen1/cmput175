
# reads the contents of the file and returns a list of lines
def read_numbers(filename):
    infile = open(filename)
    data = infile.readlines()
    return data

# takes a number in a free format and returns the standard form xxx-xxx-xxxx
def standardize(phone_number):
    phone_number = phone_number.strip()
    for x in phone_number:
        if x != '-' and x.isdigit() == False:
            phone_number = phone_number.replace(x, key_map[x])
        else:
            continue
    return phone_number

# takes a phone number in the standard form and returns the sum of its digits
def sum_of_digits(phone_number):
    digits = []
    for x in phone_number:
        if x != '-':
            digits.append(int(x))
    return sum(digits)
    
# takes a list of phone numbers and returns the highest sum of digits
def find_highest_sum(phone_list):
    sums = []
    for number in phone_list:
        digits = []
        for x in number:
            if x != '-':
                digits.append(int(x))
        sums.append(sum(digits))
    return max(sums)

key_map = {'A':'2', 'B':'2', 'C':'2',
           'D':'3', 'E':'3', 'F':'3',
           'G':'4', 'H':'4', 'I':'4',
           'J':'5', 'K':'5', 'L':'5',
           'M':'6', 'N':'6', 'O':'6',
           'P':'7', 'Q':'7', 'R':'7', 'S':'7',
           'T':'8', 'U':'8', 'V':'8',
           'W':'9', 'X':'9', 'Y':'9', 'Z':'9',
           }

# main program

phone_list = read_numbers("phones.txt")

phone_list = [ standardize(x) for x in phone_list ]
  
highest_sum = find_highest_sum(phone_list)

for number in phone_list:
    if sum_of_digits(number) == highest_sum:
        print(number, '*')
    else:
        print(number)

