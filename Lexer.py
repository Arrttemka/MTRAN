class Lexer:
    def __init__(self, code, pos=0, token_list=[]):
        self.code = code
        self.pos = pos
        self.token_list = token_list
        self.text = code

    def check_brackets(self):
        stack = []
        position_stack = [] 

        for i, char in enumerate(self.text):
            if char == '(':
                stack.append(char)
                position_stack.append(i) 
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    position_stack.pop() 
                else:
                    return False, i 
        if stack:
            return False, position_stack[-1]  

        return True, -1 



