writeList([]).
writeList([H|T]):-
	write(H),nl,
	writeList(T).

% Getting the element at the specified number in list.
getElement(X,[X|_],1).
getElement(X,[_|L],K):-
	getElement(X,L,K1), K is K1+1.

% Consulting the facts file and accessing the facts.
main:-
	consult('factsfile.txt'),
	name(Name),
	year(Year),
	branch(Stream),
	course_list(Courses),
	startPrediction(Courses).

% Get Grades in the Courses.
startPrediction(L):-
	grade_list(Grades),
	getSkills(Grades).

% Get Internships, Research, additional works.
getSkills(Grades):-
	internship_list(Internships),
	research_list(Research),
	projects_list(AddWorks),
	getAptitude(Grades,Internships,Research,AddWorks).

% Get Exceptional achievement, LORs, Coding_Skill, Clubs, Online Courses. 
getAptitude(Grades,Internships,Research,AddWorks):-
	interests_list(Exceptional),
	lors_list(LORs),
	coding_skill(Coding_Skill),
	clubs_list(Clubs),
	online_courses_list(Other_Courses),
	ingenuityConsideration(Grades,Ingenuity,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses).

% Considering Ingenuity.
ingenuityConsideration(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses):-
	long_hour(Long_Hours),
	phd(PhD),
	startup(Startup),
	printPrediction(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup).

% Printing Prediction of oppurtunities, future
printPrediction(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup):-
	getElement(GradeCSE,Grades,1),
	write('Below are all possible predictions of your future : '),nl,
	addCodingJob(Coding_Skill,GradeCSE),
	addStartup(Startup,Long_Hours),
	considerCSE(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup),
	considerECE(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup),
	considerDesign(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup),
	considerSSH(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup),
	considerCB(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup),
	considerAM(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup),
	considerFinance(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup).

% Prediction for CSE profiles.
considerCSE(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup):-
	getElement(GradeCSE,Grades,1),
	getElement(InternCSE,Internships,1),
	getElement(ResearchCSE,Research,1),
	getElement(AddCSE,AddWorks,1),
	getElement(ExceptionalCSE,Exceptional,1),
	getElement(LORsCSE,LORs,1),
	getElement(ClubsCSE,Clubs,1),
	getElement(OtherCSE,Other_Courses,1),
	((GradeCSE>=8.5,(InternCSE==1;ExceptionalCSE==1;(OtherCSE==1,ClubsCSE==1)))->
		write('Web Developer, Front-end/Back-end Developer.'),nl;
		write('')),
	((GradeCSE>=9,(ResearchCSE==1;AddCSE==1;LORsCSE==1))->
		write('Masters, Researcher, Professor in CSE fields.'),nl;
		write('')),
	((GradeCSE>=9,(ResearchCSE==1;AddCSE==1;LORsCSE==1;PhD==1))->
		write('PhD in CSE fields.'),nl;
		write('')).

% Prediction for ECE profiles.
considerECE(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup):-
	getElement(GradeECE,Grades,2),
	getElement(GradeCSE,Grades,1),
	getElement(InternECE,Internships,2),
	getElement(InternCSE,Internships,1),
	getElement(ResearchECE,Research,2),
	getElement(AddECE,AddWorks,2),
	getElement(ExceptionalECE,Exceptional,2),
	getElement(LORsECE,LORs,2),
	getElement(ClubsECE,Clubs,2),
	getElement(OtherECE,Other_Courses,2),
	((GradeECE>=8.7,(InternECE==1;ExceptionalECE==1;(OtherECE==1,ClubsECE==1)))->
		write('Hardware Engineer,Communications Engineer'),nl;
		write('')),
	((GradeECE>=8.7,(InternCSE==1;InternECE==1;ExceptionalECE==1))->
		write('Computer Engineer'),nl;
		write('')),
	((GradeECE>=8.7,(ResearchECE==1;ExceptionalECE==1;LORsECE==1;AddECE==1))->
		write('PhD. in ECE core, Researcher, Robotics'),nl;
		write('')).

% Prediction for Design Profiles.
considerDesign(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup):-
	getElement(GradeDesign,Grades,3),
	getElement(InternDesign,Internships,3),
	getElement(ResearchDesign,Research,3),
	getElement(AddDesign,AddWorks,3),
	getElement(ExceptionalDesign,Exceptional,3),
	getElement(LORsDesign,LORs,3),
	getElement(ClubsDesign,Clubs,3),
	getElement(OtherDesign,Other_Courses,3),
	((GradeDesign>=8.5,(InternDesign==1;ExceptionalDesign==1;(OtherDesign==1,ClubsDesign==1)))->
		write('UI/UX Design engineer,Graphic Designer.'),nl;
		write('')),
	((GradeDesign>=9,(ResearchDesign==1;LORsDesign==1))->
		write('Research in Design fieds as app-development, new Graphic fonts'),nl;
		write('')).

