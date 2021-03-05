file1=open('roaddistance.txt','r')
lines=file1.readlines()

#print(lines)
columncitiesline=lines[1].split()
columncities=[]
for city in columncitiesline[3:]:
	columncities.append(city)

#print(columncities)

distances={}
for i in range(2,len(lines)):
	row=lines[i].split()
	#print(row)
	distances[row[0]]={}
	for j in range(1,len(row)):
		ele=row[j]
		if ele=='-':
			distances[row[0]][columncities[j-1]]=0
		else:
			distances[row[0]][columncities[j-1]]=int(ele)

for j in range(len(columncities)):
	columncity=columncities[j]
	if columncity not in distances.keys():
		distances[columncity]={}
	for i in range(2,len(lines)):
		row=lines[i].split()
		rowcity=row[0]
		if rowcity!=columncity:
			distances[columncity][rowcity]=row[j+1]

#print(distances)

for ele in distances.keys():
	dic=distances[ele]
	#print(dic)
	#print()
	for city in dic.keys():
		if ele!=city:
			string="move("+ele.lower()+','+city.lower()+','+str(dic[city])+")."
			print(string)

