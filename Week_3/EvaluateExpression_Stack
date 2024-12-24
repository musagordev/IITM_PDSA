#Function takes unique string like 'A + B'. It returns result of mathematical operation A+B.
#Function detects integers, operations and show the results.
#It is example of stack data structure

def EvaluateExpression(exp):
    if len(exp) < 2:
        return exp[0]
    def executive_operators(ope, num_1, num_2):
        if ope == '+':
            return num_1 + num_2
        if ope == '-':
            return num_1 - num_2
        if ope == '*':
            return (num_1) * (num_2)
        if ope == '/':
            return num_1 / num_2
        if ope == '**':
            return num_1 ** num_2
    ope = ['+','-','*','/','**']
    nums = ['0','1','2','3','4','5','6','7','8','9']
    executive_ope = None
    el_num =[]
    current_num = None
    for element in exp+' ':
        
        if element == ' ':
            if current_num != None:
                el_num.append(current_num)
                current_num = None
            if executive_ope != None:
              if len(el_num) < 2:
                return el_num[0]
              else:
                num_2 = float(el_num.pop())
                num_1 = float(el_num.pop())
                new_num = executive_operators(executive_ope,num_1,num_2)
                executive_ope = None
                el_num.append(new_num)
            else:
                pass
        elif element in ope and executive_ope == None:
            executive_ope = element
        elif element in ope and executive_ope == '*':
            executive_ope = '**'
        elif element in nums and executive_ope == '-':
            current_num = f'-{element}'
        elif element in nums:
            if current_num == None:
                current_num = element
            else:
                current_num = current_num + element
    return(float(el_num[0]))

print(float(EvaluateExpression(input())))
