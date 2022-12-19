import argparse
import re
import sys


def arg_parse():
    """Docstring here"""
    parser = argparse.ArgumentParser(description='Some description')
    parser.add_argument('filename', help='Filename parameter for input file')
    return parser.parse_args()


def is_int(s):
    """Docstring here"""
    try:
        return int(s)
    except ValueError:
        return False


def node_trace(pointer, nodes_pointers, nodes):
    """Docstring here"""
    if is_int(pointer[0]):
        if nodes[pointer[0]][1] == 1:
            return
        else:
            nodes[pointer[0]][0] = 1
            nodes[pointer[0]][1] = 1

    for x in nodes_pointers:
        if x[0] == pointer[1] and nodes[x[0]][1] == 0:
            node_trace(x, nodes_pointers, nodes)

        if is_int(x[0]):
            if nodes[x[0]][1] == 1:
                nodes[x[1]][0] = 1
                nodes[x[1]][1] = 1
        else:
            nodes[x[1]][0] = 1
            nodes[x[1]][1] = 1
    

def get_nodes():
    """Docstring here"""
    nodes_pointers, nodes = [], {}
    args = arg_parse()
    input_file = args.filename

    with open(input_file) as in_file:
        node_count = 0
        for line in in_file:
            if node_count == 0:
                node_count = int(line)
            else:
                split_line = line.rstrip()
                split_line = re.split(r'[,]', split_line)

                nodes_pointers.append([split_line[0], split_line[1]])

        count = 0
        while count < node_count:
            nodes[str(count)] = [0, 0]
            count += 1

        for item in nodes_pointers:
            if not is_int(item[0]):
                node_trace(item, nodes_pointers, nodes)

    return nodes


def print_result(message, value, nodes):
    """Docstring here"""
    print(message)
    for item in sorted(nodes.items()):
        if item[1][1] == value:
            print(item[0])


def main():
    """Docstring here"""
    nodes = get_nodes()
    print_result('\nMarked: ', 1, nodes)
    print_result('\nReclaimed: ', 0, nodes)


if __name__ == '__main__':
    main()