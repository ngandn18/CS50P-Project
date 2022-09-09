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


    def create_pseudo_node(self, containers, id, n_storage, rule):
        """
        Get important values and return a dictionary of important values 
        for checking if a new node can be created
        """
        pseudo = {}
        pseudo['containers'] = containers
        pseudo['parent_id'] = id
        pseudo['n_storage'] = n_storage
        pseudo['rule'] = rule
        
        return pseudo


    def activate_rules(self, storage, capacity_1, capacity_2):
        """
        From the properties of this node, we check 6 rules to create the list of pseudo nodes.
        """
        pseudo_nodes = []
        # Change the container 1
        if self.container_1 < capacity_1:
            # Check rule 1
            if self.container_2 > 0:
                # Move oil from the container 2 into container 1 - R1
                adjust = min(capacity_1 - self.container_1, self.container_2)
                if adjust:
                    n_c1 = self.container_1 + adjust
                    n_c2 = self.container_2 - adjust
                    rule = 1
                    n_storage = storage - (n_c1 + n_c2)
                    pseudo_nodes.append(self.create_pseudo_node((n_c1, n_c2), self.id, n_storage, rule))

            # Check rule 2
            if self.n_storage > 0:
                # Move oil from the storage into container 1 - R2
                adjust = min(self.n_storage, capacity_1 - self.container_1)
                if adjust:
                    n_c1 = self.container_1 + adjust
                    n_c2 = self.container_2
                    rule = 2
                    n_storage = storage - (n_c1 + n_c2)
                    pseudo_nodes.append(self.create_pseudo_node((n_c1, n_c2), self.id, n_storage, rule))


        # Change the container 2
        if self.container_2 < capacity_2:
            # Check rule 3
            if self.container_1 > 0:
                # Move oil from the container 1 into container 2 - R3
                adjust = min(capacity_2 - self.container_2, self.container_1)
                if adjust:
                    n_c1 = self.container_1 - adjust
                    n_c2 = self.container_2 + adjust
                    rule = 3
                    n_storage = storage - (n_c1 + n_c2)
                    
                    pseudo_nodes.append(self.create_pseudo_node((n_c1, n_c2), self.id, n_storage, rule))

                    
            # Check rule 4
            if self.n_storage > 0:
                # Move oil from the storage into container 2 - R4
                adjust = min(self.n_storage, capacity_2 - self.container_2)
                if adjust:
                    n_c1 = self.container_1
                    n_c2 = self.container_2 + adjust
                    rule = 4
                    n_storage = storage - (n_c1 + n_c2)
                    
                    pseudo_nodes.append(self.create_pseudo_node((n_c1, n_c2), self.id, n_storage, rule))

        # Change the storage                    
        if self.n_storage < storage:
            # Check rule 5
            if self.container_1 > 0:
                # Move oil from the container 1 into the storage - R5
                n_c1 = 0
                n_c2 = self.container_2
                rule = 5
                n_storage = storage - (n_c1 + n_c2)
                pseudo_nodes.append(self.create_pseudo_node((n_c1, n_c2), self.id, n_storage, rule))
                    
            # Check rule 6
            if self.container_2 > 0:
                # Move oil from the container 2 into the storage - R6
                n_c2 = 0
                n_c1 = self.container_1
                rule = 6
                n_storage = storage - (n_c1 + n_c2)
                
                pseudo_nodes.append(self.create_pseudo_node((n_c1, n_c2), self.id, n_storage, rule))

        return pseudo_nodes
