from bio_EulerCycleSample import eulerian_cycle

def eulerian_path(edge_dict):
    '''Returns an Eulerian path from the given edges.'''
    # Determine the unbalanced edges.
    out_values = reduce(lambda a,b: a+b, edge_dict.values())
    for node in set(out_values+edge_dict.keys()):
        out_value = out_values.count(node)
        if node in edge_dict:
            in_value = len(edge_dict[node])
        else:
            in_value = 0

        if in_value < out_value:
            unbalanced_from = node
        elif out_value < in_value:
            unbalanced_to = node

    # Add an edge connecting the unbalanced edges.
    if unbalanced_from in edge_dict:
        edge_dict[unbalanced_from].append(unbalanced_to)
    else:
        edge_dict[unbalanced_from] = [unbalanced_to]

    # Get the Eulerian Cycle from the edges, including the unbalanced edge.
    cycle = eulerian_cycle(edge_dict)

    # Find the location of the unbalanced edge in the eulerian cycle.
    divide_point = filter(lambda i: cycle[i:i+2] == [unbalanced_from, unbalanced_to], xrange(len(cycle)-1))[0]

    # Remove the unbalanced edge, and shift appropriately, overlapping the head and tail.
    return cycle[divide_point+1:]+cycle[1:divide_point+1]

if __name__ == '__main__':

    # Read the input data.
    with open('dataset_203_5.txt') as input_data:
        edges = {}
        for edge in [line.strip().split(' -> ') for line in input_data.readlines()]:
            if ',' in edge[1]:
                edges[int(edge[0])] = map(int,edge[1].split(','))
            else:
                edges[int(edge[0])] = [int(edge[1])]

    # Get the Eulerian path associated with the edges.
    path = eulerian_path(edges)

    # Print and save the answer.
    print '->'.join(map(str, path))
    with open('dataset_203_5_out.txt', 'w') as output_data:
        output_data.write('->'.join(map(str, path)))