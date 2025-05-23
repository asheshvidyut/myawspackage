#include <Python.h>

static PyObject* my_c_module_add(PyObject* self, PyObject* args) {
    long a, b;
    if (!PyArg_ParseTuple(args, "ll", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);
}

static PyMethodDef MyCModuleMethods[] = {
    {"add", my_c_module_add, METH_VARARGS, "Adds two numbers."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef my_c_module = {
    PyModuleDef_HEAD_INIT,
    "my_package.my_c_module", // name of module
    "A simple C module.",     // module documentation, may be NULL
    -1,                       // size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
    MyCModuleMethods
};

PyMODINIT_FUNC PyInit_my_c_module(void) {
    return PyModule_Create(&my_c_module);
}