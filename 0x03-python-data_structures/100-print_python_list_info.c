#include <Python.h>
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;
    PyObject *element;
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}
