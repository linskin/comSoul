import copy


def add_production(non_terminal, production, productions):
    if non_terminal in productions:
        productions[non_terminal].append(production)
    else:
        productions[non_terminal] = [production]


def remove_production(non_terminal, production, productions):
    if non_terminal in productions and production in productions[non_terminal]:
        productions[non_terminal].remove(production)
        if not productions[non_terminal]:  # If the set becomes empty, remove the key
            del productions[non_terminal]


def eliminate_rules(key_item, value_item, production):
    end_production = copy.deepcopy(production)
    mid_key_item = key_item
    end_key_item = mid_key_item + "'"
    mid_value_item = value_item.copy()
    end_value_item = value_item.copy()
    # 先改后删
    for i in range(len(end_value_item)):
        if end_value_item[i] == mid_key_item:
            end_value_item.pop(i)
            end_value_item.append(end_key_item)
            break
    for item in end_production[mid_key_item]:
        if item == mid_value_item: continue
        if mid_key_item in item: continue
        if end_key_item in item: continue
        item.append(end_key_item)
    remove_production(mid_key_item, mid_value_item, end_production)
    add_production(end_key_item, end_value_item, end_production)
    if ['ε'] not in end_production[end_key_item]:
        add_production(end_key_item, ['ε'], end_production)
    else:
        remove_production(end_key_item, ['ε'], end_production)
        add_production(end_key_item, ['ε'], end_production)
    return end_production


def auto_eliminate_rules(productions):
    end_productions = copy.deepcopy(productions)
    tag = True
    while tag:
        tag = False
        for key in end_productions:
            for item in end_productions[key]:
                # 消去规则左递归
                if key in item and len(key) == 1:
                    tag = True
                    end_productions = eliminate_rules(key, item, end_productions)
    return end_productions


def eliminate_grammar(productions):
    mid_productions = copy.deepcopy(productions)
    end_productions = copy.deepcopy(productions)
    mid_changed_keys_list = []
    for key in productions:
        if "'" in key:
            mid_changed_keys_list.append(key.replace("'", ''))
    flg = False
    for key in mid_productions:
        if key in mid_changed_keys_list: continue
        for item in mid_productions[key]:
            tag = False
            for i in range(len(item)):
                if item[i] in mid_changed_keys_list:
                    tag = True
                    flg = True
                    for item_i in mid_productions[item[i]]:
                        end_item = item.copy()
                        end_item.pop(i)
                        end_item[i:i] = item_i
                        add_production(key, end_item, end_productions)
            if tag:
                remove_production(key, item, end_productions)
    return end_productions, flg


def ddd(productions):
    mid_productions = copy.deepcopy(productions)
    tag = False
    for key in mid_productions:
        for item in mid_productions[key]:
            # 消去规则左递归
            if key in item and len(key) == 1:
                tag = True
                break
    return tag


def auto_eliminate_left_recursion(productions):
    end_productions = copy.deepcopy(productions)
    while True:
        end_productions = auto_eliminate_rules(end_productions)
        end_productions, flg = eliminate_grammar(end_productions)
        if not flg:
            break
    return end_productions


if __name__ == '__main__':
    from print_productions import print_productions
    production = {'S': [['S', 'a'], ['T', 'b', 'c'], ['T', 'd']], 'T': [['S', 'e'], ['g', 'h']]}
    print_productions(auto_eliminate_left_recursion(production))
