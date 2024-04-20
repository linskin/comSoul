import copy


def generate_tree(tree, start):
    mid_tree = copy.deepcopy(tree)
    pre_string = "_" * 3 + start
    result = pre_string + '\n'
    tag = True
    while tag:
        tag = False
        cur_string = ""
        j = 0
        for i in range(len(pre_string)):
            if pre_string[i] == '_': continue
            j += 1
            if pre_string[i] in mid_tree:
                tag = True
                item_left, item_rigth = mid_tree[pre_string[i]][0]
                if j == item_left:
                    mid_tree[pre_string[i]].pop(0)
                    cur_string = pre_string[:i] + "___".join(item_rigth) + pre_string[i + 1:]
                    break
        result += cur_string + '\n'
        pre_string = cur_string
    return result


if __name__ == '__main__':
    print("语法分析树：")
    start = 'E'
    tree_list = {
        'E': [[1, ['E', '+', 'T']], [1, ['E', '+', 'T']], [1, ['E', '+', 'T']], [1, ['T']], [12, ['E', '+', 'T']],
              [12, ['T']]],
        'T': [[1, ['F']], [3, ['F']], [5, ['T', '*', 'F']], [5, ['T', '*', 'F']], [5, ['F']], [11, ['F']], [12, ['F']],
              [14, ['T', '*', 'F']], [14, ['F']]],
        'F': [[1, ['i']], [3, ['i']], [5, ['i']], [7, ['i']], [9, ['i']], [11, ['(', 'E', ')']], [12, ['i']],
              [14, ['i']], [16, ['i']]]}
    ans = generate_tree(tree_list, start)
    print(ans)
