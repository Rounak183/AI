import random

file1=open('roaddistance.txt','r')
lines=file1.readlines()

#print(lines)
columncitiesline=lines[1].split()
columncities=[]
for city in columncitiesline[3:]:
	columncities.append(city.lower())

#print(columncities)

distances={}
for i in range(2,len(lines)):
	row=lines[i].split()
	#print(row)
	distances[row[0].lower()]={}
	for j in range(1,len(row)):
		ele=row[j]
		if ele=='-':
			distances[row[0].lower()][columncities[j-1]]=0
		else:
			distances[row[0].lower()][columncities[j-1]]=int(ele)

for j in range(len(columncities)):
	columncity=columncities[j]
	if columncity not in distances.keys():
		distances[columncity.lower()]={}
	for i in range(2,len(lines)):
		row=lines[i].split()
		rowcity=row[0].lower()
		if rowcity!=columncity:
			distances[columncity.lower()][rowcity]=row[j+1]

#print(distances.keys())
source="agartala"
goal="ahmedabad"

for ele in distances.keys():
	dic=distances[ele]
	#print("ele = ",ele," dic = ",dic)
	#print()
	if ele==goal:
		string="heuristic("+goal+","+goal+","+str(0)+")."
		print(string)
	else:
		if goal in dic.keys():
			heuristic=int(dic[goal])
			#print("heuristic = ",heuristic," ele = ",ele)
			num=random.randint(20,30)
			heuristic_distance=heuristic-num
			string="heuristic("+ele.lower()+','+goal.lower()+','+str(heuristic_distance)+")."
			print(string)
		else:
			best_heuristic=[]
			for city in dic.keys():
				dic2=distances[city]
				if goal in dic2.keys():
					seconddistance=dic2[goal]
					firstdistance=dic[city]
					heuristic=int(firstdistance)+int(seconddistance)
					num=random.randint(30,40)
					heuristic_distance=heuristic-num
					best_heuristic.append(heuristic_distance)
			most_suitable_heuristic=min(best_heuristic)
			string="heuristic("+ele.lower()+','+goal.lower()+','+str(most_suitable_heuristic)+")."
			print(string)

