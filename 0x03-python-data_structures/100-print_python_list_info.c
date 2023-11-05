#include <python.h>

/**
 *print_python_list_info - Prints basic info about Python lists
 *
 *@p: Python object pointer list
 *
 *Return: Void
 */

void print_python_list_info(PyObject *p)
{
	int pysize, allocate, x;
	PyObject *pyobj;

	pysize = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", pysize);
	printf("[*] Allocated = %d\n", allocate);

	for (x = 0; x < pysize; x++)
	{
		printf("Element %d: ", x);

		pyobj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(pyobj)->tp_name);
	}
}
