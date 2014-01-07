Title: Simulating Natural Systems - Part 2
Date: 2014-01-07 14:00
Tags: simulation, programming, Cython, NatureOfCode
Category: Simulation
Slug: simulating-natural-process-02
Author: Antonio Ribeiro
Summary: Updating informations about the project: adding properties to x, y and z components


This post is part of a series. Please check all the previous posts before continuing: [The Nature of Code series](tag/natureofcode.html)

This will be a very short post. I just pushed to the repository the latest version of my Python API to *nvector.c*. I finished implementing the extra functions (see full list of available function in the original *nvector.h* file).

I also added properties behavior to *x*, *y* and *z* components in the *Vector* class. With this, we can access (and modify) those components direct from the *Vector* object as they were instance attributes:

    from vector import Vector

    k = Vector(1,2,3)
    print v.x
    # 1
    v.x = 10
    print v.x
    # 10

I did this using python *property* builtin:

    cdef class Vector:
        
        cdef nvector* _vector

        #(...)

        def getx(Vector self):
            return self._vector.x

        def setx(Vector self, float x):
            self._vector.x = x

        x = property(getx, setx, doc="The 'x' compoenent of the vector")

This give us access to the inner elements of our struct *_vector* without having to explicitly access the struct every time. For more informations about Python property check the [Python Documentation](http://docs.python.org/2/library/functions.html#property).

The current version of *vector.pyx* can be found [here](https://github.com/alvesjnr/nature-of-code/blob/ec7194dbca5d98c80173d2eff72fa86598b5be1f/src/vector.pyx) **Warning: permalink**

I appreciate your curiosity :)
