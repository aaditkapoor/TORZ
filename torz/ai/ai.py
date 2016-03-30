from torz.models import BrainSystem, TrendingStuff, TorzBrain

class AISystem:
	common = {

		"hi":"Hi! I am Torz",
		"how are you?":"I am fine",
		"hello":"HI!",
		"who are you?":"I am TORZ!",
	}
	query = ""

	def __init__(self,query):
		self.query = query.lower()



	def check(self):
		if self.common.get(self.query,False):
			return True
		else:
			return False

	def get_response(self):
		return self.common.get(self.query)


