#!/usr/bin/python3

def canUnlockAll(boxes):
    # Initialize a set to keep track of visited boxes
    visited = set()
    # Initialize a queue to perform BFS
    queue = [0]  # Start with the first box
    # Mark the first box as visited
    visited.add(0)

    # Perform BFS
    while queue:
        # Get the current box from the queue
        current_box = queue.pop(0)
        # Iterate over the keys in the current box
        for key in boxes[current_box]:
            # If the key opens a new box and that box has not been visited yet
            if key < len(boxes) and key not in visited:
                # Mark the new box as visited
                visited.add(key)
                # Add the new box to the queue to explore its keys
                queue.append(key)

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)

# Example usage
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False

