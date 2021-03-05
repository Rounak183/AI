import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
stop_words=set(stopwords.words('english'))

ps=PorterStemmer()

print("Please introduce yourself!")
print("Sample - I am Harsh. A 3 year ECE student in IIITD.")
print()
while True:
	intro=input()
	intro_tokenize=sent_tokenize(intro)

	name=""
	year=0
	branch=""
	for sentence in intro_tokenize:
		wordlist=nltk.word_tokenize(sentence)
		wordlist=[ps.stem(w) for w in wordlist if not w in stop_words]
		tagged=nltk.pos_tag(wordlist)
		for word_tag in tagged:
			word=word_tag[0]
			tag=word_tag[1]
			if tag=='VBP':
				name=word
			if tag=='CD':
				year=word
			if tag=='RB':
				branch=word

	if name!="" and year!=0 and branch!="":
		break
	else:
		print("Please give an input in the form of the sample")
		print()

#print(name,year,branch)
print()

dic={'cse':0,'ece':1,'design':2,'ssh':3,'computational_biolog':4,'applied_math':5,'financ':6}

print("Please state your domains of courses taken during your program: ")
print("Sample - The domains of courses I took are - CSE, ECE, SSH.")
print()
while True:
	done=0
	courses=input()
	wordlist=nltk.word_tokenize(courses)
	wordlist=[ps.stem(w) for w in wordlist if not w in stop_words]
	tagged=nltk.pos_tag(wordlist)

	course_list=[0,0,0,0,0,0,0]
	indices_for_grades=[]
	for word_tag in tagged:
		word=word_tag[0]
		tag=word_tag[1]
		if (tag=='NN' or tag=='RB') and word in dic.keys():	
			index=dic[word]
			indices_for_grades.append(index)
			course_list[index]=1
			done=1

	if done==1:
		break
	else:
		print("Please give an input in the form of the sample")
		print()

#print(course_list)
print()

print("Please state the average grade points received in those domains: ")
print("Sample - The grades I received in the courses were 10, 8.4, 8.8.")
print()
while True:
	grades=input()
	wordlist=nltk.word_tokenize(grades)
	wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
	tagged=nltk.pos_tag(wordlist)
	#print(tagged)

	grade_list=[0,0,0,0,0,0,0]
	done=0
	for word_tag in tagged:
		word=word_tag[0]
		tag=word_tag[1]
		if tag=='CD':
			index=indices_for_grades.pop(0)
			grade_list[index]=float(word)
			done=1

	if done==1:
		break
	else:
		print("Please give an input in the form of the sample")
		print()

#print(grade_list)
print()

print("Did you did any internships in the streams provided by the college?: ")
print("Sample - I did 1 internship in the CSE domain.")
print()
internships=input()
wordlist=nltk.word_tokenize(internships)
wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
tagged=nltk.pos_tag(wordlist)

internship_list=[0,0,0,0,0,0,0]
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if (tag=='NN' or tag=='VBD' or tag=='JJ') and word in dic.keys():
		index=dic[word]
		internship_list[index]=1

#print(internship_list)
print()

print("If you have a significant research experience please state: ")
print("Sample - I have relevant research experience in CSE domain.")
print()
research=input()
wordlist=nltk.word_tokenize(research)
wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
tagged=nltk.pos_tag(wordlist)

research_list=[0,0,0,0,0,0,0]
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if tag=='VBD' or tag=='JJ' or word in dic.keys():
		index=dic[word]
		research_list[index]=1

#print(research_list)
print()

print("Please state if you have some additional project or academic works: ")
print("Sample - I do not have any additional good academic projects.")
print()
projects=input()
wordlist=nltk.word_tokenize(projects)
wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
tagged=nltk.pos_tag(wordlist)

projects_list=[0,0,0,0,0,0,0]
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if (tag=='VBD' or tag=='JJ' or tag=='VBZ') and word in dic.keys():
		index=dic[word]
		projects_list[index]=1

#print(projects_list)
print()

print("Please state if you have specific interest or exceptional achievement: ")
print("Sample - I have specific interests in domain of CSE.")
print()
interests=input()
wordlist=nltk.word_tokenize(interests)
wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
tagged=nltk.pos_tag(wordlist)
#print(tagged)

interests_list=[0,0,0,0,0,0,0]
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if (tag=='NN' or tag=='JJ' or tag=='RB') and word in dic.keys():
		index=dic[word]
		interests_list[index]=1

#print(interests_list)
print()

print("Do you have an LOR or can you be recommended for a job or research in a particular field? ")
print("Sample - Yes, I have done extensive work under Prof. X in the field of CSE.")
print()
lors=input()
wordlist=nltk.word_tokenize(lors)
wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
tagged=nltk.pos_tag(wordlist)
#print(tagged)

lors_list=[0,0,0,0,0,0,0]
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if (tag=='NN' or tag=='JJ') and word in dic.keys():
		index=dic[word]
		lors_list[index]=1

#print(lors_list)
print()

print("How would you rate your coding skills?")
print("Sample - I would say I have good coding skills.")
print()
coding_skills=input()
wordlist=nltk.word_tokenize(coding_skills)
wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
tagged=nltk.pos_tag(wordlist)

