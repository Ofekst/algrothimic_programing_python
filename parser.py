import re
from abc import ABC,abstractmethod

class Expression(ABC):
    @abstractmethod
    def calc(self)->float:
        pass

# implement the classes here
class Num(Expression):
    x = 0
    def __init__(self, number) -> None:
        self.x = number

    def calc(self) -> float:
        return self.x

class BinExp(Expression):

    def __init__(self, left:Num ,right:Num) -> None:
        self.left: Num = left
        self.right: Num = right

    @abstractmethod
    def calc(self) -> float:
        pass

class Plus(BinExp):
    def calc(self) -> float:
        return self.left.calc() + self.right.calc()

class Minus(BinExp):
    def calc(self) -> float:
        return self.left.calc() - self.right.calc()

class Mul(BinExp):
    def calc(self) -> float:
        return self.left.calc() * self.right.calc()

class Div(BinExp):
    def calc(self) -> float:
        return self.left.calc() / self.right.calc()


#Helper functions
def op_priority(op) -> int:
    """
    Return the priority level of a mathematical operator
    or 0 if it does not exist.

    :param op: Character string representing an operator
    :return:
            int: The priority level of the operator
            or 0 if it does not exist.
    """
    priorities = {'+': 1, '-': 1, '*': 2, '/': 2}
    return priorities.get(op, 0)

def create_bin_exp(op, left, right) -> BinExp:
    """
    Creates a binary expression node based on the given operator and operands.
    :param op: A string representing the binary operator
    :param left: The left operand
    :param right: The right operand
    :return: An instance of the binary expression class ,
    or None if the operator is not recognized.
    """
    if op == '+':
        return Plus(left, right)
    elif op == '-':
        return Minus(left, right)
    elif op == '*':
        return Mul(left, right)
    elif op == '/':
        return Div(left, right)
    return None

def is_float_number(token:str) -> bool:
    """
    Checks if the given token is a number.
    :param token: String representing a number.
    :return: True if the given token is a number.
    """
    try:
        float(token)
        return True
    except ValueError:
        return False


def tokenize_expression(expression:str) -> list:
    """
    Tokenizes a mathematical expression string, properly handling negative numbers.
    If a minus sign represents a negative number, it merges it with the number token.

    Parameters:
        expression: A string representing a mathematical expression.

    Returns:
        List[str]: A list of tokens, with negative numbers correctly formed.
    """
    token_pattern = re.compile(r'(?:\d+\.\d+|\d+)|\+|\-|\*|\/|\(|\)')
    tokens = token_pattern.findall(expression)

    passed_tokens = []
    skip = False
    for i, token in enumerate(tokens):
        # In order to check for negative numbers
        if token == '-' and (i == 0 or tokens[i - 1] in '+-*/('):
            passed_tokens.append('-' + tokens[i + 1])
            skip = True
        elif skip:
            skip = False
        else:
            passed_tokens.append(token)

    return passed_tokens

#implement the parser function here
def parser(expression) -> float:

    output_queue = []
    operator_stack = []
    tokens = tokenize_expression(expression)

    for token in tokens:
        if is_float_number(token):
            output_queue.append(Num(int(token)))
        elif token in ['+', '-', '*', '/']:
            while (operator_stack and operator_stack[-1] != '('
                   and op_priority(operator_stack[-1]) >= op_priority(token)):
                op = operator_stack.pop()
                right = output_queue.pop()
                left = output_queue.pop()
                output_queue.append(create_bin_exp(op, left, right))
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                op = operator_stack.pop()
                right = output_queue.pop()
                left = output_queue.pop()
                output_queue.append(create_bin_exp(op, left, right))
            operator_stack.pop()  # Pop the '(' from the stack

    while operator_stack:
        op = operator_stack.pop()
        right = output_queue.pop()
        left = output_queue.pop()
        output_queue.append(create_bin_exp(op, left, right))

    if len(output_queue) != 1:
        raise ValueError("Invalid expression")

    return output_queue[0].calc()