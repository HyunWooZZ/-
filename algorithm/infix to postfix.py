class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

## 스택이 비어있는 경우 , 스택이 비어있지 않고(스택의 위에 우선순위가 낮은 게 있는 경우, 우선순위가 같거나 높은 경우) ")"를 만난 경우

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for string in S: 
        if string in prec or string == ")": # 연산자를 만났을 때
            if opStack.size() == 0 or string == "(": ### 스택이 비어 있는 경우
                opStack.push(string)
                
            
            elif string == ")":
                temp = opStack.pop()
                while temp != "(":
                    answer += temp
                    temp = opStack.pop()
                
            elif prec[opStack.peek()] > prec[string]: #스택 위의 연산자가 우선 순위가 높은 경우
                # 스택에서 가장높은 연산자가 내가 추가하려는 연산자의 우선순위보다 낮을때까지 꺼낸다.
                temp = opStack.peek()
                while prec[temp] > prec[string]:
                    temp = opStack.pop()
                    
                    if opStack.size() == 0: ### 더이상 꺼낼게 없는 경우는 멈춘다.
                        answer += temp
                        opStack.push(string)
                        break
                    else: ### 그렇지 않다면 우선순위가 낮은 것을 뽑을 때까지 멈추지 않는다.
                        answer += temp
                else: # 우선순위가 이제 더 낮다면 스택에 추가해 주자.
                    opStack.push(string)
            
            elif prec[opStack.peek()] == prec[string]:
                temp = opStack.peek()
                answer += temp
                    
            else: # # 스택위의 연산자가 우선순위가 낮은 경우
                opStack.push(string) # 그냥 스택위에 추가
                    
            
                
        else: ### 숫자를 만난 경우
            answer += string
    else:
        while opStack.size() != 0:
            answer += opStack.pop()
            
    
    return answer


"""
후위 식 연산 
"""


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)
        
        elif token == "(":
            opStack.push(token)
            
        elif token == ")":
            while opStack.peek() != "(":
                postfixList.append(opStack.pop())
            
            else:
                opStack.pop()  # 남아 있는 "(" 지우기 

        else: # 연산자를 만났을 경우
            if opStack.isEmpty(): # 스택이 비어 있는 경우
                opStack.push(token)
            
            elif prec[opStack.peek()] >= prec[token]: # 스택 가장 위에 있는 연산자 보다 연산자 우선순위가 낮은 경우
                while  not opStack.Empty() and prec[opStack.peek()] >= prec[token]: #### 반드시 비어있는지 먼저 확인 해야함. 여기서 런타임 오류 났음.
                    postfixList.append(opStack.pop())
                
                else: ## while문 끝나고 마지막으로 넣어줘야함
                    opStack.push(token)
                
            else: # 스택보다 연산자 우선순위가 높은 경우 
                opStack.push(token)
        
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
        
    return postfixList
                

def postfixEval(tokenList):
    stack = ArrayStack()
    
    for token in tokenList:
        if type(token) is int:
            stack.push(token)
        
        else:
            second = stack.pop()
            first = stack.pop()
            
            if token == "*":
                value = first * second
            
            elif token == "/":
                value = first / second
            
            elif token == "-":
                value = first - second
            
            elif token == "+":
                value = first + second
            
            stack.push(value)
            
    return stack.pop()
            

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

print(solution("(1 + 2 * (3 + 10)"))