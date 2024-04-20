class GrammaticalQuadrupleExtraction:
    @staticmethod
    def __extract_from_line(s):
        left, right = s.split('::=')
        return left.strip(), right.strip()

    def __init__(self):
        self.__production = {}
        self.__start = ''
        self.__terminators = []
        self.__non_terminators = []

    def __extract_rules_from_string(self, ls, rs):
        mid_re = rs.split('|')
        for item_s in mid_re:
            if ls not in self.__production:
                self.__production[ls] = [item_s]
            else:
                self.__production[ls].append(item_s)

    def extract_grammar_components(self, gs):
        gs = gs.replace(' ', '')
        mid_s = gs.split("\n")
        for item_s in mid_s:
            left, right = GrammaticalQuadrupleExtraction.__extract_from_line(item_s)
            self.__extract_rules_from_string(left, right)
            if 'Z' >= left >= 'A':
                self.__terminators.append(left)
            if not self.__start:
                self.__start = left
            for item_r in right:
                if item_r == ' ':
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
