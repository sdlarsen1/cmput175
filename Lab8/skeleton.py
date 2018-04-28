# sorts a list of numbers between 1 and n, using the counting sort algorithm
def counting_sort(lst, n):
    sorted_list = []
    max_val = n
    for y in range(len(lst)):
        value = y + 1
        for x in range(1,max_val+1):
            if value == x:
                for i in range(lst[y]):
                    sorted_list.append(x)
    #print(sorted_list)
    show(sorted_list)

# given a list of strings containing numbers, returns a list of numbers
def numerize(lst):
    biggest = int(lst[0])
    for x in range(len(lst)):
        if int(lst[x]) > biggest:
            biggest = int(lst[x])
    #print(biggest)
    
    count_list = []
    for y in range(1,biggest+1):
        count = 0
        for i in lst:
            if y == int(i):
                count += 1
        count_list.append(count)
    #print(count_list)
    counting_sort(count_list, biggest)

# prints a string containing the elements of a given list separated by spaces
def show(lst):
    string_list = []
    for x in lst:
        string_list.append(str(x))
    print(' '.join(string_list))

def main():
    max_num = 100
    infile = open('lists.txt', 'r')
    for line in infile:
        numlist = line.split()
        numerize(numlist)

if __name__=="__main__":
    main()
