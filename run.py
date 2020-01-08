class Run_Aplication:
	def __init__(self, lib):
		try:
			self.execute(lib)
		except:
			raise
		return None

	def execute(self, lib):
		try:
			self.bat             = open("exec_debug.bat", "w")
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
			lib.system("java -cp " + self.debug_arguments + " Application")

			self.bat.write("pause\n")
			self.bat.write("javac -classpath " + self.debug_arguments + " Data/application.java")
			self.bat.write("\ncd data/")
			self.bat.write("\njava -classpath " + self.debug_arguments + " Application")
			self.bat.write("\npause")
			self.bat.close()
		except:
			raise
		return None

if __name__ == "__main__":
	import os

	Run_Aplication(os)