def S(input_string, adjacency_matrix):
    global index
    index = 0
    initial_state = add_state(adjacency_matrix)
    if not T(input_string, initial_state, adjacency_matrix):
        return False
    if not Q(input_string, adjacency_matrix):
        return False
    print_adjacency_matrix(adjacency_matrix)
    return index == len(input_string)


def E(input_string, current_state, adjacency_matrix):
    global index
    if not T(input_string, current_state, adjacency_matrix):
        return False
    if not Q(input_string, adjacency_matrix):
        return False
    if index < len(input_string) and input_string[index] == ')' and index + 1 != len(input_string):
        return True
    elif index < len(input_string) and input_string[index] == 'e':
        next_state = add_state(adjacency_matrix)
        add_transition(adjacency_matrix, current_state, next_state, 'e')
        return E(input_string, next_state, adjacency_matrix)
    return False


def T(input_string, current_state, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] in ('(', 'a', 'b'):
        next_state = F(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        current_state = next_state
        next_state = R(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        return next_state
    return False


def F(input_string, current_state, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] in ('a', 'b'):
        index += 1
        next_state = add_state(adjacency_matrix)
        add_transition(adjacency_matrix, current_state, next_state, input_string[index - 1])
        next_state = U(input_string, next_state, adjacency_matrix)
        if next_state is None:
            return False
        return next_state
    elif index < len(input_string) and input_string[index] == '(':
        index += 1
        next_state = E(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        if index < len(input_string) and input_string[index] == ')':
            index += 1
        else:
            return False
        next_state = U(input_string, next_state, adjacency_matrix)
        if next_state is None:
            return False
        return next_state
    return False


def T(input_string, current_state, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] in ('(', 'a', 'b'):
        next_state = F(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        next_state_2 = add_state(adjacency_matrix)
        add_transition(adjacency_matrix, next_state, next_state_2, 'e')
        next_state_3 = R(input_string, next_state_2, adjacency_matrix)
        if next_state_3 is None:
            return False
        return next_state_3
    return False


def Q(input_string, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] in ('|', '+'):
        index += 1
        if index < len(input_string):
            if not T(input_string, 0, adjacency_matrix):
                return False
            if not Q(input_string, adjacency_matrix):
                return False
            return True
        else:
            return False
    return True


def R(input_string, current_state, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] in ('(', 'a', 'b'):
        next_state = F(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        current_state = next_state
        next_state = R(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        return next_state
    return True


def U(input_string, current_state, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] == '*':
        index += 1
        next_state = add_state(adjacency_matrix)
        add_transition(adjacency_matrix, current_state, next_state, 'e')
        add_transition(adjacency_matrix, next_state, current_state, 'e')
        next_state = U(input_string, next_state, adjacency_matrix)
        if next_state is None:
            return False
        return next_state
    return current_state


def valid(char):
    if char in ['a', 'b', '*', '(', ')', '|', '$', '+']:
        return 1
    else:
        return 0


def add_state(adjacency_matrix):
    state_name = str(len(adjacency_matrix))
    adjacency_matrix[state_name] = {}
    return state_name


def add_transition(adjacency_matrix, from_state, to_state, symbol):
    if symbol == 'e':
        symbol = 'ε'
    adjacency_matrix[from_state].setdefault(symbol, []).append(to_state)


def print_adjacency_matrix(adjacency_matrix):
    print("Expression accepted")
    print("State    a    b    e")
    for state, transitions in adjacency_matrix.items():
        a_transitions = "[" + ", ".join(transitions.get('a', [])) + "]"
        b_transitions = "[" + ", ".join(transitions.get('b', [])) + "]"
        e_transitions = "[" + ", ".join(transitions.get('e', [])) + "]"
        print(f"{state:<9}{a_transitions:<5}{b_transitions:<5}{e_transitions}")

    print("NFA States")
    print("start:", next(iter(adjacency_matrix.keys())))

    accept_states = []
    visited = set()

    def dfs(state):
        if state in visited:
            return
        visited.add(state)
        if 'e' in adjacency_matrix[state]:
            for next_state in adjacency_matrix[state]['e']:
                dfs(next_state)
        if '$' in adjacency_matrix[state]:
            accept_states.append(state)

    dfs(next(iter(adjacency_matrix.keys())))
    print("accept:", ', '.join(accept_states))


# Main code
print("Enter a Regular input_string! ")
input_string = input()

def remove_whitespace(input_string):
    return input_string.replace(" ", "")

input_string = remove_whitespace(input_string)

index = 0
next_char = input_string[0]

def get_next_char():
    global index, next_char
    if (index + 1) < len(input_string):
        index = index + 1
        next_char = input_string[index]
    elif (index + 1) == len(input_string):
        index += 1
        next_char = '$'

adjacency_matrix = {0:{}}

if not S(input_string, adjacency_matrix):
    print(f"INVALID: {input_string}")
else:
    print(f"VALID: {input_string}")
