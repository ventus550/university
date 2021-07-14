from fio import fio

def solve(line):

	line = line.split()
	bits = [int(x) for x in line[0]]; block = int(line[1])
	line_max = sum(bits)


	operations = len(bits)
	for i in range(len(bits)-block+1):
		block_max = sum(bits[i:i+block])
		calc = line_max + block - 2*block_max
		if operations > calc:
			operations = calc

	return str(operations)


fio("zad4_input.txt", "zad4_output.txt", solve)
