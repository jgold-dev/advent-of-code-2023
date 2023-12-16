
rownums = []
    
with open('puzzle1_input.txt') as fh:

    for line in fh:
        line = str.strip(line)
        digits = []
        for i in line:
            if i.isdigit():
                digits.append(int(i))
        rownums.append(10*digits[0] + digits[len(digits) -1])
        
    print("Sum:", sum(rownums))
