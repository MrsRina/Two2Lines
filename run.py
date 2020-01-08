class Run_Aplication:
	def __init__(self, lib):
		try:
			self.execute(lib)
		except:
			raise
		return None

	def execute(self, lib):
		try:
			lib.system("javac -classpath {lwjgl} Data/application.java".format(
			lwjgl = "Libs/lwjgl.jar"
			)
			)
		except:
			raise
		return None

if __name__ == "__main__":
	import os

	Run_Aplication(os)
