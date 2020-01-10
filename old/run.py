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
				"Libs/lwjgl.jar" +
				#"Libs/lwjgl-assimp.jar" +
				#"Libs/lwjgl-assimp-javadoc.jar" +
				#"Libs/lwjgl-assimp-natives-windows.jar" +
				#"Libs/lwjgl-assimp-sources.jar" + ";" +
				#"Libs/lwjgl-bgfx.jar" + ";" +
				#"Libs/lwjgl-bgfx-javadoc.jar" + ";" +
				#"Libs/lwjgl-bgfx-natives-windows.jar" + ";" +
				#"Libs/lwjgl-bgfx-sources.jar" + ";" +
				#"Libs/lwjgl-cuda.jar" + ";" +
				#"Libs/lwjgl-cuda-javadoc.jar" + ";" +
				#"Libs/lwjgl-cuda-sources.jar" + ";" +
				#"Libs/lwjgl-egl.jar" + ";" +
				#"Libs/lwjgl-egl-javadoc.jar" + ";" +
				#"Libs/lwjgl-egl-sources.jar" + ";" +
				"Libs/lwjgl-glfw.jar" + ";" +
				"Libs/lwjgl-glfw-javadoc.jar" + ";" +
				"Libs/lwjgl-glfw-natives-windows.jar" + ";" +
				"Libs/lwjgl-glfw-sources.jar" + ";" +
				#"Libs/lwjgl-javadoc.jar" + ";" +
				#"Libs/lwjgl-jawt.jar" + ";" +
				#"Libs/lwjgl-jawt-javadoc.jar" + ";" +
				#"Libs/lwjgl-jawt-sources.jar" + ";" +
				#"Libs/lwjgl-jemalloc.jar" + ";" +
				#"Libs/lwjgl-jemalloc-javadoc.jar" + ";" +
				#"Libs/lwjgl-jemalloc-natives-windows.jar" + ";" +
				#"Libs/lwjgl-jemalloc-sources.jar" + ";" +
				#"Libs/lwjgl-libdivide.jar" + ";" +
				#"Libs/lwjgl-libdivide-javadoc.jar" + ";" +
				#"Libs/lwjgl-libdivide-natives-windows.jar" + ";" +
				#"Libs/lwjgl-libdivide-sources.jar" + ";" +
				#"Libs/lwjgl-llvm.jar" + ";" +
				#"Libs/lwjgl-llvm-javadoc.jar" + ";" +
				#"Libs/lwjgl-llvm-natives-windows.jar" + ";" +
				#"Libs/lwjgl-llvm-sources.jar" + ";" +
				#"Libs/lwjgl-lmdb.jar" + ";" +
				#"Libs/lwjgl-lmdb-javadoc.jar" + ";" +
				#"Libs/lwjgl-lmdb-natives-windows.jar" + ";" +
				#"Libs/lwjgl-lmdb-sources.jar" + ";" +
				#"Libs/lwjgl-lz4.jar" + ";" +
				#"Libs/lwjgl-lz4-javadoc.jar" + ";" +
				#"Libs/lwjgl-lz4-natives-windows.jar" + ";" +
				#"Libs/lwjgl-lz4-sources.jar" + ";" +
				#"Libs/lwjgl-meow.jar" + ";" +
				#"Libs/lwjgl-meow-javadoc.jar" + ";" +
				#"Libs/lwjgl-meow-natives-windows.jar" + ";" +
				#"Libs/lwjgl-meow-sources.jar" + ";" +
				#"Libs/lwjgl-nanovg.jar" + ";" +
				#"Libs/lwjgl-nanovg-javadoc.jar" + ";" +
				#"Libs/lwjgl-nanovg-natives-windows.jar" + ";" +
				#"Libs/lwjgl-nanovg-sources.jar" + ";" +
				#"Libs/lwjgl-natives-windows.jar" + ";" +
				#"Libs/lwjgl-nfd.jar" + ";" +
				#"Libs/lwjgl-nfd-javadoc.jar" + ";" +
				#"Libs/lwjgl-nfd-natives-windows.jar" + ";" +
				#"Libs/lwjgl-nfd-sources.jar" + ";" +
				#"Libs/lwjgl-nuklear.jar" + ";" +
				#"Libs/lwjgl-nuklear-javadoc.jar" + ";" +
				#"Libs/lwjgl-nuklear-natives-windows.jar" + ";" +
				#"Libs/lwjgl-nuklear-sources.jar" + ";" +
				#"Libs/lwjgl-odbc.jar" + ";" +
				#"Libs/lwjgl-odbc-javadoc.jar" + ";" +
				#"Libs/lwjgl-odbc-sources.jar" + ";" +
				#"Libs/lwjgl-openal.jar" + ";" +
				#"Libs/lwjgl-openal-javadoc.jar" + ";" +
				#"Libs/lwjgl-openal-natives-windows.jar" + ";" +
				#"Libs/lwjgl-openal-sources.jar" + ";" +
				#"Libs/lwjgl-opencl.jar" + ";" +
				#"Libs/lwjgl-opencl-javadoc.jar" + ";" +
				#"Libs/lwjgl-opencl-sources.jar" + ";" +
				#"Libs/lwjgl-opengl.jar" + ";" +
				"Libs/lwjgl-opengles.jar" + ";" +
				"Libs/lwjgl-opengles-javadoc.jar" + ";" +
				"Libs/lwjgl-opengles-natives-windows.jar" + ";" +
				"Libs/lwjgl-opengles-sources.jar" + ";" +
				"Libs/lwjgl-opengl-javadoc.jar" + ";" +
				"Libs/lwjgl-opengl-natives-windows.jar" + ";" +
				"Libs/lwjgl-opengl-sources.jar" + ";" 
				#"Libs/lwjgl-openvr.jar" + ";" +
				#"Libs/lwjgl-openvr-javadoc.jar" + ";" +
				#"Libs/lwjgl-openvr-natives-windows.jar" + ";" +
				#"Libs/lwjgl-openvr-sources.jar" + ";" +
				#"Libs/lwjgl-opus.jar" + ";" +
				#"Libs/lwjgl-opus-javadoc.jar" + ";" +
				#"Libs/lwjgl-opus-natives-windows.jar" + ";" +
				#"Libs/lwjgl-opus-sources.jar" + ";" +
				#"Libs/lwjgl-ovr.jar" + ";" +
				#"Libs/lwjgl-ovr-javadoc.jar" + ";" +
				#"Libs/lwjgl-ovr-natives-windows.jar" + ";" +
				#"Libs/lwjgl-ovr-sources.jar" + ";" +
				#"Libs/lwjgl-par.jar" + ";" +
				#"Libs/lwjgl-par-javadoc.jar" + ";" +
				#"Libs/lwjgl-par-natives-windows.jar" + ";" +
				#"Libs/lwjgl-par-sources.jar" + ";" +
				#"Libs/lwjgl-remotery.jar" + ";" +
				#"Libs/lwjgl-remotery-javadoc.jar" + ";" +
				#"Libs/lwjgl-remotery-natives-windows.jar" + ";" +
				#"Libs/lwjgl-remotery-sources.jar" + ";" +
				#"Libs/lwjgl-rpmalloc.jar" + ";" +
				#"Libs/lwjgl-rpmalloc-javadoc.jar" + ";" +
				#"Libs/lwjgl-rpmalloc-natives-windows.jar" + ";" +
				#"Libs/lwjgl-rpmalloc-sources.jar" + ";" +
				#"Libs/lwjgl-shaderc.jar" + ";" +
				#"Libs/lwjgl-shaderc-javadoc.jar" + ";" +
				#"Libs/lwjgl-shaderc-natives-windows.jar" + ";" +
				#"Libs/lwjgl-shaderc-sources.jar" + ";" +
				#"Libs/lwjgl-sources.jar" + ";" +
				#"Libs/lwjgl-sse.jar" + ";" +
				#"Libs/lwjgl-sse-javadoc.jar" + ";" +
				#"Libs/lwjgl-sse-natives-windows.jar" + ";" +
				#"Libs/lwjgl-sse-sources.jar" + ";" +
				#"Libs/lwjgl-stb.jar" + ";" +
				#"Libs/lwjgl-stb-javadoc.jar" + ";" +
				#"Libs/lwjgl-stb-natives-windows.jar" + ";" +
				#"Libs/lwjgl-stb-sources.jar" + ";" +
				#"Libs/lwjgl-tinyexr.jar" + ";" +
				#"Libs/lwjgl-tinyexr-javadoc.jar" + ";" +
				#"Libs/lwjgl-tinyexr-natives-windows.jar" + ";" +
				#"Libs/lwjgl-tinyexr-sources.jar" + ";" +
				#"Libs/lwjgl-tinyfd.jar" + ";" +
				#"Libs/lwjgl-tinyfd-javadoc.jar" + ";" +
				#"Libs/lwjgl-tinyfd-natives-windows.jar" + ";" +
				#"Libs/lwjgl-tinyfd-sources.jar" + ";" +
				#"Libs/lwjgl-tootle.jar" + ";" +
				#"Libs/lwjgl-tootle-javadoc.jar" + ";" +
				#"Libs/lwjgl-tootle-natives-windows.jar" + ";" +
				#"Libs/lwjgl-tootle-sources.jar" + ";" +
				#"Libs/lwjgl-vma.jar" + ";" +
				#"Libs/lwjgl-vma-javadoc.jar" + ";" +
				#"Libs/lwjgl-vma-natives-windows.jar" + ";" +
				#"Libs/lwjgl-vma-sources.jar" + ";" +
				#"Libs/lwjgl-vulkan.jar" + ";" +
				#"Libs/lwjgl-vulkan-javadoc.jar" + ";" +
				#"Libs/lwjgl-vulkan-sources.jar" + ";" +
				#"Libs/lwjgl-xxhash.jar" + ";" +
				#"Libs/lwjgl-xxhash-javadoc.jar" + ";" +
				#"Libs/lwjgl-xxhash-natives-windows.jar" + ";" +
				#"Libs/lwjgl-xxhash-sources.jar" + ";" +
				#"Libs/lwjgl-yoga.jar" + ";" +
				#"Libs/lwjgl-yoga-javadoc.jar" + ";" +
				#"Libs/lwjgl-yoga-natives-windows.jar" + ";" +
				#"Libs/lwjgl-yoga-sources.jar" + ";" +
				#"Libs/lwjgl-zstd.jar" + ";" +
				#"Libs/lwjgl-zstd-javadoc.jar" + ";" +
				#"Libs/lwjgl-zstd-natives-windows.jar" + ";" +
				#"Libs/lwjgl-zstd-sources.jar" + ";"
				)))

			lib.system('javac -cp ' + self.debug_arguments + ' Data\\Application.java ')
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