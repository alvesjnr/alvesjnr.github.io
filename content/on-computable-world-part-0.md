Title: On Computable World - Part 0
Date: 2013-12-19 10:20
Tags: math, compsci, computation, Turing
Category: Math
Slug: on-computable-world-00
Author: Antonio Ribeiro
Summary: What do I think about numbers and computatble numbers.

What is computable?
------------------

So I decided to start a series of posts about __'What is computable'__, but what do I mean about computable?

The computer world nowadays becomes so complex, with lots of levels separating me as a computer engineer and the computer as a machine. What I intend with this post series is to come back to the origin of the idea of computable, to approach to the ancient concept of computable numbers and computable machine, and to create, using these foundations, our own computer architecture.

So, to begin let's go back to the concept of numbers: what is a number? On the beginning of humanity, number was introduced on the humans life to practical reasons: to count. To do this, natural numbers were enough. A former had the necessity of know (and store this value) how many cows, goals, sheep he had. To do this, natural numbers fits well. Just a note here: at this point the concept of zero as a number was unknown. Zero was not considered as a number, and it makes sense in this scenario: if the farmer didn't have any cow, why does he would represent it?

But in a determined moment on the human history, integers number were not doing all the necessary work. How would I represent the distance between two points? Let's say that we represent this value using multiples of a small unity, as a foot, for instance. This might works to represent relatively large distance, as the distance between my house and the church (127 feet) or the distance between my city and Paris(99713 feet). Natural numbers fits nice to do this work, but how would I represent the distance among my finger and the center of my hand using natural numbers in this scale? This distance is shorter than a foot, so I have two possibilities: to approximate it to one foot, or to approximate it to zero foot (assuming the existence of zero as a number).

So, to this work we lay in lack of representativity of the natural numbers. With natural numbers we are not able to represent a portion of a quantity, we just can represent multiples of a unity of this quantity. So, at this moment the rational numbers fits nice.

Rational numbers is any number which can be represented by the ratio of two integers. It makes any natural also a rational number, for instance,

_4/2=2_

But it introduces us to some very interesting numbers, which were not present as an natural number. With this way to represent number we are not anymore limited to multiples of a unity, we could represent sub-multiples of it. So, to represent the distance among my finger and the center of my hand now I could use rational numbers, and it becomes: _1/2_ foot.

At this moment a completely new world was introduced. The old world where numbers was discrete points became (apparently) continuous, with much more possibilities to represent what we need.

Is this the real life? Or is this just fantasy?
-----------------------------------------------

But at some time weird numbers becomes to us, and it was quite difficult to represent it using rational numbers. Example of numbers where the rational representations doesn't fits was popping every time. Numbers as

_sqrt(2)_

_sqrt(3)_

_pi_

_e_

were becoming more usual in the math world, but the available tools doesn't represents them very well. At some time a questions was done: is the rational numbers enough to represent any existing number? Or there are number which couldn't be represented as a ratio of two natural numbers? If those numbers exists, how to prove it?

Sometimes proving things becomes very difficult, so mathematicians introduced a way to describe a proof: the proof by contradiction. The idea is to assume that something is true, and then get into contradiction, which let us to prove exactly the contrary.

So, to check if the rational numbers is actually enough to represent any possible number, let's assume that every number is rational. So, it let numbers as _1_, _2_, _3_, _1/4_, _0.888_ became rational. For this it is okay, because we actually know that those number are rational. But what about a number that we are not that sure about? Lets pick _sqrt(2)_. According to our assumption, _sqrt(2)_ is a rational number, so it can be represented as a ratio of two natural numbers:

