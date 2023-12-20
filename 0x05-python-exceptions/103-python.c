#define PY_SSIZE_T_CLEAN
#include "Python.h"


/**
 * print_python_bytes - prints info about Python strings.
 * @p: pointer to head of list
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *list = (PyBytesObject *) p;
	long int itr, size = list->ob_base.ob_size;

	setbuf(stdout, NULL);
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
 * print_python_float - prints python float info.
 * @p: head pointer
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *list = (PyFloatObject *) p;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %s\n", PyOS_double_to_string(list->ob_fval, 'r'
				, 0, Py_DTSF_ADD_DOT_0, NULL));
}


/**
 * print_python_list - prints info about Python lists.
 * @p: pointer to head of list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	long int itr, count = list->ob_base.ob_size;
	const char *type;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", count);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (itr = 0; itr < count; itr++)
	{
		type = list->ob_item[itr]->ob_type->tp_name;
		printf("Element %ld: %s\n", itr, type);
		if (PyBytes_Check((PyObject *) list->ob_item[itr]))
			print_python_bytes((PyObject *) list->ob_item[itr]);
		else if (PyFloat_Check((PyObject *) list->ob_item[itr]))
			print_python_float((PyObject *) list->ob_item[itr]);
	}
}
