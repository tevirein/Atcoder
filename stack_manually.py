MAX = 1000

st = [0] * MAX
top = 0

def init():
    global top

    top = 0

def isEmpty():
    global top

    return top == 0

def isFull():
    global top
    global MAX

    return top == MAX

def push(x: int):
    global top

    if isFull():
        print("error")
    st[top] = x
    top += 1

def pop():
    global top
    
    if isEmpty():
        print("error")
    top -= 1
    return st[top]

def main():
    init()

    push(3)

    push(5)

    push(7)

    print(pop())

    print(pop())

    push(9)

if __name__ == "__main__":
    main()