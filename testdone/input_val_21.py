global regex_input
def run_check():
    import subprocess

    process = subprocess.Popen(['python', 'input_val_2.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    global regex_input
    regex_input = input("Enter a regular expression: ")  # Assign a value separately

    process.stdin.write(bytes(regex_input + '\n', 'utf-8'))
    process.stdin.flush()

    output, error = process.communicate()

    output_message = output.decode('utf-8')
    error_message = error.decode('utf-8')

    print(output_message)

    if error_message:
        print(error_message)

run_check()

print(regex_input)


index = 0
next_char = regex_input[0]
def get_next_char():  # Function that helps fetch the preceeding character .
    global index, next_char
    if (index + 1) < len(regex_input):
        index = index + 1
        next_char = regex_input[index]
    elif (index + 1) == len(regex_input):
        index += 1
        next_char = '$'

y=0
flag=[]

for x in regex_input:
    if x == '(':
        flag[y]=1
        y+=1
        get_next_char()
        continue
    if x == '+':




