def arithmetic_arranger(problems, show_answers=False):
    # to check how many problems in the list
    if len(problems) > 5 :
        return 'Error: Too many problems.'
    first_operand = []
    second_operand = []
    dashes = []
    results = []
    # to run every single index on the list
    for i in problems :
      #to split string then input it to the correct variable
        part = i.split()
        first, operator, second = part
      # make sure the operators are correct
        if operator not in ['+', '-'] :
            return "Error: Operator must be '+' or '-'."
        # make sure the strings are digits
        if first.isdigit() == False or second.isdigit() == False :
            return 'Error: Numbers must only contain digits.'
        #make sure the digits length not exceeding 4
        if len(first) > 4 or len(second) > 4 :
            return 'Error: Numbers cannot be more than four digits.'
        # decide max length
        width = max(len(first), len(second)) + 2
        # arranging the line
        first_operand.append(first.rjust(width))
        second_operand.append(operator + second.rjust(width-1))
        dashes.append('-' * width)
        # calculate the results if needed
        if show_answers :
            if operator == '+' :
                result = str(int(first) + int(second))
                results.append(result.rjust(width))
            elif operator == '-' :
                result = str(int(first) - int(second))
                results.append(result.rjust(width))
    # arranging the output
    arranged_problems = (
        '    '.join(first_operand) + '\n' +
        '    '.join(second_operand) + '\n' +
        '    '.join(dashes) 
    )
    # show results if asked
    if show_answers :
        arranged_problems += '\n' + '    '.join(results)
    return arranged_problems

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