% Prediction for SSH Profiles.
considerSSH(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup):-
	getElement(GradeSSH,Grades,4),
	getElement(InternSSH,Internships,4),
	getElement(ResearchSSH,Research,4),
	getElement(AddSSH,AddWorks,4),
	getElement(ExceptionalSSH,Exceptional,4),
	getElement(LORsSSH,LORs,4),
	getElement(ClubsSSH,Clubs,4),
	getElement(OtherSSH,Other_Courses,4),
	((GradeSSH>=8.3,(InternSSH==1;OtherSSH==1;AddSSH==1;ExceptionalSSH==1;ClubsSSH==1))->
		write('Public Speaker, Environmentalist, Social Server'),nl;
		write('')),
	((GradeSSH>=8.5,(ExceptionalSSH==1,LORsSSH==1,ResearchSSH==1))->
		write('Professor in the SSH field preferred'),nl,
		write('Phsycologist, Philanthrophist.'),nl;
		write('')).

% Prediction for CB Profiles.
considerCB(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup):-
	getElement(GradeCB,Grades,5),
	getElement(GradeCSE,Grades,1),
	getElement(InternCB,Internships,5),
	getElement(ResearchCB,Research,5),
	getElement(AddCB,AddWorks,5),
	getElement(ExceptionalCB,Exceptional,5),
	getElement(LORsCB,LORs,5),
	getElement(ClubsCB,Clubs,5),
	getElement(OtherCB,Other_Courses,5),
	(((GradeCB>=8.5;GradeCSE>=9),(InternCB==1;ExceptionalCB==1;(OtherCB==1,ClubsCB==1)))->
		write('ML enthusiast in Biomedical fields'),nl,
		write('Computational Biology, Human Anatomy, Genome fields'),nl;
		write('')),
	(((GradeCB>=8.5;GradeCSE>=9),(ResearchCB==1;LORsCB==1;ExceptionalCB==1))->
		write('Research in Computational Biology'),nl;
		write('')).

% Prediction for AM Profiles.
considerAM(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup):-
	getElement(GradeAM,Grades,6),
	getElement(GradeCSE,Grades,1),
	getElement(InternAM,Internships,6),
	getElement(ResearchAM,Research,6),
	getElement(AddAM,AddWorks,6),
	getElement(ExceptionalAM,Exceptional,6),
	getElement(LORsAM,LORs,6),
	getElement(ClubsAM,Clubs,6),
	getElement(OtherAM,Other_Courses,6),
	((GradeAM>=8.5,GradeCSE>=8.5,(InternAM==1;(OtherAM==1,ClubsAM==1);ExceptionalAM==1))->
		write('Investment analysis fields, Data Analysis fields'),nl;
		write('')),
	((GradeAM>=9,AddAM==1,OtherAM==1)->
		write('Further Maths studies and fields'),nl;
		write('')),
	((GradeAM>=9,(ResearchAM==1;LORsAM==1))->
		write('Professor in mathematics, further studies like Masters or PhD.'),nl;
		write('')).

% Prediction for Finance Profiles.
considerFinance(Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup):-
	getElement(GradeFinance,Grades,7),
	getElement(GradeCSE,Grades,1),
	getElement(InternFinance,Internships,7),
	getElement(ResearchFinance,Research,7),
	getElement(AddFinance,AddWorks,7),
	getElement(ExceptionalFinance,Exceptional,7),
	getElement(LORsFinance,LORs,7),
	getElement(ClubsFinance,Clubs,7),
	getElement(OtherFinance,Other_Courses,7),
	((GradeFinance>=9,GradeCSE>=8.5,(InternFinance==1;(OtherFinance==1,ClubsFinance==1);ExceptionalFinance==1))->	
		write('Analyist at Banking Firms, Cyber-Security fields in banks'),nl;
		write('')),
	((GradeFinance>=9,InternFinance==1,(OtherFinance==1;ClubsFinance==1))->
		write('Investment Banker'),nl;
		write(''),nl).

% Prediction for an SDE job.
addCodingJob(Coding_Skill,GradeCSE):-
	Coding_Skill==1,GradeCSE>=8.5->
		write('Software Development Engineer'),nl;
		write('').

% Prediction for Startup.
addStartup(Startup,Long_Hours):-
	Startup==1,Long_Hours==1->
		write('Possibilty of Startup'),nl;
		write('').

% Prediction for PhD after job.
addPhD(PhD):-
	((PhD==1)->
		write('Possibility of PhD during job or after graduation.'),nl;
		write('')).

% Grades,Internships,Research,AddWorks,Exceptional,LORs,Coding_Skill,Clubs,Other_Courses,Long_Hours,PhD,Startup*/