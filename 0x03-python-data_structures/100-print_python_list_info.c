#include <python.h>

/**
 * print_python_list_info - prints information about python lists
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int totall_count, allocation, itr;
	PyObject *object;

	totall_count = Py_SIZE(p);
	allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", totall_count);
	printf("[*] Allocated = %d\n", allocation);

	for (itr = 0; itr < totall_count; itr++)
	{
		printf("Element %d: ", itr);
		object = PyList_GetItem(p, itr);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
