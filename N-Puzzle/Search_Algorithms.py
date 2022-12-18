from State import State
from queue import PriorityQueue


def best_first_search_euclidean_distance(given_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    # root.evaluation()

    evaluation = root.euclidean_distance(n)
    frontier.put((evaluation[0], counter, root))  # based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1

                evaluation = child.euclidean_distance(n)
                # based on greedy evaluation
                frontier.put((evaluation[0], counter, child))
    return


def best_first_search_Manhattan_Distance(given_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    # root.evaluation()

    evaluation = root.Manhattan_Distance(n)
    frontier.put((evaluation[0], counter, root))  # based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1

                evaluation = child.Manhattan_Distance(n)
                # based on greedy evaluation
                frontier.put((evaluation[0], counter, child))
    return


def best_first_search_Misplaced_Tiles(given_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    # root.evaluation()

    evaluation = root.Misplaced_Tiles(n)
    frontier.put((evaluation[0], counter, root))  # based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1

                evaluation = child.Misplaced_Tiles(n)
                # based on greedy evaluation

                frontier.put((evaluation[0], counter, child))


def best_first_searchs_placed_Tiles(given_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    # root.evaluation()

    evaluation = root.placed_Tiles(n)
    frontier.put((evaluation[0], counter, root))  # based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1

                evaluation = child.placed_Tiles(n)

                frontier.put((evaluation[0], counter, child))

    return
