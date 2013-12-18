Title: How Does a Spirograph Work
Date: 2013-12-18 10:20
Tags: thats, awesome
Category: yeah
Slug: my-super-post
Author: Antonio Ribeiro
Summary: Short version for index and feeds


Some of you shall ask yourselves: "How does a spirograph work?". But I'm sure that most of you would ask me: "What the wacko is an spirograph?"

An spirograph is a toy used to draw "weird spirals" using two circles (one inside other). For whom doesn't remember, the toy is these one:

![Espirografo]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/spirograph_01.jpg "Espirografo")

The way that this toy works is simples: One gear spins inside a big circle (also with gears!). The pen is placed in a hole of the gear. When you spin the gear through the major circle, the pen follows tho different movements: An circle movement made by the gear around the center of the great circle (let's call this point as O) and a movement made by the pen around the center of the gear (let's call the center of the gear as C and the point where the pen is placed as P). As the center of the gear is moving, the result position of the point P is the sum of these two movements: P over C plus C over O.

![desenhos muito doidos de São Tomé]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/spirograph_02.jpg "desenhos muito doidos de São Tomé")

But what we want at this point is: how to reproduce these traces? How can we parametrize the equation that give us the point P(x,y) as the gear spins. You must not believe at this moment, but these equations are pretty easy to find.

First of all let's define some things. As I'm not a mathematician (nor sick) let's put the center of our circle in the origin of our coordinates system. Let's call the center of the circle as O (origin). Let's also call as R the radius of this circle.

The gear has two important parameters: it's radius (which will be called r) and the radius of the trace, that is, the distance between the center of the gear and the point where the pen will be placed. Let's call this radius as r'. The center of this gear will be called C. And the point where the pen is placed will be called P.

Just one more definition: let's assume that the gear translate on the counterclockwise way.

![KmPlot]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/espirografo_define.png "blah")

##Part I - Parameterization of the position of the point C

Once we start to trace our spiral, we move the gear counterclockwise. What we want to get at this point is the coordinates of the point C (center of the gear) over the angle theta.

![C]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/espirografo_C.png "blah")

Letting (R-r) be the distance between the origin O and the center of the gear, we get:

![equ_C]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/equ_c.gif "blah")

And here we've just got the position (x,y) of a point of the spiral for each angle theta of our system.

##Part II - Parametrization of the pint P over the point C

Now that we already have the equations of the point C, let's look for the position of the point P over the point C. Again let's draw to easily see the equation:

![equ_Pc]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/espirografo_Pc.png "blah")

Look that when we move our gear counterclockwise (increase theta) this same gear spins (around itself) clockwise (phi decreases). It give us:

![equ_Pc]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/equ_pc.gif "blah")

The minus sign on equation y is given just because the gear spins clockwise. To better see what is heppen, let's take this initial position:

![equ_Pc]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/rodando.png "blah")

In this case we have thata=0 and phi=0. As soon as we start to move the gear clockwise through the big circle (increase theta), the point P will decrease on the y axe over the point C. That is why the value of y in this equation have the minus sign.

##Part III - Summing the values

Now that we have C over O and P over C, let's sum these equations and get P over O:

![equ_Pc]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/equ_p_theta_phi.gif "blah")

Look that our parametric function has two variables: theta and phi. But there is an correlation about those two values.

![equ_Pc]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/thetaphi.gif "blah")

What give us:

![equ_Pc]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/equ_p_theta_phi.gif "blah")

When we substitute the value of phi in the position equation we get:

![equ_Pc]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/equ_P_final.gif "blah")

And finally with just one variable (theta) and three parameters (R, r and r') we have an equation of the spirograph

Below is provided a Python script that draws the spiral by those parameters. The function that generates the point can accept also two extra parameters:

spins -> how many complete turns the gear will do
resolution -> how much is the increment of the angle phi for each point

To run this script you must have matplotlip installed in your computer

We can also plot the trace of an spirograph using any graphical software that accept parametric equations. Here we have one example using KmPlot on Ubuntu Linux:

![KmPlot]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/kmplot.png "KmPlot")
Parâmetros: 
*R*: 5
*r*: 1.1
*r'*: 1
theta: variando de 0 a 2*pi*10 (10 voltas complestas)

Some examples using the Python script:

![Python]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/espirapy_1.png "Python")

![Python]( https://github.com/alvesjnr/alvesjnr.github.io/raw/master/static/espirapy_2.png "Python")

[Python Source Code](https://gist.github.com/1948754#file_spirograph.py)

