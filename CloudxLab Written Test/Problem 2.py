"""
Algorithm:
1. take employee json list
2. create dictionary (employee tree map) with key as manager id and value as
employee list under the manager
3. select root node where manager id is null and send to print node method
4. in print node method create current node xml structure, get the children list
5. repeat the recursive process till no more children found in the tree map
6. indent variable used to indent child nodes.
"""

def print_tree(employee_list):
    def get_parent_child_map():
        manager_dict = {}
        for e in employee_list:
            sub_emp_list = manager_dict.get(e['manager_id'])
            if sub_emp_list is not None:
                sub_emp_list.append(e)
            else:
                manager_dict.setdefault(e['manager_id'], [e])
        return manager_dict
    tree_map = get_parent_child_map()
    print(tree_map)

    def print_node(parent,indent):
        node_xml = ""
        for node in parent:
            node_xml += "\n" + ("  " * indent) + "<Node name=\"" + node['name'] + "\" id=\"" + str(node['id']) + "\">"
            child = tree_map.get(node['id'])

            if child is not None:
                node_xml += print_node(child, indent + 1)
            node_xml += "\n" + ("  " * indent) + "</Node>"

        return node_xml

    return print_node(tree_map[None], 0)


if __name__ == '__main__':
    list = [
        {'id': 1, 'name': 'Dinesh', 'manager_id': 2},
        {'id': 2, 'name': 'Ramesh', 'manager_id': 4},
        {'id': 3, 'name': 'Sandeep', 'manager_id': 4},
        {'id': 4, 'name': 'Abhishek', 'manager_id': None}
    ]
    print(print_tree(list))