![Math - a/b = sqrt(2)](http://alvesjnr.github.io/blog/static/on_computable_p0_img1.png)

In this case, not _a_ and _b_ can be even numbers, at least one of they must be an odd number. Why? Let's assume that both are even, so we could divide both by _2_, which give us a new representation of the same number. An we are able to repeat this action until at least one of this two numbers becomes odd.

From this representation, after a very simple manipulation we get:

![Math](http://alvesjnr.github.io/blog/static/on_computable_p0_img2.png)

![Math](http://alvesjnr.github.io/blog/static/on_computable_p0_img3.png)


So, with this we conclude that _a²_ is an even number, because it is equal to _2*b²_ (any natural number multiplied by two is an even number). The only way that _a²_ became an even number is if _a_ is also an even number, because only an even number multiplied by itself becomes an even number. So we can conclude that _a_ is even for this case. Our next step is to check if we can get into contradictions with this.

If _a_ is even, _b_ cannot be, it should be an odd number. And if _a_ is even, it should be 2 times any number. Let's call this new number as _c_. So _a=2*c_, what give us:

![Math](http://alvesjnr.github.io/blog/static/on_computable_p0_img4.png)

![Math](http://alvesjnr.github.io/blog/static/on_computable_p0_img5.png)

![Math](http://alvesjnr.github.io/blog/static/on_computable_p0_img6.png)

![Math](http://alvesjnr.github.io/blog/static/on_computable_p0_img7.png)

That give us _b²_ as an even number, because b² is twice a number. And also as any square root of an even number is also even, we get _b_ as an even number.

As we said, assuming _sqrt(2)=a/b_ let us into a contradiction, which proves that exists numbers that can't be represented as a ratio of two natural numbers.

As this numbers is not a ratio of natural numbers, is is called irrational number.

Now our set of numbers seems to be complete. We have ways to represent any natural number (to count), a way to represent any fractional number, as a ratio of natural, and we also proved the existence of numbers that are not represented as a ratio of two natural numbers. Add to this the possibility of negative numbers, to represent values lowers than zero, and we have a complete scenario of all possible numbers (Imaginary numbers don't care to us in this essay). Are we correct?

To make an exercise with our minds, lets think about a trick: which set is bigger, the set of all natural numbers or the set of all __even__ natural numbers? Maybe our first answer is that the set of all natural numbers has twice the size of the set that contains just the even ones. But the amount of natural numbers are infinity, and quickly we get confused ... Lets try again:

Set of all natural numbers (let's forget the zero for those cases):

s = {1, 2, 3, 4, 5, ... }

Set of all even numbers:

s_e = {2, 4, 6, 8, ...}

If we look into those sets, we can make an correlation among the first set and the second one. In another word, we can enumerate the set of even numbers using the set of natural numbers, what give us:

s_e = {1->2, 2->4, 3->6, 4->8, ...}

So, for each number on the even set we have a correspondent on the natural set. What tell us that the size of both sets are the same. Does it makes sense?

Infinites and Infinites
-----------------------

At this point it was necessary to add another concept to tell about infinite sets: the concept of countable. A set is countable if we are able to order any element of this set in a proper order.

As we show above, we was able to enumerate the set of even numbers. We are also able to enumerate the set of all rational numbers, for instance:

s = {1/1, 1/2, 2/2, 1/3, 2/3, 3/3, 1/4, 2/4, 3/4, 4/4 ...}

Don't care if we get some repeated numbers inside our set, the true here is that is possible to list all the rational numbers inside a set, which make then a countable set. But what about irrational numbers?

[some!] Irrational numbers can be represented as the root of a algebraic function, just like:

![Math](http://alvesjnr.github.io/blog/static/on_computable_p0_img8.png)

As the exponent _N_ of the polynomial equation is a natural number and each one of its coefficients are integers, for any particular equation we get a finite number of solutions. If we get the sum of all coefficients and the exponential as an index of the equation, is it possible to list all integers that can be represented by the solution of an algebraic function in a set. Which make this set enumerable.

The question now is: is the set of all existent number enumerable?

Defining the Undefined
----------------------

Let's again suppose that something is possible even if we are not sure about it. Lets assume that is it possible to enumerate the set which contains every single number existent. To this becomes true we should be able, for instance, to enumerate the set that contains every single number between 0 and 1 (open interval in both sides). So, let's try:

_0.4276387832 ..._

_0.1414213562 ..._

_0.1231231231 ..._

_0.3333333333 ..._

_0.1000000000 ..._
_..._

And this list go on ... But remember, this list is infinity. Our question is: is it complete?

Is it easy to prove that, no matters how big is this list, it is aways incomplete. Let's pick the values on the diagonal of this list (forget the 0., let's take care just of the decimal part). In another words, let's get the first element of the first number, the second element of the second number, and so. At the end we get:

_44330 ..._

So, let's add _1_ to each element of this number. If the element is _9_ it will become _0_:

_55441 ..._

And place this number in our scale from 0 to 1, which give us:

_0.55441 ..._

So, is this number in our previous list? Doing it step by step, is this number the first one? No, because the first element is different (we added one to it). Is this number the second one? Also it isn't, because the second element is different. Is this number the _n_ th? No, because de _n_ th element is different.

So, it proves that, no matter how complete is our set, it will be aways missing numbers on it. 

What does it tell us? Remember, the set of natural numbers is enumerable. The set of rational is also enumerable. Even the set of algebraic numbers is enumerable. But the set of all possible numbers isn't! Which means that there are some numbers that are not neither natural, nor integer, nor algebraic. Those numbers are called transcendental numbers. One classic transcendental number is __π__. Which means that there is not a algebraic function which the root is __π__.

But, if there is not an algebraic way to obtain an transcendental number, how can it be obtained? One way to obtain it is through the series of sums. One example of series of sum is the Leibniz formula for __π__:

![Math](http://alvesjnr.github.io/blog/static/leibniz_pi_series.png)

This way to obtain _pi_ is nothing but an __algorithm__. And here is where our tour through the computable world begins.
