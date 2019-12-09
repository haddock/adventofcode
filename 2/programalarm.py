def do(program, offset = 0):
    opcode = program[offset]
    if opcode == 99:
        return program
    
    firstargposition = program[offset + 1]
    secondargposition = program[offset + 2]
    targetposition = program[offset + 3]

    if opcode == 1:
        result = program[firstargposition] + program [secondargposition]
    elif opcode == 2:
        result = program[firstargposition] * program [secondargposition]
    program.pop(targetposition)
    program.insert(targetposition, result)
    return do(program, offset+4)

def dofromfile(filename):
    f = open(filename)
    program = list(map(int, f.readline().split(',')))
    program[1] = 12
    program[2] = 2
    print(do(program)[0])
if __name__ == '__main__':
    dofromfile("program.txt")