coding_skill=0
coding_skills_list=['good','fair','excel','averag','nice']
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if (tag=='JJ' or tag=='VBP') and word in coding_skills_list:
		coding_skill=1
		break

#print(coding_skill)
print()

print("Do you have acknowledgable participation in clubs?")
print("Sample - Yes, I have significant participation in CSE and SSH clubs.")
print()
clubs=input()
wordlist=nltk.word_tokenize(clubs)
wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
tagged=nltk.pos_tag(wordlist)

clubs_list=[0,0,0,0,0,0,0]
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if (tag=='JJ' or tag=='NN') and word in dic.keys():
		index=dic[word]
		clubs_list[index]=1

#print(clubs_list)
print()

print("Have you completed any online courses?")
print("Sample - I have done a few online courses in CSE, ECE and SSH fields.")
print()
online_courses=input()
wordlist=nltk.word_tokenize(online_courses)
wordlist=[ps.stem(w) for w in wordlist if w not in stop_words]
tagged=nltk.pos_tag(wordlist)
#print(tagged)

online_courses_list=[0,0,0,0,0,0,0]
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if (tag=='JJ' or tag=='RB' or tag=='NN') and word in dic.keys():
		index=dic[word]
		online_courses_list[index]=1

#print(online_courses_list)
print()

print("Do you think you can work long hours?")
print("Sample - Yes, I believe I can work long hours.")
print("Sample - No, I donot/don't/do not think I can work long hours.")
print()
long_hours=input()
wordlist=nltk.word_tokenize(long_hours)
tagged=nltk.pos_tag(wordlist)

long_hour=0
long_hours_list=['Yes','can']
long_hours_negation_list=['No',"n't",'not','donot']
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if (tag=='MD' or tag=='UH') and word in long_hours_list:
		long_hour=1
	
	if word in long_hours_negation_list:
		long_hour=0
		break

#print(long_hour)
print()

print("Do you think of ever going for a Phd?")
print("Sample - Yes, I think of going for a Phd.")
print("Sample - No, I have no intention of going for a Phd.")
print()
phd=input()
wordlist=nltk.word_tokenize(phd)
tagged=nltk.pos_tag(wordlist)

phd_val=0
phd_list=['Yes','can','will']
phd_negation_list=['No',"n't",'not','donot']
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if word in phd_list:
		phd_val=1

	if word in phd_negation_list:
		phd_val=0
		break

#print(phd_val)
print()

print("Does it ever come to you of establishing your own startup?")
print("Sample - Yes, I have a few ideas.") 
print("Sample - No, I haven't thought in that direction. But maybe in the future.")
print()
startup=input()
wordlist=nltk.word_tokenize(startup)
tagged=nltk.pos_tag(wordlist)

startup_val=0
startup_list=['Yes','will','can']
startup_negation_list=['No',"n't",'not','donot']
for word_tag in tagged:
	word=word_tag[0]
	tag=word_tag[1]
	if word in startup_list:
		startup_val=1

	if word in startup_negation_list:
		startup_val=0
		break

#print(startup_val)	

''' Inputs are -

name, year,branch
course_list
grade_list
internship_list
research_list
projects_list
interests_list
lors_list
coding_skill
clubs_list
online_courses_list
long_hour
phd_val
startup_val
'''

# Writing in the facts file.

out=open("factsfile.txt","w")
name_fact="name("+str(name)+")."
out.write(name_fact)
out.write('\n')
year_fact="year("+str(year)+")."
out.write(year_fact)
out.write('\n')
branch_fact="branch("+str(branch)+")."
out.write(branch_fact)
out.write('\n')
course_list_fact="course_list("+str(course_list)+")."
out.write(course_list_fact)
out.write('\n')
grade_list_fact="grade_list("+str(grade_list)+")."
out.write(grade_list_fact)
out.write('\n')
internship_list_fact="internship_list("+str(internship_list)+")."
out.write(internship_list_fact)
out.write('\n')
research_list_fact="research_list("+str(research_list)+")."
out.write(research_list_fact)
out.write('\n')
projects_list_fact="projects_list("+str(projects_list)+")."
out.write(projects_list_fact)
out.write('\n')
interests_list_fact="interests_list("+str(interests_list)+")."
out.write(interests_list_fact)
out.write('\n')
lors_list_fact="lors_list("+str(lors_list)+")."
out.write(lors_list_fact)
out.write('\n')
coding_skill_fact="coding_skill("+str(coding_skill)+")."
out.write(coding_skill_fact)
out.write('\n')
clubs_list_fact="clubs_list("+str(clubs_list)+")."
out.write(clubs_list_fact)
out.write('\n')
online_courses_list_fact="online_courses_list("+str(online_courses_list)+")."
out.write(online_courses_list_fact)
out.write('\n')
long_hour_fact="long_hour("+str(long_hour)+")."
out.write(long_hour_fact)
out.write('\n')
phd_val_fact="phd("+str(phd_val)+")."
out.write(phd_val_fact)
out.write('\n')
startup_fact="startup("+str(startup_val)+")."
out.write(startup_fact)
out.write('\n')
out.close()
