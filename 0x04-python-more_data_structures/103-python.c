#include <Python.h>

/**
 *print_python_list - Prints basic info about Python lists
 *
 *@p: PyObject list object
 *
 *Return: Void
 */

void print_python_list(PyObject *p)
{
	int size, allocate, j;
	const char *list_type;
	PyListObject *pylist = (PyListObject *)p;
	PyVarObject *variable = (PyVarObject *)p;

	size = variable->ob_size;
	allocate = pylist->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (j = 0; j < size; j++)
	{
		list_type = pylist->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, list_type);
		if (strcmp(list_type, "bytes") == 0)
			print_python_bytes(pylist->ob_item[j]);
	}
}

/**
 *print_python_bytes - Prints basic info about Python byte objects
 *
 *@p: PyObject byte object
 *
 *Return: Void
 */

void print_python_bytes(PyObject *p)
{
	unsigned char j, size;
	PyBytesObject *pybytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", pybytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (j = 0; j < size; j++)
	{
		printf("%02hhx", pybytes->ob_sval[j]);
		if (j == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
