#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_bytes - prints basic info about byes
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *Bytes = (PyBytesObject *) p;
	unsigned char  itr, size;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", Bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", size);
	for (itr = 0; itr < size; itr++)
	{
		printf("%02hhx", Bytes->ob_sval[itr]);
		if (itr == (size - 1))
			printf("\n");
		else
			printf(" ");
	}

}



/**
 * print_python_list_info - prints information about python lists
 * @p: PyObject list
 */

void print_python_list(PyObject *p)
{
	int total_size, allocation, itr;
	const char *type;
	PyListObject *List = (PyListObject *)p;
	PyVarObject *variable = (PyVarObject *)p;

	total_size = variable->ob_size;
	allocation = List->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", total_size);
	printf("[*] Allocated = %d\n", allocation);

	for (itr = 0; itr < total_size; itr++)
	{
		type = List->ob_item[itr]->ob_type->tp_name;
		printf("Element %d: %s\n", itr, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(List->ob_item[itr]);
	}
}
