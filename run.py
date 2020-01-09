class Run_Aplication:
	def __init__(self, lib):
		try:
			self.execute(lib)
		except:
			raise
		return None

	def execute(self, lib):
		try:
			self.bat             = open("debug.bat", "w")
			self.debug_arguments = ("{}".format((
				"Libs/lwjgl.jar;"                          +
				"Libs/lwjgl-glfw.jar;"                     +
				"Libs/lwjgl-javadoc.jar;"                  +
				"Libs/lwjgl-glfw-natives-windows.jar.jar;" +
				"Libs/lwjgl-glfw-sources.jar;"             +
				"Libs/lwjgl-opengl.jar;"                   +
				"Libs/lwjgl-opengl-natives-windows.jar;"   +
				"Libs/lwjgl-opengles-javadoc.jar;"         +
				"Libs/lwjgl-opengles.jar;"                 +
				"Libs/lwjgl-opengles-sources.jar;"         +
				"Libs/lwjgl-opengles-natives-windows.jar" 
				)))

			lib.system("javac -cp " + self.debug_arguments + " Data\\Application.java")
			lib.system("cd data & java Application")

			self.process_file_debug(self.bat)
		except:
			raise
		return None

	def process_file_debug(self, file):
		try:
			file.write("pause\n")
			file.write("javac -cp " + self.debug_arguments + " Data\\Application.java")
			file.write("cd data & java Application")
			file.write("\npause")
			file.close()
		except:
			raise
		return None

if __name__ == "__main__":
	import os

	Run_Aplication(os)