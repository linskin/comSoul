class GrammarCleaner:
    def __init__(self):
        pass

    @staticmethod
    def add_to_prod_dict(s, t, p):
        if s not in p:
            p[s] = [t]
        else:
            p[s].append(t)

    @staticmethod
    def clean_UtoU(production):
        cleaned_production = {}
        for key, value in production.items():
            if key not in value:
                cleaned_production[key] = value
        return cleaned_production

    @staticmethod
    def clean_Utou1(production, start):
        end_production = production.copy()
        marks = [start]
        start_list = production[start]
        for item in start_list:
            for item_s in item:
                if 'A' <= item_s <= 'Z' and item_s not in marks:
                    marks.append(item_s)
        tag1 = True
        tag2 = True
        while tag1 or tag2:
            tag1 = False
            tag2 = False
            for key in production:
                if key in marks:
                    continue
                k_list = production[key]
                for item in k_list:
                    for item_s in item:
                        if 'A' <= item_s <= 'Z' and item_s in marks:
                            tag1 = True
                            marks.append(key)
            for key in marks:
                k_list = production[key]
                for item in k_list:
                    for item_s in item:
                        if 'A' <= item_s <= 'Z' and item_s not in marks:
                            tag2 = True
                            marks.append(item_s)
        for key in end_production.copy():
            if key not in marks:
                del end_production[key]
        return end_production

    def clean_Utou2(self, production):
        end_production = {}
        marks = []
        for key in production:
            for item in production[key]:
                tag = True
                for item_s in item:
                    if 'A' <= item_s <= 'Z':
                        tag = False
                        break
                if tag:
                    marks.append(key)
                    self.add_to_prod_dict(key, item, end_production)
        tag1 = True
        while tag1:
            tag1 = False
            for key in production:
                for item in production[key]:
                    num_no_mark = False
                    for item_s in item:
                        if 'A' <= item_s <= 'Z' and item_s not in marks:
                            num_no_mark = True
                            break
                    if not num_no_mark and (key not in end_production or item not in end_production[key]):
                        tag1 = True
                        marks.append(key)
                        self.add_to_prod_dict(key, item, end_production)
        return end_production

    def auto_clean(self, production, start):
        end_production = self.clean_UtoU(production)
        tag = True
        while tag:
            end_production = self.clean_Utou1(end_production, start)
            if end_production == end_production:
                tag = False
            end_production = self.clean_Utou2(end_production)
            if end_production == end_production:
                tag = False
        return end_production


if __name__ == '__main__':
    cleaner = GrammarCleaner()
    productions = {'Z': ['Be'], 'A': ['Ae', 'e'], 'B': ['Ce', 'Af'], 'C': ['Cf']}
    print(cleaner.clean_UtoU(productions))
    print(cleaner.clean_Utou1(productions, start='Z'))
    print(cleaner.clean_Utou2(productions))
    print(cleaner.auto_clean(productions, start='Z'))
