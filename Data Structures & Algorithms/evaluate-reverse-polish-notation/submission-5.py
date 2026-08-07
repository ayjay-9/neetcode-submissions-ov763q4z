class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack, result = [], 0
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                match tokens[i]:
                    case "+":
                        operand2 = stack.pop()
                        operand1 = stack.pop()
                        result = int(operand1) + int(operand2)
                        stack.append(result)
                    case "-":
                        operand2 = stack.pop()
                        operand1 = stack.pop()
                        result = int(operand1) - int(operand2)
                        stack.append(result)
                    case "*":
                        operand2 = stack.pop()
                        operand1 = stack.pop()
                        result = int(operand1) * int(operand2)
                        stack.append(result)
                    case "/":
                        operand2 = stack.pop()
                        operand1 = stack.pop()
                        result = int(operand1) / int(operand2)
                        stack.append(result)
                    case _:
                        pass
        return int(stack[-1])