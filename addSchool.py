import json, re

name = input('School Name: ')

engScore = input('English Score: ')
mathScore = input('Math Score: ')

gradRate = input('Grad Rate: ')
ucReqs = input('UC/CSU Req %: ')
avgSAT = input('AVG SAT: ')

lowIncomeRate = input('Low Income %: ')
teacherRatio = input('Teacher/Student Ratio: ')

print('Race Data: ')
items = []
while True:
	line = input()
	if line:
		items.append(line)
	else:
		break

raceData = []
for line in items:
	counter = 0
	for char in line:
		if char.isdigit():
			break
		counter += 1
	raceData.append((line[0:counter], line[counter:len(line)]))
		
data = {
        'Name': name,
        'Scores': {
            'English': engScore,
            'Math': mathScore,
            'SAT': avgSAT
        	},
        'Grad %': gradRate,
        'UC/CSU Reqs': ucReqs,
		'Race Data': raceData,
		'Low Income %': lowIncomeRate,
		'Teacher/Student Ratio: ': teacherRatio
	}

#jsonData = json.dumps(data, indent=4, sort_keys=True)
#print(jsonData)


with open(name.replace(" ", "") + '.json', 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

print(data)