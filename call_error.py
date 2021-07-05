class CallError(Exception):
	def __init__(self, field, message):
		self._field = field
		self._message = message
	def __str__(self):
	    return 'You have entered an {}. {}'.format(self._field,self._message)
