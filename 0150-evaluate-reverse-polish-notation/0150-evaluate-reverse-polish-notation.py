class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    result = first + second
                elif token == '-':
                    result = first - second
                elif token == '*':
                    result = first * second
                elif token == '/':
                    result = int(float(first) / second)
                stack.append(result)
        return stack.pop()