from mynode import Node, get_vars

# Rule 0 represent the initiation of the tree
rules = [
        'Begin: 2 containers are empty',
        'Move oil from the container 2 into container 1 - R1',
        'Move oil from the storage into container 1 - R2',
        'Move oil from the container 1 into container 2 - R3',
        'Move oil from the storage into container 2 - R4',
        'Move oil from the container 1 into the storage - R5',
        'Move oil from the container 2 into the storage - R6'
    ]



def is_solution(node, needed):
    """
    Check to return True if node is a solution node else Fase
    """
    return needed == node.container_1 or needed == node.container_2 

