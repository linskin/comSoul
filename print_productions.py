def print_productions(productions):
    result = ""
    for key in productions:
        tss = ""
        for item in productions[key]:
            for item_s in item:
                for item_t in item_s:
                    tss += item_t + ' '
            tss += '| '
        result += f"{key} ::= {tss[:-2]}\n"
    return result[:-1]
        # print()


if __name__ == "__main__":
    production = {'S': [['S', 'a'], ['T', 'b', 'c'], ['T', 'd']], 'T': [['S', 'e'], ['g', 'h']]}
    ans = print_productions(production)
    print(ans)
