def evaluate_postfix(arr):
        stack = []

        for item in arr:
            # if the item is operator so pop the two numbers from the stack
            # then make the process and push the result instead of them
            if item == '+':
                stack.append(stack.pop() + stack.pop())
            elif item == '-':
                last, first = stack.pop(), stack.pop()
                stack.append(first - last)
            elif item == '*':
                stack.append(stack.pop() * stack.pop())
            elif item == '/':
                last, first = stack.pop(), stack.pop()
                stack.append(first // last)
            # if is a number push it to the stack
            else:
                stack.append(int(item))

                
        # because now we have just one value in the stack
        return stack[0]


print(evaluate_postfix(["2", "1", "+", "3", "*"]))

################################
# another solution using match
###############################

# def evaluate_postfix(arr):
#         stack = []
#
#         for item in arr:
#             # DO IT WITH match [switch in other languages]
#             match item:
#                 case '+':
#                     stack.append(stack.pop() + stack.pop())
#                 case '-': 
#                     last, first = stack.pop(), stack.pop()
#                     stack.append(first - last)
#                 case '*':
#                     stack.append(stack.pop() * stack.pop())
#                 case '/':
#                     last, first = stack.pop(), stack.pop()
#                     stack.append(first // last)
#                 # default case else
#                 case _:
#                     stack.append(int(item))
#
#         # because now we have just one value in the stack
#         return stack[0]


