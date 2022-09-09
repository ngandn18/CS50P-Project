# from project import append_result_id, create_tree, print_node_info, *
from project import *

from mynode import Node
# import pytest

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

    

def test_create_tree():
    # storage, capacity_1, capacity_2, needed = 16, 12, 6, 5
    result, tree = create_tree(16, 12, 6, 5)
    # no sution node
    assert(result == [])
    assert(list(tree.keys())) == list(range(11))
    assert(str(tree[10]) == str(Node(10, 8, 6, 4, 6, [0, 2, 6, 8, 10], 3, 4)))
    # assert(result, := create_tree(16, 12, 6, 5)) == []
    result, tree = create_tree(16, 11, 6, 5)
    # 2 solution node
    assert(result == [3, 4])
    assert(list(tree.keys())) == list(range(7))
    assert(str(tree[6]) == str(Node(6, 2, 0, 10, 6, [0, 2, 6], 2, 2)))
    # assert(len(tree.keys()) == 7)
    result, tree = create_tree(16, 11, 6, 8)
    # 2 solution node
    assert(result == [31, 32])
    assert(list(tree.keys())) == list(range(33))
    assert(str(tree[32]) == str(Node(32, 30, 2, 8, 6, [0, 2, 6, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],
 3, 14)))


def test_get_node_info():
    # rule 1
    node = Node(5, 2, 8, 8, 0, [0, 2, 5], 1, 2)
    assert(get_node_info(node) == 'Move oil from the container 2 into container 1 - R1--(8, 8, 0)')
    # rule 2
    node= Node(6, 2, 0, 10, 6, [0, 2, 6], 2, 2)
    assert(get_node_info(node) == 'Move oil from the storage into container 1 - R2--(0, 10, 6)')
    # rule 3
    node =Node(32, 30, 2, 8, 6, [0, 2, 6, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32], 3, 14)
    assert(get_node_info(node) == 'Move oil from the container 1 into container 2 - R3--(2, 8, 6)')
    # rule 4
    node = Node(12, 10, 3, 5, 8, [0, 1, 4, 8, 10, 12], 4, 5)
    assert(get_node_info(node) == 'Move oil from the storage into container 2 - R4--(3, 5, 8)')
    # rule 5
    node = Node(15, 14, 14, 0, 2, [0, 1, 4, 8, 10, 12, 14, 15], 5, 7)
    assert(get_node_info(node) == 'Move oil from the container 1 into the storage - R5--(14, 0, 2)')    
    # rule 6
    node = Node(7, 3, 13, 3, 0, [0, 1, 3, 7], 6, 3)
    assert(get_node_info(node) == 'Move oil from the container 2 into the storage - R6--(13, 3, 0)')
    