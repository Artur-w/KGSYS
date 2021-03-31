"""
File contining some example sentences.




"""
txt = "An engineer had to plan the construction of an artificial lake to produce electric energy."
txt2 = "An engineer had to plan the construction of an artificial lake to produce electric energy. To feed the lake he thought to build a unique wide canal collecting water coming from a near valley. However, a mason pointed out that during the flood periods the stream of water flowing along the canal might be too strong and might damage the surrounding areas; by contrast, during the drought periods a unique stream of water might be insufficient to feed the lake. In order to avoid these mishaps, the mason suggested to build, instead of a unique wide canal, four small canals whose total flow was the same as the unique wide canal previously planned. These small canals were placed around the lake so that they conveyed water coming from four different valleys. In this way only small amounts of water could flow in each canal and thus during flood periods dangerous overflowing might not occur. At the same time, the lake was fed by water from various belts, so that also during drought periods it was sufficiency that the fed."
txt3="Because of their wellknown stance as activists, many members of the faculty have been called to testify before Congress."
txt4="As a result, many members of this department have become recognizable faces on television news programs."
txt5="The English department faculty also have excellent reputations as teachers."
txt6="Not only are the faculty in this department extremely bright, they are able to enter the �beginner�s mind� and present material in a clear engaging manner."

# Arguments: subject-related (Subject Dependency)
# nsubj - (nominal subject)
# advmod
ex0 = "This house is pretty."
ex1 = "She and I came home together"
ex2 = "Earlier was better."
ex3 = "She grew older."
# nsubjpass (passive nominal subject)
ex4 = "I am drawn to her."
ex5 = "We will get married."
ex6 = "She will become nationalized."
ex7 = "The car was bought by John."
# csubj (clausal subject)
ex8 = "Whether she liked me doesn’t matter"
ex9 = "What you have to say is not important."
# csubjpass (clausal passive subject)
ex10 = "Whoever misbehaves will be dismissed"
ex11 = "Whether you come will be recorded."
# agent (agent) - complement of a passive verb
ex12 = "decisions made by those"
ex13 = "this was not carried out by immigrants"
# expl (expletive)
ex14 = "There was an explosion"
ex15 = "There seems to be a mistake."
# dobj (direct object)
ex16 =  "She bought me these books"
ex17 = "Minorities face inequalities."
ex18 = "She gave her a book."
# dative (indirect object)
ex19 = "She bought me these books"
ex20 = "She bought these books for me"
ex21 = "She bought me these books."
ex22 = "She gave her a book."
ex23 = "She gave a book to her."
# attr (attribute)
ex24 = "This product is a global brand"
ex25 = "This is our house."
ex26 = "Beliefs are part of a legacy."
ex27 = "Boys will be boys."
# oprd (object predicate)
ex28 = "She calls me her friend"
ex29 = "I am considered her friend"
ex30 = "She seems tired."
ex31 = "She grows older every day."
# AUX ( auxiliary )
ex32 = "I have been seeing her"
ex33 = "I decided to go home."
ex34 = "Boys will be boys."
ex35 = "I don’t like to be bothered."
# AUXPASS (passive auxiliary)
ex36 = "I am drawn to her."
ex37 = "I am struck by her beauty."
ex38 = "I don’t like to be bothered."
# BIOSCIENCE AND MEDICAL RELATED TEXTS
biosci01 = """Myeloid derived suppressor cells (MDSC) are immature
# myeloid cells with immunosuppressive activity.
# They accumulate in tumor-bearing mice and humans
# with different types of cancer, including hepatocellular
# carcinoma (HCC)."""
fox = "The brown fox is quick, and he is jumping over the lazy dog"

