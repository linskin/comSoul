grammar_str1 = ("Z ::= B e\n"
                "A ::= A e\n"
                "A ::= e\n"
                "B ::= C e\n"
                "B ::= A f\n"
                "C ::= C f\n"
                "D ::= f\n"
                "E ::= E\n")
grammar_str2 = ("E ::= E + T | T\n"
                "T ::= T * F | F\n"
                "F ::= ( E ) | i\n")
grammar_str3 = ("A ::= B a | C b | c\n"
                "B ::= d a | A e | f\n"
                "C ::= B g | h")
grammar_str4 = ("Ems ::= Ems + Tfs | Tfs\n"
                "Tfs ::= Tfs * F' | F'\n"
                "F' ::= ( Ems ) | iss\n")
