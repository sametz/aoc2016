from part2 import parse_input, nodes_by_capacity


def test_parse_input():
    node_data = parse_input("test_input.txt", 1)
    assert node_data[0] == ((0, 0), 10, 8, 2, 80)
    assert node_data[-1] == ((2, 2), 9, 6, 3, 66)


def test_grid_has_empty_node():
    node_data = parse_input("input.txt", 2)
    for node in node_data:
        if node[2] == 0:
            print(node)  # 35, 18
    assert 1 == 1


def test_nodes_by_capacity():
    nodes = parse_input("input.txt", 2)
    nodes_sorted = nodes_by_capacity(nodes)
    for node in nodes_sorted[-30:]:
        print(node)