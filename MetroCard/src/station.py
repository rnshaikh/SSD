from heapq import heappush, heappop


class Station:

	def __init__(self, name):
		self.__name = name
		self.__total_amount_collected = 0
		self.__discount = 0
		self.people_count = {}
		
	def check_in(self, amount, discount, person_type):
		self.__total_amount_collected += amount
		self.__discount += discount
		self.people_count[person_type] = self.people_count.get(person_type, 0) + 1

	def order_people(self):
		heap = []
		for i in self.people_count:
			heappush(heap, (-self.people_count[i], i))
		return heap

	def print_summary(self):

		print("TOTAL_COLLECTION {name} {amount} {discount}".format(name=self.__name, 
																   amount=self.__total_amount_collected,
																   discount=self.__discount))
		print("PASSENGER_TYPE_SUMMARY")
		heap = self.order_people()
		while heap:
			people = heappop(heap)
			print(people[1], -people[0])





