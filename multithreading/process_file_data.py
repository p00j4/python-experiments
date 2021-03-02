import requests
import resource 
"""
Problem statement: Create a json response validator library for given 2 files

Details
- Given 2 files with millions of request URLs (the files can be humongous that memory error can happen)
- Compare the response of
File 1 : line 1 & File 2 : line 1,
File 1 : line 2 & File 2 : line 2,

Thought Process
1. Memory care: To prevent memory error, lazy load with generator 
(Question: doesn't existing below way of file reading does this by default?
         with open(file) as f:
          	for line in f:
          		print(line)
2. To speed up, run then in parallel
Questions: 
Since there is I/O operation and Network call both so will multithreading help or  
or something else because I need to somehow logically be able to control the distribution of tasks to different threads/processes 
(different threads to work on different lines in files and not pick the lines which are already picked by other threads)
And how do I save the state/cursor/offset per thread so other thread knows from where to pick?
read line -> make API call for that line -> process should happen in sequence to keep the logic working

"""

class APIManager():

	@staticmethod
	def get(url):
		response = None
		try:
			response = requests.get(url)
		except Exception as e:
			raise e
		return response.json()

class Comparator():

	def __init__(self, file1, file2):
		self.file1 = file1
		self.file2 = file2

	def compare_json(self, response1, response2):
		if len(response1) != len(response2):
			return False 
		return response1 == response2


	def get_file_generator(self, file_object):
		for line in file_object:
			yield line

	def get_response(self):
		"""  FILES CAN BE HUGE - GENERATOR/YEILD"
		DUps entries
		#read file 2 -> get json
	    #read file 2 -> get json
		"""
		""" READ 1 line at a time using 2 generators """
		with open(self.file1, "r") as f1, open(self.file2, "r") as f2:
			f1 = self.get_file_generator(f1)
			f2 = self.get_file_generator(f2)

			while True:
				try:
					f1_line = next(f1)
					f2_line = next(f2)

					try:
						if f1_line != f2_line:
							f1_resp = APIManager.get(f1_line)
							f2_resp = APIManager.get(f2_line)
							if self.compare_json(f1_resp, f2_resp):
								print("{} equals {}".format(f1_line, f2_line))
							else:
								print("{} not equals {}".format(f1_line, f2_line))
						else:
							print("{} equals {}".format(f1_line, f2_line))

					except Exception as e:
						print("Exception: ", e)
				except StopIteration as e:
					print("No more line to read on the file") #any of the file generators have exhaunsted
					return


		""" WORKING SOLUTION without thinking about memory"""
		# with open(self.file1) as f1, open(self.file2) as f2: # uneven lines are okay
		# 	for f1_line, f2_line in zip(f1, f2):     #WORKS EASILY but memory heavy as zip will double the list
		# 		try:
		# 			f1_resp = APIManager.get(f1_line)
		# 			f2_resp = APIManager.get(f2_line)
		# 			if self.compare_json(f1_resp, f2_resp):
		# 				print("{} equals {}".format(f1_line, f2_line))
		# 			else:
		# 				print("{} not equals {}".format(f1_line, f2_line))
		# 		except Exception as e:
		# 			print("DEBUG: ", e)


f1 = <GIVE_filepath1_INSERT BELOW LINES IN FILE> 
"""
https://reqres.in/api/users/3
https://reqres.in/api/users/1
https://reqres.in/api/users/2
https://reqres.in/api/users/9
https://reqres.in/api/users?page=7 
"""
f2 = <GIVE_filepath2 INSERT BELOW LINES IN FILE> 
"""
https://reqres.in/api/users/2
https://reqres.in/api/users/9
https://reqres.in/api/users/1

https://reqres.in/api/users?page=7 
"""

c = Comparator(f1, f2)
file_gen = c.get_response()
print("\n\nMemory {}".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
