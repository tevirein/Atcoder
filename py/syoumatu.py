# import stack_manually

# n = "(()(())())(()())"
# count = 0
# a = []

# for i in n:
#     if i == "(":
#         stack_manually.push(i)
#         count += 1
#     elif i == ")":
#         pop = stack_manually.pop()
#         if pop == "(":
#             a.append([count, count+1])
#             count += 1
#         elif pop == ")":
#             print("不整合")
#             exit()

# print(a)

# if stack_manually.isEmpty():
#     print("整合")
# else:
#     print("不整合")

def check_parentheses_and_find_pairs(s):
    stack = []  # スタック
    pairs = []  # 対応関係を記録するリスト
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # 左括弧のインデックスをスタックに追加
        elif char == ')':
            if not stack:
                return False, []  # 整合していない
            open_index = stack.pop()  # 対応する左括弧のインデックスを取得
            pairs.append((open_index + 1, i + 1))  # 1-based インデックスで記録
    
    if stack:
        return False, []  # スタックが空でない場合、整合していない

    return True, pairs  # 整合している場合、対応関係を返す


s = "(()(())())(()())"
is_valid, pairs = check_parentheses_and_find_pairs(s)
if is_valid:
    print("括弧列は整合しています。")
    print("対応関係:", pairs)
else:
    print("括弧列は整合していません。")
