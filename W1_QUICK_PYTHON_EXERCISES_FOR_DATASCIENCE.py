
##******** 1- QUICK PYTHON EXERCISES FOR DATA SCIENCE / PART 1 ##*********

#1 What is virtual environment ?

# In short [*] : Creating a virtual environment to isolate projects with different needs.
# Different versions of libraries, packages or modules can be kept.
# They can work without affecting each other.

    # 1.1 FORMAL DEFINITION :

    '''The venv module provides support for creating lightweight “virtual environments” with
    their own site directories, optionally isolated from system site directories.
    Each virtual environment has its own Python binary (which matches the version of the binary that
    was used to create this environment) and can have its own independent set of installed Python packages in
    its site directories.[1]'''

#2 What is Conda ?

# In short it is a tool for creating Virtual Environment and manage it. You can also make dependency management

    # 2.1 FORMAL DEFINITION :

    ''' Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, 
        JavaScript, C/ C++, FORTRAN, and more.
        Conda is an open source package management system and environment management system that runs 
        on Windows, macOS and Linux. 
        Conda quickly installs, runs and updates packages and their dependencies. 
        Conda easily creates, saves, loads and switches between environments on your local computer. 
        It was created for Python programs, but it can package and distribute software for any language. [2]'''

#3 What is Dependency Management ?

# In short it is as it's name Dependency and Package management.
# (Package like Numpy, Pandas etc... ) so that is, the management of these and the tools
# that manage the dependencies of these packages.

        # 3.1 FORMAL DEFINITION :

        ''' Conda as a package manager helps you find and install packages. 
        If you need a package that requires a different version of Python, you do not need to switch to 
        a different environment manager, because conda is also an environment manager. 
        With just a few commands, you can set up a totally separate environment to run that different version of
        Python, while continuing to run your usual version of Python in your normal environment. [3] '''

#4 Use string format and print the personnel "no & name"

personnel = {"name": "John", "no": 63323}
"name : {} ,  no : {}".format(personnel["name"],personnel["no"])

#5 Print the "name" and "no" with fstring.

name = "Connor"
no = 63324
f"Name: {name} , No: {no}"

#6 Please divide the sentence below with the split()

sentence=" Hello Data Science World "
sentence.split()

#7 Please remove the "H" letters and spaces in the sentences below by using strip() with two separate operations.

sentence=" Hello Data Science World "
sentence.strip()
sentence2="Hello Data Science WorldH".strip("H")
sentence2.strip("H")

#8 Take a number from the user by input function. Assign the number to the no variable. Multiple by 8 and
#divede by 2

no= int(input())
no*8/2

#9 Create an employee list. Use dir() to see the possible processes that you can do . Use append() to add
# employee name "Ulas" to the list and then apply pop() method to remove the third element.

employees = ["John","Connor","Sarah","Arnold"]
dir("John")
employees.append("Ulas")
employees
employees.pop(3)
employees

#10 Create a tuple with 6 element and print the first 5 of it.

my_tuple=(1,2,"3",4,'5',6)
my_tuple[:5]

#11 WHAT IS ENUMERATE ?

# In short [*] : Enumeric automatically generates an index, ie counter, in a loop.
# Thus, the elements of a list or any object to be visited in it are automatically indexed.
# This is a life saver to match, track and transact on it.

    # 11.1 FORMAL DEFINITION :

    """In computer programming, an enumerated type
    (also called enumeration, enum, or factor in the R programming language,
    and a categorical variable in statistics)
    is a data type consisting of a set of named values called elements,
    members, enumeral, or enumerators of the type.[4]"""

    # 11.2 ADDITIONAL DEFINITIONS AND USAGE :
    #
    #
    # The enumerate() method creates a counter that tracks how many iterations have occurred in a loop.
    # enumerate() is built-in to Python, so we do not have to import any libraries to use
    # the enumerate() method [5]
    #
    # The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
    # The enumerate() function adds a counter as the key of the enumerate object.[6]


#12 Write a program with enumerate that gives the output below from the list
employee = ["Ulas", "John", "Connor", "Sarah"]
'''REQUIRED OUTPUT :
0 Ulas
1 John
2 Connor
3 Sarah
'''

 for index,name in enumerate(employee):
     print(index,name)

#13 Write a program with enumerate that gives the output below from the list.
'''REQUIRED OUTPUT : 
1 Ulas
2 John
3 Connor
4 Sarah'''

employee = ["Ulas", "John", "Connor", "Sarah"]
for index, name in enumerate(employee,1):
    print(index, name)

#14 Create 2 groups from employee list. If index is even assign it to the group X otherwise group Y.
# Use enumeration

X=[]
Y=[]
for index, name in enumerate(employee,1):
    if index%2 == 0:
        X.append(name)
    else:
        Y.append(name)

#15 Create a functional solution for question 14

def employeeGroups (employee):
    empGroups=[[],[]]
    for index, name in enumerate(employee, 1):
     if index % 2 == 0:
        empGroups[0].append(name)
     else:
        empGroups[1].append(name)
    print(empGroups)

employeeGroups(employee)

#16 Write a modifier function which takes a sentence as an argument . If index is even turn it to lower case
# otherwise to upper case.

def modifier(string):
    modSentence= ""
    for i in range(len(string)):
        if i%2==0:
            modSentence+=string[i].lower()
        else:
            modSentence+=string[i].upper()
    print(modSentence)

modifier("Hello World")


#17 What is Map Function for ?

