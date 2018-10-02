[![Build Status](https://travis-ci.com/chapman-phys220-2018f/CHANGEME.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/CHANGEME)

# PHYS220/MATH220/CPSC220 CW 6

**Author(s):** **Trevor, Paul**

## Specification

1. Recall the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) that specifies proper coding style in Python for Google. You will use this style guide to assess both your own code and that of your class mates.
1. Critique CW 4 for your group member:
    * Open a Jupyter notebook: ```critique.ipynb```
    * Have one member of your group (the "reviewee") open the python code for their previous CW04 (i.e., the module, the test module, and the Juyter notebook). Have the other member (the "reviewer") constructively critique the code in a clearly labeled section of the critique Jupyter notebook. Use the following questions as a guideline: Is it clear how the code is organized? Is the code properly documented with both docstrings and supplementary comments according to industry standards? Can you follow the algorithm of the code, i.e., what it is doing, and how? Does the code work? (Try cloning the respository and running it yourself to make sure it runs correctly.) Do you see any suggestions for how to improve the code? Are the test cases in the test module run by the code automatically by Travis? Do the tests verify correct functionality? On a scale of 0-100, the reviewer should rate the work produced by the reviewee. As the reviewer writes this critique and evaluation into the Jupyter notebook, the reviewer should discuss these questions and any issues that arise with the reviewee.
    * Repeat this exercise, but swapping roles of "reviewee" and "reviewer", and record the second critique in a new section of the notebook.
1. From CW05 copy your module ```elementary.py``` into this classwork repository. You will be using this class to vizualize the motion of a particle in a gravitational field. Also copy in the test modules from CW05 so that you have someting to test in Travis. We will not be adding any further tests for this week's assignment.
1. Consult the notebook ```example_notebook.ipynb``` for an example of how to use the ```matplotlib``` plotting module. This module is a python clone of how MATLAB plotting code functions, and is well-used in industry. Note the import statements at the top of the notebook, including the simple line for how to change the (terrible) defaults of matplotlib into the (more reasonable) defaults of the plotting module ```seaborn``` based on matplotlib. Pay attention to how you can structure your notebook to look nice - take pride in your work as a professional. If you want further examples of how to structure notebooks, take a look in the ```info``` repository.
1. In a new notebook, ```CW06.ipynb```, work with your teammate to import ```elementary.py``` create 1 generic ```Particle``` instance, 1 ```Electron``` instance, and 1 ```Proton``` instance. In your notebook show that each has different mass. Give each particle an initial momentum of $\vec{p}_0 = (10\,\text{kg m/s})\,\hat{k} \sim (0,\,0,\,10)\,\text{kg m/s}$ (straight up). Start the initial positions at $\vec{r}_0 \sim (0,\,0,\,1)\text{m}$, $(0,\,0,\,2)\text{m}$, and $(0,\,0,\,3)\text{m}$, respectively, where $\vec{r} \sim (x,\,y,\,z)$.
1. In your notebook, create a plot that shows the $z$ coordinate of each particle plotted as a function of time, $z(t)$, after placing each particle in a gravitational field $\vec{g}$ (see the example notebook). To do this, you will create a loop that iterates ```.move(dt)``` for a large number of time steps ```dt```. For specificity, use ```dt = 1e-2``` in units of seconds (centiseconds). For each time step ```dt```, you will apply an impulse $d\vec{p}$ to each particle (see example notebook) from the gravitational field, then apply the ```.move(dt)``` method and store the new $z$ coordinate of each particle. After you have accumulated $5$ seconds worth of time steps, plot each particle trajectory $z(t)$ on the same graph. Be sure to label each particle distinctly, and use different styles so that you can easily distinguish the particles. Be sure to use the proper list of time steps on the horizontal axis, such that it matches correctly with all lists of vertical positions on the vertical axis. Comment about your findings regarding how electrons, protons, and generic particles all move in a gravitational field.
1. As a side note, ```matplotlib``` is a powerful visualization library that we will be using much more in this class. If you wish to start browsing through its many features, take a look at the following links. Note that most of these examples use ```numpy``` arrays, which we will introduce next week.
    1. https://www.labri.fr/perso/nrougier/teaching/matplotlib/
    1. https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html
    1. https://matplotlib.org/tutorials/index.html

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have. You can use the GitHub web interface to edit this file directly for now.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAMES**
