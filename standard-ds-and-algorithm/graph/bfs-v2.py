"""
Version2:
- simple bfs traversal implementation with queue
- implementation with adjacency list


Implementation steps:
- Step1: initializing - add the source node to the 'next_to_process' queue. Also add source node to 'seen' list

- Step2: pop a 'processing_node' from the 'next_to_process' queue. And add the 'processing_node' to the 'processed' list
    - Popping a node from the 'next_to_process' queue means you will do some process on the node you just
    popped - 'processing_node'. Example of some process that you could do on 'processing_node'- (1) printing the node,
    (2) searching the node (3) adding the node to list (4) or any other operations
    - Adding 'processing_node' to 'processed' list is OPTIONAL

- Step3: for each unseen neighbor (adjacent node) to processing_node add it to next_to_process queue.
Also add each of these neighbour to the 'seen' set.
    -  Adding a node to the 'seen' list means you just seen/found the node. I'm not sure whether these nodes are
         processed or not. But I'm sure I've seen them somewhere.
    - the node found in the 'seen' could be processed or unprocessed.
    - I only could guarantee that the nodes found in the 'processed' list are processed
    - 'seen' list just keep tracks of the of the seen node so we don't fall into an infinite loop - by attempting to
        process an already processed node again
    - If you found any node in the 'seen' set then you don't NEED TO ADD it in the 'next_to_process' list again.
    - Adding a node to 'next_to_process' list => you will process the first node from that queue later.
    - Removing a node from 'next_to_process' => already done with processing the node.

- Step4: repeat step 2 and 3 until the 'next_to_process' list is empty

"""
import collections


def doBfs(graph, source):
    processed, seen, next_to_process = [], set(), collections.deque()

    # step1: initializing - add the source node to the 'next_to_process' queue.
    next_to_process.append(source)
    seen.add(source)

    while next_to_process:
        # Step2: pop a 'processing_node' from the 'next_to_process' queue. And add the node to the 'processed' list
        processing_node = next_to_process.popleft()
        # Do your required processing eg- print, checking if some node exist. THEN ADD it to the 'processed' list.
        # Do your processing here
        # print(processing_node, end=' ')
        processed.append(processing_node)

        for neighbor in graph[processing_node]:
            if neighbor not in seen:
                # step3: for each unseen neighbor (adjacent node) to processing_node add it to 'next_to_process' queue
                # and also add it to the 'seen' set. Adding anything to the 'seen' set means you just discover/seen it
                # and you will process it later.
                next_to_process.append(neighbor)
                seen.add(neighbor)
        # step4: repeat step 2 and 3 until the 'next_to_process' queue is empty

    print(processed)


def main():
    graph1 = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    doBfs(graph1, 0)
    # expected: [0 1 2 3]

    graph2 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}
    doBfs(graph2, 0)
    # expected : [0, 1, 2, 3, 4]

    graph3 = {
        'a': ['b', 'c', 'd', 'm'],
        'b': ['a', 'c', 'e'],
        'c': ['a', 'b', 'e', 'f'],
        'd': ['a', 'e'],
        'e': ['b', 'c', 'd', 'h', 'i'],
        'f': ['c'],
        'g': ['c', 'h'],
        'h': ['e', 'g', 'i'],
        'i': ['e', 'h', 'j'],
        'j': ['i', 'l', 'k'],
        'k': ['j'],
        'l': ['j', 'm'],
        'm': ['l', 'a']
    }
    doBfs(graph3, 'a')
    # expected: [a b c d m e f l h i j g k ]

    graph4 = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    doBfs(graph4, 2)
    # expected: [2, 0, 3, 1]

    graph5 = {
        1: [2, 4],
        2: [1, 3, 5, 7, 8],
        3: [2, 4, 9, 10],
        4: [1, 3],
        5: [2, 6, 7],
        6: [5],
        7: [2, 5, 8],
        8: [2, 7],
        9: [3],
        10: [3]
    }
    doBfs(graph5, 1)
    # expected: [1, 2, 4, 3, 5, 7, 8, 9, 10, 6]

    tree1 = {9: [3, 7, 4],
             3: [8], 7: [1, 5], 4: [12, 13],
             8: [10, 11], 1: [14], 5: [15, 16], 12: [17, 18], 13: [19, 20, 21],
             10: [], 11: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], 20: [], 21: []}
    doBfs(tree1, 9)
    # expected: [9, 3, 7, 4, 8, 1, 5, 12, 13, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21]


if __name__ == '__main__':
    main()
