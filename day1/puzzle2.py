
rownums = []

numbers = ["one","two","three","four","five","six","seven","eight","nine"]

def get_str_nums(line, hash, num_index:int, start_index = 0):
    x = line.find(numbers[num_index], start_index)
    if (x >= 0):
        hash[x] = num_index + 1
        get_str_nums(line, hash, num_index, x + len(numbers[num_index]))

    
with open('puzzle_input.txt') as fh:

    for line in fh:
        line = str.strip(line)

        # hash of all digits, by index
        digits = {}

        for str_num_index in range(len(numbers)):
            get_str_nums(line, digits, str_num_index, 0)

        for i in range(len(line)):
            if line[i].isdigit():
                digits[i] = (int(line[i]))

        # Combine numbers and add to array
        rownums.append(10*digits[min(digits.keys())] + digits[max(digits.keys())])
        
    print("Sum:", sum(rownums))
