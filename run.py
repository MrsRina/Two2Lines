class Run_Aplication:
	def __init__(self, lib):
		try:
			self.execute(lib)
		except:
			raise
		return None

	def execute(self, lib):
		try:
			lib.system("javac -classpath {} Data/application.java".format((
				"Libs/lwjgl.jar;" +
				"Libs/lwjgl-glfw.jar;" +
				"Libs/lwjgl-javadoc.jar;" +
				"Libs/lwjgl-glfw-natives-windows.jar.jar;" +
				"Libs/lwjgl-glfw-sources.jar"
				)))
		except:
			raise
		return None

if __name__ == "__main__":
	import os

	Run_Aplication(os)
