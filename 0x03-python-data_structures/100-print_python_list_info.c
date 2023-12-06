#include <python.h>

/**
 * print_python_list_info - prints information about python lists
 * @p: PyObject list
 */

void print_python_list_info(Pyobject *p)
{
	int totall_count, allocation, itr;
	PyObject *object;

	totall_count = Py_SIZE(p);
	allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", totall_count);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", itr);
		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
