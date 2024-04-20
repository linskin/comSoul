import threading

from extract_grammar import GrammaticalQuadrupleExtraction
from grammar_derivation_visualizer import GrammarDerivationVisualizer
from output_window import MyOutputWindow
from tools.banner import banner_str, banner_str_welcome


def solve():
    print(banner_str, '\n', banner_str_welcome)
    # 数据初始化
    grammar_string = "E ::= E + T | T \nT ::= T * F | F \nF ::= ( E ) | i"
    extractor = GrammaticalQuadrupleExtraction()
    terminators, non_terminators, production, start = extractor.extract_grammar_components(grammar_string)

    # 实例化两个窗口类
    window1 = MyOutputWindow(grammar_string=grammar_string)
    window2 = GrammarDerivationVisualizer(production, start)

    # 创建并启动线程
    thread1 = threading.Thread(target=window1.run())
    thread2 = threading.Thread(target=window2.run())
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    solve()
