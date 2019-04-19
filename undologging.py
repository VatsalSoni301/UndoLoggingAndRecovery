import sys
import copy
disc = {}
m = {}
a = []
varx={}
local1 = {}
active = []
i = 0
fname = sys.argv[1]
q = int(sys.argv[2])
mz=[]
transactions = {}
mapping = {}
mm = 0
flag = 0
fout = open("2018201005_1.txt", "w")

with open(fname,'r') as f:
	c = 0
	for line in f:
		if c == 0:
			var = line.split(" ")
			i = 0
			while i < len(var):
				disc[var[i]]=int(var[i+1])
				m[var[i]]=int(var[i+1])
				i=i+2
		else:
			if flag == 1:
				var = line.split(" ")
				mapping[var[0]]=mm
				mapping[mm]=var[0]
				varx[mm]=[]
				transactions[mm]=[]
				mm = mm + 1
				at = var[0]
				flag = 0
			else:
				if line=="\n":
					flag = 1
				else:
					flag = 0
					# print(at)
					transactions[mapping[at]].append(line)

		c = c + 1

# print("DDDDDDDDDDDDDDDDDDDD")
# print(disc)
# print("MMMMMMMMMMMMMMMMMMMM")
# print(m)
# print("TTTTTTTTTTTTTTTTTTTTTTT")
# print(transactions)

maxlen = 0

for i in transactions.keys():
	if maxlen < len(transactions[i]):
		maxlen = len(transactions[i])

i = 0
while i < maxlen:

	for j in transactions.keys():
		x = 0
		while x < q :
			if x+i<len(transactions[j]):
				a.append((j,transactions[j][x+i]))
				x = x + 1 
			else:
				break

	i = i + q

# print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
# print(a)

trans = map(lambda x: (x[0], x[1].strip("\n")), a)

nl = 0
for i in trans:
	
	if i[0] not in active:
		active.append(i[0])
		wr = '<START '+ mapping[i[0]]+'>'
		fout.write(wr)
		fout.write("\n")
		kk = m.keys()
		kk.sort()
		sp = 0
		for w in kk:
			if w in mz:
				if sp == 0:
					wr = w+" "+str(m[w])
				else:
					wr = " "+w+" "+str(m[w])
				sp = sp + 1
				fout.write(wr)
		fout.write("\n")
		kk = disc.keys()
		kk.sort()
		sp = 0
		for w in kk:
			if sp == 0:
				wr = w +" "+ str(disc[w])
			else:
				wr = " "+w +" "+ str(disc[w])
			sp = sp + 1
			fout.write(wr)
		fout.write("\n")
	
	e = i[1]
	
	if '=' in e:
		
		temp = e.split(':=')
		temp = map(lambda x: x.strip(), temp)
		m1=copy.deepcopy(m)
		local1[temp[0]] = eval(temp[1], m1, local1)

	if 'READ' in e:
		
		temp = e.split('(')[1].split(')')[0].split(',')
		temp = map(lambda x: x.strip(), temp)
		local1[temp[1]] = m[temp[0]]
		if temp[0] not in varx[i[0]]:
			mz.append(temp[0])
			varx[i[0]].append(temp[0])

	if 'WRITE' in e:
		
		temp = e.split('(')[1].split(')')[0].split(',')
		temp = map(lambda x: x.strip(), temp)

		wr = '<'+mapping[i[0]]+', '+temp[0]+', '+str(m[temp[0]])+'>'
		fout.write(wr)
		fout.write("\n")
		m[temp[0]] = local1[temp[1]]
		kk = m.keys()
		kk.sort()
		sp = 0
		for w in kk:
			if w in mz:
				if sp == 0:
					wr = w+" "+str(m[w])
				else:
					wr = " "+w+" "+str(m[w])
				sp = sp + 1
				fout.write(wr)
		fout.write("\n")
		kk = disc.keys()
		kk.sort()
		sp = 0
		for w in kk:
			if sp == 0:
				wr = w+" "+str(disc[w])
			else:
				wr = " "+w+" "+str(disc[w])
			sp = sp + 1
			fout.write(wr)
		fout.write("\n")

	if 'OUTPUT' in e:
		
		temp = e.split('(')[1].split(')')[0]
		disc[temp] = m[temp]
		l = varx[i[0]]
		l.remove(temp)
		if len(l) == 0:
			wr = '<COMMIT '+ mapping[i[0]]+'>'
			fout.write(wr)
			fout.write("\n")
			kk = m.keys()
			kk.sort()
			sp = 0
			for w in kk:
				if w in mz:
					if sp == 0:
						wr=w+" "+str(m[w])
					else:
						wr=" "+w+" "+str(m[w])
					fout.write(wr)
					sp = sp + 1

			fout.write("\n")
			kk = disc.keys()
			kk.sort()
			sp = 0
			for w in kk:
				if sp == 0:
					wr=w+" "+str(disc[w])
				else:
					wr = " "+w+" "+str(disc[w])
				fout.write(wr)
				sp = sp + 1
			if nl != len(trans)-1:
				fout.write("\n")
	nl = nl + 1
fout.close()
# file = open("2018201005_1.txt", "r")
# lines = file.readlines()
# file.close()
# file = open("2018201005_1.txt", "w")
# for i in lines:
# 	file.write(i)
# file.close()