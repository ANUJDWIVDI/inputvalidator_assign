# Function to check if a string is accepted by the given regular expression
def S(input_string, adjacency_matrix):
    global index
    index = 0
    initial_state = '0'
    adjacency_matrix[initial_state] = {}

    if not T(input_string, initial_state, adjacency_matrix):
        return False

    if not Q(input_string, adjacency_matrix):
        return False

    add_final_states(adjacency_matrix)
    print_adjacency_matrix(adjacency_matrix)
    return index == len(input_string)


# Function to handle concatenation in the regular expression
def R(input_string, current_state, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] in ('(', 'a', 'b'):
        next_state = F(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        current_state = next_state

        # Recursively handle concatenation
        next_state = R(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False

        # Add epsilon transition for concatenation
        add_transition(adjacency_matrix, current_state, next_state, 'ε')
        return next_state
    return True


# Recursive function to parse the regular expression
def T(input_string, current_state, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] in ('(', 'a', 'b'):
        next_state = F(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        current_state = next_state

        # Check for concatenation
        next_state = R(input_string, current_state, adjacency_matrix)
        if next_state is None:
            return False
        return next_state
    return False


# Function to handle Kleene star (*) in the regular expression
def U(input_string, current_state, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] == '*':
        index += 1
        next_state = add_state(adjacency_matrix)
        add_transition(adjacency_matrix, current_state, next_state, 'ε')
        add_transition(adjacency_matrix, next_state, current_state, 'ε')
        next_state = U(input_string, next_state, adjacency_matrix)
        if next_state is None:
            return False
        return next_state
    return current_state


# Recursive function to handle expressions enclosed in parentheses
def E(input_string, current_state, adjacency_matrix):
    global index
    if not T(input_string, current_state, adjacency_matrix):
        return False

    if not Q(input_string, adjacency_matrix):
        return False

    if index < len(input_string) and input_string[index] == ')' and index + 1 != len(input_string):
        return True
    elif index < len(input_string) and input_string[index] == 'ε':
        next_state = add_state(adjacency_matrix)
        add_transition(adjacency_matrix, current_state, next_state, 'ε')
        return E(input_string, next_state, adjacency_matrix)
    return False


# Function to handle factors in the regular expression (a, b, or expressions in parentheses)
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




# Function to handle '|' and '+' operators
def Q(input_string, adjacency_matrix):
    global index
    if index < len(input_string) and input_string[index] in ('|', '+'):
        index += 1
        if index < len(input_string):
            if not T(input_string, '0', adjacency_matrix):  # Start from state '0'
                return False
            if not Q(input_string, adjacency_matrix):
                return False
            return True
        else:
            return False
    return True





# Function to add a new state to the adjacency matrix
def add_state(adjacency_matrix):
    state_name = str(len(adjacency_matrix))
    adjacency_matrix[state_name] = {}
    return state_name


# Function to add a transition to the adjacency matrix
def add_transition(adjacency_matrix, from_state, to_state, symbol):
    if from_state not in adjacency_matrix:
        adjacency_matrix[from_state] = {}
    adjacency_matrix[from_state].setdefault(symbol, []).append(to_state)


# Function to identify and mark final states in the adjacency matrix
def add_final_states(adjacency_matrix):
    for state, transitions in adjacency_matrix.items():
        if '$' in transitions and len(transitions['$']) > 0:
            for final_state in transitions['$']:
                adjacency_matrix[final_state] = {}  # Reset transitions for final states


# Function to print the adjacency matrix representing the NFA
def print_adjacency_matrix(adjacency_matrix):
    print("Expression accepted")
    print("State    a    b    ε")
    for state, transitions in sorted(adjacency_matrix.items(), key=lambda item: int(item[0]) if item[0] != 'ie' else float('inf')):
        if state != 'ie':
            a_transitions = "[" + ", ".join(transitions.get('a', [])) + "]"
            b_transitions = "[" + ", ".join(transitions.get('b', [])) + "]"
            e_transitions = "[" + ", ".join(map(str, transitions.get('ε', []))) + "]" if 'ε' in transitions else "[]"
            print(f"{state:<9}{a_transitions:<5}{b_transitions:<5}{e_transitions}")

    print("NFA States")
    start_state = next(iter(adjacency_matrix.keys()))
    accept_states = [state for state, transitions in adjacency_matrix.items() if '$' in transitions and len(transitions['$']) > 0]
    print("start:", start_state)
    print("accept:", " : True")


# Main code
print("Enter a Regular input_string! ")
input_string = input()

def remove_whitespace(input_string):
    return input_string.replace(" ", "")

input_string = remove_whitespace(input_string)

index = 0
next_char = input_string[0]

adjacency_matrix = {'0': {}}  # Initialize adjacency matrix with start state '0'

if not S(input_string, adjacency_matrix):
    print(f"INVALID: {input_string}")
else:
    print(f"VALID: {input_string}")