covtext = """
                **`Science` ’s COVID-19 reporting is supported by the Pulitzer Center and the Heising-Simons Foundation.**
                This fall, cardiologist Sam Mohiddin will embrace a new role—that of research subject. MRI scans of his heart at St. Bartholomew’s Hospital in London, where he works, will help answer a pressing question: Do people who suffered a mild or moderate bout of COVID-19 months ago, as he did, need to worry about their heart health?
                Fears that COVID-19 can cause the cardiac inflammation called myocarditis have grown, as doctors report seeing previously healthy people whose COVID-19 experience is trailed by myocarditis-induced heart failure. Mohiddin recently treated 42-year-old Abul Kashem, who had typical COVID-19 symptoms in April, including loss of smell and mild shortness of breath. A month later, he fell critically ill from severe myocarditis. “I’m just grateful to be alive,” says Kashem, who spent more than 2 weeks in an intensive care unit. Why did this happen? he wonders.
                How the virus might damage heart muscle is just one question researchers are now probing. Other studies are following people during and after acute illness to learn how common heart inflammation is after COVID-19, how long it lingers, and whether it responds to specific treatments. Researchers also want to know whether patients fare similarly to those with myocarditis from other causes, which can include chemotherapy and other viruses. In more than half of virus-induced cases, the inflammation resolves without incident.
                But some cases lead to arrhythmia and impaired heart function, or, rarely, the need for a heart transplant. Because millions are now contracting the coronavirus, even a small proportion who suffer severe myocarditis would amount to a lot of people. “Are we going to have an increase of patients with heart failure secondary to this?” asks Peter Liu, a cardiologist and chief scientific officer of the University of Ottawa Heart Institute.
                Whether SARS-CoV-2, the virus that causes COVID-19, induces cardiac injury including myocarditis more often, or with greater severity, than other viruses is still unclear. Because SARS-CoV-2 can trigger an intense immune response throughout the body, survivors may be at heightened risk of cardiac inflammation. Another idea suggests COVID-19 patients might be prone to the condition because the virus enters cells by binding with the angiotensin-converting enzyme 2 (ACE2) receptor, which sits on heart muscle cells. But researchers caution against outrunning the data. “It’s a good hypothesis, but it’s not a tested one,” says Leslie Cooper, a cardiologist at the Mayo Clinic in Jacksonville, Florida, about ACE2.
                One reason it’s hard to say whether COVID-19 poses a special risk of myocarditis is uncertainty about its prevalence after other infections. Echocardiogram studies after some influenza outbreaks suggest up to 10% of flu patients have transient heart abnormalities, Liu says. But such studies are scarce. “We don’t scan patients after they had the flu,” says Valentina Püntmann, a cardiologist at University Hospital Frankfurt.
                Püntmann fueled concerns about myocarditis when she did just that with COVID-19 patients. Her team used MRI to scan the hearts of 100 COVID-19 patients an average of 71 days after they had tested positive. The scans showed cardiac abnormalities in 78 people, with 60 appearing to have active inflammation. Most also described lingering symptoms, such as fatigue and mild shortness of breath, leading Püntmann to wonder whether heart inflammation might be responsible.
                Although [the work by Püntmann and her colleagues](https://jamanetwork.com/journals/jamacardiology/fullarticle/2768916), published in July in *JAMA Cardiology*, prompted alarming headlines, many researchers say it needs to be replicated. Cardiologists urge anyone with symptoms like shortness of breath or chest discomfort after COVID-19 to see a doctor, but they worry about a flood of healthy recovered people clamoring for heart assessments. “Here’s the good news: We’re going to find out” how likely cardiac injury is, says Matthew Martinez, director of sports cardiology at Morristown Medical Center.
                Because of the physical demands of sports, team doctors need to be on guard for myocarditis. A paper in *JAMA Cardiology* last week reported a study of 26 athletes at Ohio State University after COVID-19; four had developed myocarditis. Professional sports leagues are also scanning the hearts of athletes who were infected with SARS-CoV-2. Those with myocarditis, regardless of whether they have symptoms, are benched, in part out of fear that myocarditis could lead to sudden death during intense activity. Martinez, who’s helping coordinate the research for the National Basketball Association and Major League Soccer, predicts a flow of data on athletes over the coming months. “Those of us in this space are willing to ruin a Saturday or a Sunday to get this done.”
                He stresses, though, that even if researchers can clarify the average duration of myocarditis and its risks for a young athlete, those may be very different for a 50-year-old with obesity or high blood pressure, especially if they were sick enough with COVID-19 to be hospitalized. “In those individuals, I am going to be more cautious” and screen for heart injury, he says.
                Others are pursuing clues to how COVID-19 can damage the heart, which might point to ways to head off the damage. “SARS-CoV-2 does challenge your immune system in unconventional ways,” Liu says. Autopsies of heart tissue after COVID-19 have revealed inflammation [in the heart’s blood vessels](https://jamanetwork.com/journals/jamacardiology/fullarticle/2768914) instead of its muscle cells, the site of the inflammation caused by other infections. Another autopsy study found [scattered death of heart cells](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.120.049465), but the authors noted the mechanism of injury was unknown. “There’s been a lot of discussion whether this is myocarditis” as typically defined, Liu says. Regardless, he and others hope for clinical trials to test whether preventive strategies, such as taking beta blocker drugs, might head off heart failure in someone flagged as high risk after COVID-19.
                While Mohiddin volunteers for a study of survivors, he’s also running one: a trial that [aims to recruit 140 people](https://clinicaltrials.gov/ct2/show/NCT04340921) while they are hospitalized with COVID-19 or soon after, 20 with severe myocarditis and the rest without. He and colleagues will look for abnormal T cell levels in the blood of people with myocarditis, which could help explain whether and how the immune system is causing cardiac injury. He is also exploring whether immune cell patterns in the blood presage myocarditis later.
                Even if COVID-19 rarely causes serious myocarditis, one hypothesis is that mild cases could heighten the risk of heart disease years later. Scar tissue can form as myocarditis heals, and earlier work has shown residual cardiac inflammation portends worse heart health. As cardiologists, “We’re in the business of identifying asymptomatic risk factors,” such as hypertension, Mohiddin says. “It’s not difficult to imagine that in the future, clinical practitioners will ask a new patient, ‘Did you have COVID?’”
            """
