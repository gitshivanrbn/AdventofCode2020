

def main():
    with open('Day2/input_day2.txt','r') as f:
        lines = f.readlines()
   
    invalid_count = 0

    for line in lines:
        stripped_line = line.strip()
        no_spaces = stripped_line.strip()

        #split line into policy and passcode
        fields = no_spaces.split(':')
        #get the policy
        line_policy = fields[0]

        #get the first number
        number1 = int(line_policy.split('-')[0])
        #get the second number and the policy letter
        number2_with_letter = line_policy.split('-')[1]
        #get the second number
        number2 = int(number2_with_letter.split()[0])

        #get the policy letter 
        letter = number2_with_letter.split()[1]

        code_with_space = fields[1]
        code = code_with_space.lstrip()
        print(code)
        if (code[number1 - 1] == letter and code[number2 - 1] != letter) or (code[number1 - 1] != letter and code[number2 - 1] == letter):
            invalid_count += 1


    print(invalid_count)
    
if __name__ == "__main__":
    main()    
