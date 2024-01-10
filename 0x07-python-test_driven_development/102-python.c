#include <Python.h>
#include <object.h>
#include <unicodeobject.h>



/**
 * print_python_string - prints information about python string object
 * @p: pointer to PyObject
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (PyUnicode_Check(p) == 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
	printf("  length: %lu\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}
