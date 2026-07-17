class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            if token not in "+-*/":
                operands.append(int(token))
                continue
            if token == '+':
                operands[-2] = operands[-2] + operands[-1]
            elif token == '-':
                operands[-2] = operands[-2] - operands[-1]
            elif token == '*':
                operands[-2] = operands[-2] * operands[-1]
            elif token == '/':
                operands[-2] = int(operands[-2] / operands[-1])
            operands.pop()
        return operands[0]

