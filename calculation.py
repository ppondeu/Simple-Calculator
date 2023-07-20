from collections import deque
from decimal import Decimal
def is_operator(ch):
    return ch in '^*/%+-'

def is_higher_precedence(op1, op2):
    precedence = {'^': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1}
    return precedence[op1] >= precedence[op2]

def tokenize_expression(expression):
    tokens = []
    current_token = ""
    if expression[0] == '-':
        expression = '0' + expression
    for idx, char in enumerate(expression):
        if char.isspace():
            continue

        if is_operator(char) or char in '()':
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        else:
            current_token += char

    if current_token:
        tokens.append(current_token)

    return tokens

def calculate(operand1, operand2, operator):
    if operator == '+':
        return Decimal(operand1) + Decimal(operand2)
    elif operator == '-':
        return Decimal(operand1) - Decimal(operand2)
    elif operator == '*':
        return Decimal(operand1) * Decimal(operand2)
    elif operator == '/':
        if Decimal(operand2) == 0:
            raise ZeroDivisionError
        return Decimal(operand1) / Decimal(operand2)
    elif operator == '%':
        if Decimal(operand2) == 0:
            raise ZeroDivisionError
        return Decimal(operand1) % Decimal(operand2)
    elif operator == '^':
        return Decimal(operand1) ** Decimal(operand2)
    else:
        raise ValueError
def infix_to_postfix(tokens):
    num_postfix = deque()
    op_postfix = deque()
    op_stack = []

    for token in tokens:
        if token.isalnum() or '.' in token:
            num_postfix.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while op_stack[-1] != '(':
                op_postfix.append(op_stack.pop())
                operand1 = num_postfix.pop()
                operand2 = num_postfix.pop()
                op = op_postfix.pop()
                result = calculate(operand2, operand1, op)
                # print(operand2, op, operand1, '=', result)
                num_postfix.append(str(result))
            op_stack.pop()
        else:
            while op_stack and op_stack[-1] != '(' and is_higher_precedence(op_stack[-1], token):
                op_postfix.append(op_stack.pop())
                operand1 = num_postfix.pop()
                operand2 = num_postfix.pop()
                op = op_postfix.pop()
                result = calculate(operand2, operand1, op)
                # print(operand2, op, operand1, '=', result)
                num_postfix.append(str(result))
            op_stack.append(token)
    
    while op_stack:
        operand1 = num_postfix.pop()
        operand2 = num_postfix.pop()
        op = op_stack.pop()
        # print(operand2, op, operand1, '=', calculate(operand2, operand1, op))
        num_postfix.append(Decimal(calculate(operand2, operand1, op)))
    return str(num_postfix.pop())
if __name__ == '__main__':
    expression = input('Enter infix expression: ')
    tokens = tokenize_expression(expression)
    print(tokens)
    print(infix_to_postfix(tokens))