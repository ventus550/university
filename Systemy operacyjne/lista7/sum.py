from glob import glob

VmSize = VmRSS = 0

files = glob("/proc/**/status")
for f in files:
	for line in open(f, 'r'):
		line = line.split()
		if 'VmSize:' in line: VmSize += int(line[1])
		if 'VmRSS:' in line: VmRSS += int(line[1])

print(f"VmSize: {VmSize} kB\nVmRSS: {VmRSS} kB")