def chooser_judgment(cnt):
    while True:
        answer = input("Choose a number from 1 to {}: ".format(cnt))
        answer = int(answer)
        if 1 <= answer <= cnt:
            return answer
        else:
            print("Please enter a number from 1 to {}".format(cnt))
            continue


def production_shower(production, key):
    # while True:
    # print("Production shower with key {}: ".format(key))
    for i, item in enumerate(production, start = 1):
        mid_str = " ".join(item)
        print(f"{i}: {key} => {mid_str}")
    print("-" * 100)
    choice = chooser_judgment(len(production))
    return choice


def auto_derivation(input_str, productions, start_symbol):
    derived_string = start_symbol  # 初始时将起始符号作为推导的起点
    result = ""  # 存储推导结果
    tree = {}  # 存储语法分析树
    # 逐步推导直到无法再推导为止
    while derived_string:
        derived = False  # 标志是否成功推导
        # 遍历所有产生式
        for key in productions:
            # 如果当前推导串中包含产生式左部，则问询是否进行替换
            if key in derived_string:
                print("Deriving {} with key {}".format(derived_string, key))
                choice = production_shower(productions[key], key)
                # 问询替换
                end_string = "".join(productions[key][choice - 1])
                pos = derived_string.find(key)
                # 将当前推导过程添加到结果中
                result += " => {} ({} -> {})\n".format(derived_string, key, end_string)
                # 进行替换
                derived_string = derived_string[:pos] + end_string + derived_string[pos + len(key):]
                derived = True  # 表示成功推导
                # 更新语法分析树
                if key in tree:
                    tree[key].append(end_string)
                else:
                    tree[key] = [end_string]
            # 如果成功推导，就跳出外层循环
            if derived:
                break

        # 如果无法再进行推导，则退出循环
        if derived_string == input_str:
            print("Derive done, the end symbol is {}".format(derived_string))
            break
        if not derived:
            print("Derive false, the end symbol is {}".format(derived_string))
            break

    return result, tree


if __name__ == "__main__":
    input_string = "i + i * i"
    production = {'E': [['E', '+', 'T'], ['T']], 'T': [['T', '*', 'F'], ['F']], 'F': [['(', 'E', ')'], ['i']]}
    auto_derivation(input_string, production, 'E')
