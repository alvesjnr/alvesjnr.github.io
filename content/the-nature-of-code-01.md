Title: Simulating Natural Systems - Part 1
Date: 2014-01-06 14:00
Tags: simulation, programming, Cython, NatureOfCode
Category: Simulation
Slug: simulating-natural-process-01
Author: Antonio Ribeiro
Summary: Updating informations about th e project: implementing basic vector arithmetic


This post is part of a series. Please check all the previous posts before continuing: [The Nature of Code series](tag/natureofcode.html)

I implemented the first half of the codes discussed in the first chapter of [The Nature of Code](http://natureofcode.com). Mostly of the time was spent learning Cython, instead of actually programing, so I think that the second half of the code wouldn't take more than an hour to be implemented.

The code is available at my [Github repository](https://github.com/alvesjnr/nature-of-code) for this project. The main three files so far are:

```
nvector_vector.h - C header file
nvector_vector.c - Logical implementation of all operations
vector.pyx - Binding to Python
```

All the logic is implemented in the *nvector_vector.c* file. As the logic on basic vetors operation (dot and cross multiplication, addition, subtraction, mudule, etc.) are pretty straightforward, I'll not discuss this implementation at this point. The file *vector.pyx* is a Cython code that binds the C implementation to Python, providing a Python module after compiled (vector.so). Lets focus on this file.

My goal when creating a python binding is not just translating the C functions to be called by a Python code. Actually what I have in mind is to write a Python version of the same code, as much *pythonic* as possible.

A C code has an explicitly distinction between the data and the logic. As you can see in *nvector_vector.c*, our data is represented by a *struct* and all the relevant operations are effectuated by functions that receives our data vector (struct) as a parameter. That's how we code in C, but that's not how we do it in Python.

When coding in Python, an object oriented approach is more convenient. Our vector would be no longer only a data container, but a full object which contains both our data and the operations over this data (our methods). This way, operations as addition, multiplications, etc. would no longer be executed by external function (as in C) but by the vector object itself.

That said, lets start coding our Python equivalent of *nvector_vector.c*. To do this we will use a third language (neither C nor Python): [Cython](http://www.cython.org/). Cython is a superset of Python, which means that, at least in theory, all Python code is valid as a Cython code. Also Cython provides us a lot of extra resources. In special for us at this project is the possibility of talk to C libraries.

So, the very first thing we do in Cython on this project is to *import* our C functions. At the very beginning of the code (*vector.pyx*) we have:

    cdef extern from "nvector.h":

It starts a bloc of code where are declared all the extern functions/data structures that we are importing from our C library:

    cdef extern from "nvector.h":

        ctypedef struct nvector:
            double x
            double y

        nvector* nvector_new(double x, double y)
        nvector* nvector_copy(nvector *v)
        void nvector_del(nvector *v)
        void nvector_add(nvector *left, nvector *right)
        void nvector_sub(nvector *left,  nvector *right)
        void nvector_mul(nvector *left, double right)
        double nvector_dot( nvector *left,  nvector *right)
        double nvector_mag( nvector *v)
        nvector* nvector_normalize( nvector *v)
        void nvector_setmag(nvector *v, double mag)
        double nvector_angle_between( nvector *v1,  nvector *v2)
        double nvector_angle( nvector *v)

This bloc of code tells to Cython which functions and data structures we are interfacing with. Extra attention to the struct: we statically defined the type of each variables in the struct.

Our next step is to define our Python equivalent of the vector. The approach will be to create a class Vector which implements all the methods related to our vector:

    cdef class Vector:
        
        cdef nvector* _vector
        cdef nvector* _aux_vector

        def __cinit__(self, double x=0.0, double y=0.0):
            self._vector = nvector_new(x,y)

One main thing can be notated from this piece of code: the class statically define the variable _vector as 'cdef nvector* vector'. The reason to do this is that nvector is not an ordinary python object, but a Cython type, and it should be explicitly declared as so.

Tricky part: Convincing the compiler that Vector is indeed a Vector
------------------------------------------------

Here a tricky part: when implementing the *\_\_add\_\_* function I got an error because the Cython compiler was not finding my _vector variable. The original code was more or less like this:


    cdef class Vector:
        
        cdef nvector* _vector
        cdef nvector* _aux_vector

        def __cinit__(self, double x=0.0, double y=0.0):
            self._vector = nvector_new(x,y)
        
        def __add__(left, right):
            left._aux_vector = nvector_copy(left._vector)
            nvector_add( left._aux_vector, right._vector)

            return Vector(left._aux_vector.x, left._aux_vector.y)

The code compiled, but when trying to use it I got:

    AttributeError: 'vector.Vector' object has no attribute '_vector'

The reason is: as *_vector* is declared as *cdef*, it does not works as an ordinary python object. In fact, to access it we have to explicitly indicate to Cython compiler that my Vector object is indeed of type Vector. We can do it in two different ways: casting our *left* and *right* variables to Vector:
    
    def __add__(left, right):
        (<Vector>left)._aux_vector =  nvector_copy((<Vector>left)._vector)
        nvector_add( (<Vector>left)._aux_vector, (<Vector>right)._vector)

        return Vector((<Vector>left)._aux_vector.x, (<Vector>left)._aux_vector.y)

or adding the type of the variables in our \_\_add\_\_ method signature:

    def __add__(Vector left, Vector right):
        left._aux_vector =  nvector_copy(left._vector)
        nvector_add(  left._aux_vector, right._vector)

        return Vector(left._aux_vector.x, left._aux_vector.y)

Although the second way is cleaner, it doesn't fits in situations when the same method might receive different operands type. For example, for the *\_\_mul\_\_* method, we overload the operator * to operates both cross product (not yet implemented) and do the multiplication from a vector to an integer/float. In those situations, the variables passed to the method *\_\_mul\_\_* might by either a double, an int or a Vector object. Our solution for this case is not to specify the type in the method signature, but to sxplicitly cast it in our code:

    def __mul__(left, right):

        if isinstance(left, (int, float)) ^ isinstance(right, (int, float)):
            #lets put int/float at right side
            if isinstance(left, (int,float)):
                right, left = left, right
            return (<Vector>left).mul(right) #explicitly casting
        
        elif isinstance(right, Vector) and isinstance(left, Vector):
            return (<Vector>left).cross(right) #explicitly casting

        else:
            return NotImplemented


That's all so far. The full code can be visualized in the [Github repository](https://github.com/alvesjnr/nature-of-code). The current version of *vector.pyx* can be found at [here](https://github.com/alvesjnr/nature-of-code/blob/7d6ef32caa5519878ddac1a90470953439e3e409/src/vector.pyx) **Warning: This is a permalink. All possible fixes will not be applied to the code at in link**. I'll continue to implement this first chapter and a next post will be done as far as I get my hands on the second chapter.

I appreciate your curiosity :)
