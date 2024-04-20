class GrammaticalQuadrupleExtraction:
    @staticmethod
    def __extract_from_line(s):
        left, right = s.split('::=')
        return left.strip(), right.strip()

    # @staticmethod
    def __add_production(self, non_terminal, oneproduction):
        if non_terminal in self.__production:
            self.__production[non_terminal].append(oneproduction)
        else:
            self.__production[non_terminal] = [oneproduction]

    def __init__(self):
        self.__production = {}
        self.__start = ''
        self.__terminators = []
        self.__non_terminators = []

    def __extract_rules_from_right(self, ls, rs):
        mid_re = rs.split('|')
        for item in mid_re:
            item_ts = []
            for item_t in item:
                item_ts += [item_t]
            self.__add_production(ls, item_ts)

    def extract_grammar_components(self, gs):
        gs = gs.replace(' ', '')
        mid_s = gs.split("\n")
        for item_s in mid_s:
            left, right = self.__extract_from_line(item_s)
            self.__extract_rules_from_right(left, right)
            if ('Z' >= left >= 'A') and left not in self.__terminators:
                self.__terminators.append(left)
            if self.__start == '':
                self.__start = left
            for item_r in right:
                if item_r == '|':
                    continue
                if (item_r > 'Z' or item_r < 'A') and item_r not in self.__non_terminators:
                    self.__non_terminators.append(item_r)
        return self.__terminators, self.__non_terminators, self.__production, self.__start


if __name__ == '__main__':
    # 示例用法
    extractor = GrammaticalQuadrupleExtraction()
    grammar_string = "E ::= E + T | T\nT ::= T * F | F\nF ::= ( E ) | i"
    terminators, non_terminators, production, start = extractor.extract_grammar_components(grammar_string)
    print(terminators)
    print(non_terminators)
    print(production)
    print(start)
