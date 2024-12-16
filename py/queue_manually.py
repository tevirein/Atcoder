MAX = 1000 # キュー配列の最大サイズ

qu = [0] * MAX # キューを表す配列
head, tail = 0, 0 # キューの要素区間を表す変数

#キューを初期化する
def init():
    global head, tail

    head, tail = 0, 0

# キューが空かどうかを判定する
def isEmpty():
    global head, tail

    return (head == tail)

# キューが満杯かどうかを判定する
def isFull():
    global MAX

    return (head == (tail + 1) % MAX)

# enqueue
def enqueue(x: int):
    global tail, MAX

    if (isFull()):
        raise IndexError("pueue is full.")
    
    qu[tail] = x
    tail += 1
    if tail == MAX:
        tail = 0 # リングバッファの終端に来たら0にする

# dequeue
def dequeue():
    global head, MAX

    if isEmpty():
        raise IndexError("queue is empty.")
    
    res = qu[head]
    head += 1
    if head == MAX:
        head = 0 # リングバッファの終端に来たら0にする
    return res

def main():
    init()

    enqueue(3)
    enqueue(5)
    enqueue(7)

    print(dequeue())
    print(dequeue())

    enqueue(9)

if __name__ == "__main__":
    main()