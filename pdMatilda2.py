"""
For all strategies,
 return True for cooperate, 
 return False for defect

"""
import random 

class PDStrat:
	def getName(self):
		return "Matilda"

	def getMove(self, mvHist, oppMvHist):
		alwayscoop = False 
		#goals: try to find a tit for tat strategy and counter it somehow..
		#maybe just take us both down??? 
		#goal 2: find when its always cooperate by attempting defects within the first 30 and then switching to
		#always defecting 
		#want to cooperate with punishment: 
		if mvHist == []: #start with cooperation
			return True
		if alwayscoop == True:
			return False 
		if len(mvHist) == 20:
			return False
		if len(mvHist) == 21:
			return False
		if len(mvHist) == 22:
			return False
		if len(mvHist) == 23:
			return False
		if len(mvHist) == 24 and oppMvHist == [24*[True]]:
			alwayscoop = True

		#tit for tat but with a tiny bit of remorse for kicks 
		if oppMvHist[-1]==True:
			return True
		elif oppMvHist[-1] == False and random.random() > .05: #random forgivness 
		#to not get stuck in loop of defects, very few times though 
			return False
		else: 
			return True 


			
	
		



