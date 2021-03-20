from collections import Counter
class MajorityElement:
	def getMajorityElement(self, array):
		elements = Counter(array)
		size = len(array)
		return (", ".join(str(x) for x in [k for k,v in elements.items() if v>size/2]))