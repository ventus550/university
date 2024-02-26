def fio(iput, oput, transform, encoding='utf-8'):
	res = []
	with open(iput, encoding=encoding) as f:
		for line in f:
			line = [int(x) for x in line.strip().split()]
			res.append(line)

	rnum = res[0][0]; cnum = res[0][1];
	rows = res[1:rnum+1]; cols = res[rnum+1:]
	for i in range(len(rows)):
		rows[i] = Partition(cnum, rows[i], "row", i)

	for i in range(len(cols)):
		cols[i] = Partition(rnum, cols[i], "col", i)

	res = transform(rows, cols)
	with open(oput, mode="w", encoding=encoding) as f:
		f.write(res)
