import sys


def universal_turing(n, r, tr, a, w):
    global output, head, limit_head
    output = w
    head = 0

    allowed = {'a', 'b', 'R', 'L'}

    # Check if the tape symbols are within the allowed symbols
    if all(symbol in allowed for symbol in w[1:-1]) and w[0] == '<' and w[-1] == '>':
        limit_head = len(output)
        for x in range(r):
            output_print = ''.join(tr_perform(tr[x]))
            print("RULE : ", x + 1)
            print(output_print)
    else:
        print("Invalid tape symbols. The tape symbols must be within the allowed symbols:", allowed)


def tr_perform(tr):
    global output, head, limit_head
    start_state = tr[0]
    symbol_check = tr[1]
    final_state = tr[2]
    replace_symbol = tr[3]
    direction = tr[4]

    output = [char for char in output]

    output_print = output

    if start_state == final_state:
        # Loop until the next symbol is not found
        while output[head] == symbol_check:
            pos = head

            output[pos] = replace_symbol

            # Move the head according to the direction
            if direction == 'R':
                head += 1
                pos = head
            elif direction == 'L':
                head -= 1
                pos = head

            # Check if head is out of bounds
            if head < 0:
                output = ['_'] + output
                head = 0
                pos = head
            elif head >= limit_head:
                output = output + ['_']
                limit_head += 1
                pos = head

            before = output[:pos]
            after = output[pos:]
            output_print = before + [final_state] + after

    else:
        # Non-looping rule
        pos = head

        before = output[:pos]
        after = output[pos:]

        if symbol_check == output[pos]:
            output[pos] = replace_symbol
            output_print = before + [final_state] + after

            # Move the head according to the direction
            if direction == 'R':
                head += 1
            elif direction == 'L':
                head -= 1

            # Check if head is out of bounds
            if head < 0:
                output = ['_'] + output
                head = 0
            elif head >= limit_head:
                output = output + ['_']
                limit_head += 1

        else:
            sys.stderr.write("Symbol not found")
            sys.exit(1)

    return ''.join(output_print)


def main():
    global output, head

    n = 5
    r = 11

    tr = [
        "0<0<R",
        "0a1xR",
        "1a1aR",
        "1y1yR",
        "1b2yL",
        "2y2yL",
        "2a2aL",
        "2x0xR",
        "0y3yR",
        "3y3yR",
        "3>4>R"
    ]

    a = 4
    w = "<aabb>"
    output = w
    head = 0
    universal_turing(n, r, tr, a, w)


if __name__ == "__main__":
    main()
