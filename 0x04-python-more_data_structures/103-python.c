#include <Python.h>


/**
 * print_python_bytes - prints basic info about byes
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *list = (PyBytesObject *) p;
	long int itr, size = list->ob_base.ob_size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", list->ob_sval);
	size = size < 10 ? size + 1 : 10;
	printf("  first %ld bytes:", size);
	for (itr = 0; itr < size; itr++)
	{
		printf(" %2.2x", list->ob_sval[itr] & 0xff);
	}
	putchar('\n');
}



/**
 * print_python_list_info - prints information about python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int total_count, allocation, itr;
	const char *type;
	PyListObject *List = (PyListObject *)p;
	PyVarObject *variable = (PyVarObject *)p;

	total_count = variable->ob_size;
	allocation = List->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", total_count);
	printf("[*] Allocated = %d\n", allocation);

	for (itr = 0; itr < total_count; itr++)
	{
		type = List->ob_item[itr]->ob_type->tp_name;
		printf("Element %d: %s\n", itr, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(List->ob_item[itr]);
	}
}
