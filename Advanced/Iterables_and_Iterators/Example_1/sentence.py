class Sentence:

	def __init__(self, sentence):

		self.words_in_sentence = sentence.split()

		self.sentence_length = len(self.words_in_sentence)

		self.current_index = 0


	def __iter__(self):

		return self


	def __next__(self):

		if self.current_index < self.sentence_length:

			word = self.words_in_sentence[self.current_index]

			self.current_index += 1

			return word

		else:

			raise StopIteration