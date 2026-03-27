class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = []

        for token in tokens:
            match token:
                case "*":
                    first = int(operators.pop())
                    second = int(operators.pop())
                    operators.append(second*first)
                case "/":
                    first = int(operators.pop())
                    second = int(operators.pop())
                    operators.append(second/first)
                case "+":
                    first = int(operators.pop())
                    second = int(operators.pop())
                    operators.append(second+first)
                case "-":
                    first = int(operators.pop())
                    second = int(operators.pop())
                    operators.append(second-first)
                    
                case _:
                    operators.append(token)
        
        return int(operators[-1])
