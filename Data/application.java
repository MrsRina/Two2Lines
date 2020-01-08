// Imports all contents.

import org.lwjgl.system.*;
import org.lwjgl.glfw.*;
import org.lwjgl.*;

import java.nio.*;


class application 
{
	private long twoWindow;

	public void main(String[] args) 
	{
		int twoWidth  = 1280;
		int twoHeight = 800;

		String twoTitle = "Two2Lines";

		new application().twoGameProcess();
	}

	public void twoGameProcess()
	{
		glfwInit();

		glfwDefaultWindowHints();
		glfwWindowHint(GLFW_VISIBLE, GLWF_FALSE);
		glfwWindowHint(GLFW_RESIZABLE, GLWF_TRUE);

		twoWindow = glfwCreateWindow(twoWidth, twoHeight, twoTitle, NULL, NULL);

		new application().twoSycnFinshApplication();
	}

	public void twoSycnFinshApplication()
	{
		glfwSetKeyCallBck(twoWindow, (twoWindow, key, scancode, action, mods) -> 
		{
			if (key == GLFW_KEY_ESCAPE && action == GLFW_REALSE)
				glfwSetWindowShouldClose(twoWindow, true);
		});
	}
}