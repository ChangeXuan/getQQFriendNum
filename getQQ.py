#encoding=utf-8
def showNum(s,oth=''):
    fomart = '0123456789'
    for c in s:
        if not c in fomart:
            s = s.replace(c,'');
    return s;

all_data = []

with open('xxx.csv' , 'rt') as f:
	for num in f:
		d = '@qq'
		num = num[num.find(d) + 1:]
		all_data.append(showNum(num)+"\n")

f = open("QQNUM.txt","w+")
f.writelines(all_data)
f.close