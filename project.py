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


def create_tree(storage, capacity_1, capacity_2, needed):
    """
    Create the first node of the tree
    Create the first value of container list
    Create the tree and find if the solution nodes exist in the tree
    Return the results dictionary with the details of the path from root to the node having the needed value and the complete tree.
    """    
    tree = {}
    lst_containers = []
    tree[0] = Node(0, 0, storage, 0, 0, [0], 0, 0)
    lst_containers.append((0,0))
    result = []

    control = 1
    start = 0

    while control > 0:
        total = max(tree.keys())

        for k in range(start, total + 1):
            if k not in result:
                pseudo_nodes = tree[k].activate_rules(storage, capacity_1, capacity_2)
                for node in pseudo_nodes:
                    if node['containers'] not in lst_containers:
                        # Create id for new node
                        id = max(tree.keys()) + 1
                        # Create path for new node
                        path = tree[node['parent_id']].path.copy()
                        path.append(id)
                        # Create level for new node
                        level = tree[node['parent_id']].level + 1
                        # Create new node 
                        tree[id] = Node(id, node['parent_id'], node['n_storage'], node['containers'][0], node['containers'][1], path, node['rule'], level)
                        # Update lst_containers for further checking new Node
                        lst_containers.append(node['containers'])
                        # Check if Node is the result: is_solution(tree[id], needed), add this Node to the result list
                        if is_solution(tree[id], needed):
                            result.append(id)
                
        # Print the list of nodes for debug
        # for key in range(total+1, max(tree.keys())+1):
        #     print(tree[key])

        start = total + 1
        control = max(tree.keys()) - total
        # stop creating more nodes when there are 2 solutions
        if len(result) == 2:
            break

    return result, tree

