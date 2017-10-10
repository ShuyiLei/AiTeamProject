import csv
with open('validation_set.tsv') as f:
	with open('res.tsv','w+') as g:
		reader = csv.reader(f,delimiter='\t')
		reader.next();
		g.write("id,correctAnswer\n")
		for row in reader:
			g.write(row[0]+',A\n')
