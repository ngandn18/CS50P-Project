# from project import append_result_id, create_tree, print_node_info, *
from project import *

from mynode import Node
import pytest

def test_is_solution():
    node, needed = Node(10, 8, 6, 4, 6, [0, 2, 6, 8, 10], 3, 4), 5
    assert(is_solution(node, needed) == False)
    node, needed = Node(3, 1, 5, 5, 6, [0, 1, 3], 3, 2), 5
    assert(is_solution(node, needed) == True)
    node, needed = Node(31, 29, 8, 8, 0, [0, 2, 5, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],
1, 14), 8
    assert(is_solution(node, needed) == True)
    node, needed = Node(32, 30, 2, 8, 6, [0, 2, 6, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],
 3, 14), 8
    assert(is_solution(node, needed) == True)

