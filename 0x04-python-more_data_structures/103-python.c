#include <Python.h>
void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(item)->tp_name;
        printf("Element %ld: %s\n", i, type_name);
    }
}
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;
    PyObject *repr;
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    repr = PyObject_Repr(p);
    str = PyUnicode_AsUTF8(repr);
    printf("  trying string: %s\n", str);
    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
        if (i < 9 && i < size - 1)
            printf(" ");
    }
    printf("\n");

    Py_XDECREF(repr);
}
