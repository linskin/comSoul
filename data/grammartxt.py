grammar_str1 = "Z ::= B e\nA ::= A e\nA ::= e\nB ::= C e\nB ::= A f\nC ::= C f\nD ::= f\nE ::= E\n"
grammar_str2 = "E ::= E + T | T\nT ::= T * F | F\nF ::= ( E ) | i\n"
grammar_str3 = "A ::= B a | C b | c\nB ::= d a | A e | f\nC ::= B g | h"
grammar_str4 = "Ems ::= Ems + Tfs | Tfs\nTfs ::= Tfs * F' | F'\nF' ::= ( Ems ) | iss\n\n\n\n\n"