# In short: Map  means to matching. It provides the possibility to apply
# a certain function to each element of an iterative object without writing a loop.

    # 17.1 FORMAL DEFINITION :
    ''' Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.[7] '''

    # 17.2 ADDITIONAL DEFINITIONS AND USAGE :
    #
    #
    # map(function, iterable, ...)
    # Apply function to every item of iterable and return a list of the results.
    # If additional iterable arguments are passed, function must take that many arguments
    # and is applied to the items from all iterables in parallel.[8]

#18 	Please write a new_prices function which modifies the prices  by additional 30 % .
#   Then map this function into the list.

prices = [10000, 20000, 30000, 40000, 50000]

def new_prices(p):
    return p*30/100 + p

list(map(new_prices,prices))

#19 For question 8 now apply lambda with map function. Don't write a new_prices function .
# Just write it's features #with lambda function.

list(map(lambda x: x+x*30/100,prices))

#20 Please filter the num_list's even numbers with lambda in Filter() function.

num_list = [0,1,11, 22, 33, 44, 55, 66, 77, 88, 99, 100]

list(filter(lambda x: x%2==0,num_list))

#21 We would like to make summation in the num_list numbers with Reduce fuction.
# Please write the necescary code.

from functools import reduce
reduce(lambda x,y: x+y,num_list)

    # 21.1 : Please explain what Reduce () function.
    # In short Reduce() function just makes reduction.

    # FORMAL DEFINITION :
    """
    def reduce(function, sequence, initial=_initial_missing):
    reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty. [9]
    """

#22 What is list comprehension for ?

# In short It is a list operation that allows the outputs to remain as a list with a faster effort
# as a result of a series of operations.

    # FORMAL DEFINITIONS :

    '''List comprehension offers a shorter syntax when you want to create a new list based on the values of
    an existing list.[10]'''

    #List comprehensions provide a concise way to create lists. Common applications are to make new lists
    # where each element is the result of some operations applied to each member of another sequence
    # or iterable, or to create a subsequence of those elements that satisfy a certain condition. [11]

#23  Please multiple every price in price list by 3 and hold them in the list compherension.
prices = [10000, 20000, 30000, 40000, 50000]

[i*3 for i in prices ]

    #23.1- At that time If prices are lower than 30000 multiple by 3 . Use list compherension
        [i*3 for i in prices if i<30000 ]

    #23.2- At this time If prices are lower than 30000 multiple by 3 .  otherwise apply
    # new_prices() . Use list compherension
        [i * 3 if i < 30000 else new_prices(i) for i in prices ]

    #23.3- At this time If prices are lower than 30000 multiple by 3 and apply new_prices(). Otherwise only apply
    # new_prices() . Use list compherension
        [3*new_prices(i) if i < 30000 else new_prices(i) for i in prices ]

#24 When to use the list comprehensions ?

# In short  when we want to processes easier

    # FORMAL DEFINITIONS :

    ''' List comprehensions provide us with a simple way to create a list based on some iterable.
    # During the creation, elements from the iterable can be conditionally included
     in the new list and transformed as needed.[12] '''

#25 There are 2 list exist. Use List comprehension.Loop in "employee" list and create a new list.
# if the names in "employee" exist in the "non_employee" list write the first letters of them
# in lower case to the new list. Add the other names in capital case to the list.

employee = ["Ulas", "John", "Connor", "Sarah"]
non_employee = ["John", "Sarah"]

[i.lower() if i in non_employee else i  for i in employee]

#26 What is Dictionary Comprehensions {} and when to use ?

# In short it is a structure that keep keys and values in pairs.
# We use "{}" When we want to keep key and value
# operation results as a dictionary .

    # FORMAL DEFINITIONS :

    ''' Returns a dictionary based on existing iterables.[13]'''

#27 What happens when key(),value(),items() functions used sequentially on dictionary ?
dictionary = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

dictionary.values()
dictionary.keys()
dictionary.items()

#28 Use DC (Dictionary Comprehension) and take the second power of all values in "dictionary".

{ keys:values**2 for keys,values in dictionary.items() }

    #28.1  Use DC (Dictionary Comprehension) and turn to the capital case of all keys in "dictionary".

    { keys.upper():values for keys,values in dictionary.items() }

    #28.2 Double the keys existing values
    { keys*2:values for keys,values in dictionary.items() }

#29 Print the even numbers with Dictionary Comprehension as key and their square as value
    numbers = range(10)

    { keys: keys**2 for keys in numbers if keys%2==0 }

#SOURCES :

#[*]:  All information started with `In short` : https://www.veribilimiokulu.com -  Mr Mustafa Vahit Keskin ( Data Scientist ) -  DSMLBC4 (2021)
#[1]:  https://docs.python.org/3/library/venv.html
#[2]:  https://docs.conda.io/en/master/
#[3]:  https://docs.conda.io/en/master/
#[4]   https://en.wikipedia.org/wiki/Enumerated_type#:~:text=From%20Wikipedia%2C%20the%20free%20encyclopedia,or%20enumerators%20of%20the%20type.
#[5]:  https://careerkarma.com/blog/python-enumerate/
#[6]:  https://www.w3schools.com/python/ref_func_enumerate.asp
#[7]:  https://docs.python.org/3.8/library/functions.html#map & jetbrains help documentation
#[8]:  https://stackoverflow.com/questions/10973766/understanding-the-map-function
#[9]:  https://docs.python.org/3.8/library/functools.html#functools.reduce
#[10]: https://www.w3schools.com/python/python_lists_comprehension.asp
#[11]:  https://docs.python.org/3/tutorial/datastructures.html
#[12]:  https://towardsdatascience.com/python-basics-list-comprehensions-631278f22c40
#[13]: https://python-reference.readthedocs.io/en/latest/docs/comprehensions/dict_comprehension.html