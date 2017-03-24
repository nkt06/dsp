# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples are both sequences, but lists are mutable while tuples are immutable. Tuples will work as keys in dictionaries because they are comparable and hashable.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Python lists and sets are different in that sets cannot contain duplicates, are unordered and can only contain hashable elements. Python lists and sets are similar in that they are both collections of elements. It is faster to find an element in a set because in lists the elements are accessed by iterating over the list, whereas a set is hashable so an element can be found by directly mapping the element to a unique index without having to iterate over the entire set.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's lambda is a keyword used to generate anonymous functions. It can be used to sort complex objects using some of the object's indices as a key. E.g. sorted(x_tuples, key=lambda x: x[2])

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is used to take an existing sequence and perform some function and/or filter to it, resulting in a new list. 
> > E.g. things = [3, 4, 6, 7, 0, 1]
> > print [x*2 for x in things if x % 2 == 0]
> > Equivalent with 'map' and 'filter':
> > print map(lambda x: x*2, filter(lambda y: y % 2 == 0, things))
> > Both have the same capabilities, but list comprehensions are more direct and clearer.
> > Set comprehensions are used to take an existing sequence and perform some function and/or filter to it, resulting in a new set. 
> > E.g. In a list of names, we are only interested in names longer then one character and wish to represent all names in the same format: The first letter should be capitalised, all other characters should be lower case.
> > names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]
> > { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }
> > Dictionary comprehensions are used to take an existing sequence and perform sum function and/or filter to it, resulting in a new dictionary.
> > E.g. We require a dictionary in which the occurrences of upper and lower case characters are combined.
> > mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
> > { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys() }

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





