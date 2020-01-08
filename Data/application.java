// Imports all contents.

import org.lwjgl.system.*;
import org.lwjgl.opengl.*;
import org.lwjgl.glfw.*;
import org.lwjgl.*;

import java.nio.*;

import static org.lwjgl.glfw.Callbacks.*;
import static org.lwjgl.glfw.GLFW.*;

import static org.lwjgl.opengl.GL11.*;

class Application 
{
	private long twoWindow;

	public int twoWidth  = 1280;
	public int twoHeight = 800;

	public String twoTitle = "Two2Lines";

	public static void main(String[] args) 
	{
		new Application().twoGameInit();
	}

	public void twoGameInit()
	{
		new Application().twoGameProcess();
		new Application().twoGameLoop();

		glfwFreeCallbacks(twoWindow);
		glfwDestroyWindow(twoWindow);

		glfwTerminate();
		glfwSetErrorCallback(null).free();
	}

	public void twoGameProcess()
	{
		glfwInit();

		glfwDefaultWindowHints();
		glfwWindowHint(GLFW_VISIBLE, GLFW_FALSE);
		glfwWindowHint(GLFW_RESIZABLE, GLFW_TRUE);

		twoWindow = glfwCreateWindow(twoWidth, twoHeight, twoTitle, 0, 0);

		new Application().twoSycnFinshApplication();

		glfwMakeContextCurrent(twoWindow);
		glfwShowWindow(twoWindow);
		glfwSwapInterval(1);
	}

	public void twoGameLoop()
	{
		glClearColor(0.5f, 0.5f, 0.5f, 0.0f);

		while (!glfwWindowShouldClose(twoWindow))
		{
			glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
			glfwSwapBuffers(twoWindow);
			glfwPollEvents();
		}
	}

	public void twoSycnFinshApplication()
	{
		glfwSetKeyCallback(twoWindow, (twoWindow, key, scancode, action, mods) -> 
		{
			if (key == GLFW_KEY_ESCAPE && action == GLFW_RELEASE)
				glfwSetWindowShouldClose(twoWindow, true);
		});
	}
}