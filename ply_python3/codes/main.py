#! /usr/bin/env python
# coding=utf-8
from py_yacc import yacc
from util import clear_text
from translation import Tran

def translation(filename):
    text = clear_text(open(filename, 'r').read())
    def put2str(node):
        global res
        if node:
            data = str(node._data)
            data = data.replace("[", "").replace("]", "").replace("/'", "")
            res += data
        if node._children:
            for i in node._children:
                res += "["
                put2str(i)
                res += "]"
    # syntax parse
    root = yacc.parse(text)
    root.print_node(0)
    # translation
    t = Tran()
    t.trans(root)
    print(t.v_table)

    put2str(root)
    print("["+res+"]")
if __name__ == '__main__':
    res = ""
    translation("quick_sort.py")
