import matplotlib.pyplot as plt
import numpy as np
import json

schools = ['PaloAltoHighSchool', 'MontaVistaHighSchool', 'Menlo-AthertonHighSchool', 'WoodsideHighSchool', 'ApolloHighSchool', 'NationalAverages']
colors = ['#4286f4', '#4286f4', '#4286f4', '#4286f4', '#4286f4', '#fcb65a']
data = []

for name in schools:
	with open(name + '.json') as f:
		data.append(json.loads(f.read()))

def getNames():
	names = []
	for school in data:
		names.append(school['Name'][0:len(school['Name'])-12])

	return names

def getScores(key):
	scores = []
	for school in data:
		scores.append(int(school['Scores'][key]))
	return scores

def getData(key):
	dataPoints = []
	for school in data:
		dataPoints.append(int(school[key]))
	return dataPoints

def getRaceData(threshold):
	raceData = []
	for school in data:
		schoolData = []
		for race in school['Race Data']:
			if int(race[1][0:-1]) >= threshold:
				schoolData.append(race)
		raceData.append(len(schoolData))
	return raceData

def compareScoreGraph(crit0, crit1):
	crit0Data = getData(crit0)
	crit1Data = getScores(crit1)

	plt.plot(np.unique(crit0Data), np.poly1d(np.polyfit(crit0Data, crit1Data, 1))(np.unique(crit0Data)))

	plt.title(crit0 + " vs. " + crit1 + " Scores")
	plt.xlabel(crit0)
	plt.ylabel(crit1)
	plt.scatter(crit0Data, crit1Data, None, colors)
	if crit1 == 'SAT':
		if crit0 == 'Teacher/Student Ratio: ':
			plt.axis([10, 25, 0, 2400])
		else:
			plt.axis([0, 100, 0, 2400])
	elif crit0 == 'Teacher/Student Ratio: ':
		plt.axis([10, 25, 0, 100])
	else:
		plt.axis([0, 100, 0, 100])
	fileName = crit0 + "vs" + crit1 + "Scores.png"
	fileName = fileName.replace("%", "")
	ileName = fileName.replace("%", "")
	fileName = fileName.replace("/", "")
	fileName = fileName.replace(" ", "")
	fileName = fileName.replace(':', "")
	plt.savefig(fileName)
	plt.show()

def compareScoresGraph(crit0, crit1):
	crit0Data = getScores(crit0)
	crit1Data = getScores(crit1)

	plt.plot(np.unique(crit0Data), np.poly1d(np.polyfit(crit0Data, crit1Data, 1))(np.unique(crit0Data)))

	plt.title(crit0 + " Scores vs. " + crit1 + " Scores")
	plt.xlabel(crit0)
	plt.ylabel(crit1)
	plt.scatter(crit0Data, crit1Data, None, colors)
	if crit0 == 'SAT':
		plt.axis([0, 2400, 0, 100])
	else:
		plt.axis([0, 100, 0, 100])
	fileName = crit0 + "ScoresVs" + crit1 + "Scores.png"
	fileName = fileName.replace("%", "")
	plt.savefig(fileName)
	plt.show()

def compareGraph(crit0, crit1):
	crit0Data = getData(crit0)
	crit1Data = getData(crit1)

	plt.plot(np.unique(crit0Data), np.poly1d(np.polyfit(crit0Data, crit1Data, 1))(np.unique(crit0Data)))

	plt.title(crit0 + " vs. " + crit1)
	plt.xlabel(crit0)
	plt.ylabel(crit1)
	plt.scatter(crit0Data, crit1Data, None, colors)
	if crit0 == 'Teacher/Student Ratio: ':
		plt.axis([15, 25, 0, 100])
	else:
		plt.axis([0, 100, 0, 100])
	fileName = crit0 + "ScoresVs" + crit1 + ".png"
	fileName = fileName.replace("%", "")
	fileName = fileName.replace("/", "")
	fileName = fileName.replace(" ", "")
	fileName = fileName.replace(':', "")
	plt.savefig(fileName)
	plt.show()

def compareRaceGraph(threshold, crit1):
	crit0Data = getRaceData(threshold)
	crit1Data = getScores(crit1)

	plt.plot(np.unique(crit0Data), np.poly1d(np.polyfit(crit0Data, crit1Data, 1))(np.unique(crit0Data)))

	plt.title('# of Races with over ' + str(threshold) + "% vs. " + crit1 + ' Scores')
	plt.xlabel('# of Races with over ' + str(threshold) + '%')
	plt.ylabel(crit1)
	plt.scatter(crit0Data, crit1Data, None, colors)
	plt.axis([0, 5, 0, 100])
	if crit1 == 'SAT':
		plt.axis([0, 5, 0, 2400])
	fileName = 'RaceOver' + str(threshold) + "Vs" + crit1 + 'Scores'
	fileName = fileName.replace("%", "")
	fileName = fileName.replace("/", "")
	plt.savefig(fileName)
	plt.show()
'''
compareGraph('Teacher/Student Ratio: ', 'Grad %')
compareScoreGraph('Teacher/Student Ratio: ', 'SAT')
compareScoreGraph('Teacher/Student Ratio: ', 'English')
compareScoreGraph('Teacher/Student Ratio: ', 'Math')

compareScoreGraph('Low Income %', 'English')
compareScoreGraph('Low Income %', 'Math')
compareScoreGraph('Low Income %', 'SAT')

compareGraph('Low Income %', 'Grad %')
compareGraph('Teacher/Student Ratio: ', 'Grad %')

compareScoresGraph('SAT', 'English')
compareScoresGraph('SAT', 'Math')

compareRaceGraph(10, 'English')
compareRaceGraph(10, 'Math')
compareRaceGraph(10, 'SAT')
'''