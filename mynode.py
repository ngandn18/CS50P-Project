class Node:
    def __init__(self, 
            id, 
            parent_id, 
            n_storage, 
            container_1, 
            container_2,
            path, 
            rule, 
            level
            ):
            
        self.id = id                    # id of the node: int
        self.parent_id = parent_id      # id of the parent of the node: int
        self.n_storage = n_storage      # new capacity of the storage: int
        self.container_1 = container_1  # new capacity of the container 1: int
        self.container_2 = container_2  # new capacity of the container 2
        self.path = path                # list of nodes from root 
        self.rule = rule                # id of the rule creating the node
        self.level = level              # level of the node
        

    def __str__(self):
        """
        For checking anh printing
        """
        return f'Node({self.id}, {self.parent_id}, {self.n_storage}, ' \
            f'{self.container_1}, {self.container_2}, {self.path}, {self.rule}, {self.level})'

