def main():
    with open("input01.txt", "r") as f:
        data = f.read().splitlines()
    
    answer = 0
    
    numbers = ['one','two','three','four','five','six','seven','eight','nine']
    for line in data:
        
        # Creating a new line with only numbers by concatenating
        # numbers to new one as they come up in the data
        # Skipped in part 1 
        fixed_line = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                fixed_line += line[i]
            else:
                # Checking if the line start with any written number at the current index
                for n in range(len(numbers)):
                    try:
                        if (line[i:].startswith(numbers[n])):
                            fixed_line += str(n+1)
                            break
                    except:
                        pass
        line = fixed_line

        # Finding the first digit
        for i in range(len(line)):
            if line[i].isnumeric():
                first = line[i]
                break
            
        # Finding the last digit
        for i in range(1,len(line)+1):
            if line[-i].isnumeric():
                last = line[-i]
                break
        
        number = int(first+last)
        answer += number    
    print(answer)

if __name__ == "__main__":
    main()