import stack_manually

def con_check(text: str)-> bool:
    """
    stackにかっこだけをpushして、判定する関数
    """
    dic = {")":"(", "}":"{", "]":"["}

    for i in range(len(text)):
        if text[i] in "({[":
            stack_manually.push(text[i])
        elif text[i] in ")}]":
            if not stack_manually.isEmpty():
                take = stack_manually.pop()
            else:
                print("不整合")
                exit()
            if dic[text[i]] == take:
                continue
            else:
                print("不整合")
                exit()
        else:
            continue
    
    if stack_manually.isEmpty():
        print("整合")
    else:
        print("不整合")

def main():
    text = "ab{cd[e(f){g}(h)]i}(j)"
    con_check(text)

if __name__ == "__main__":
    main()