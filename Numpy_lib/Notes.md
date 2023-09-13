## Numpy library

**General notes**
Methods and functions of numpy, used to compute things like the sum of the elements of an array, create a random integer array, amongs other things.

```python
import numpy as np

#sample from [0.0, 1.0)
np.random.rand((n,m)) #provide a tuple for dimensions

#sample from normal
np.random.normal(50, 10, size =(n,m)) #change mean to 50 and s.d. to 10

#random number from range
np.random.randint(0,10, size=n) #range [0, 10), squre

a = np.random...
a.shape #returns shape of the object
a.size #return the multiplication of the dimensions
len(a.shape) #number of dimensions
a.dtype #return the type of the elements

a.sum() #return the sum of all elements
a.sum(axis=1) #return sum along each row
a.sum(axis=0) #return sum

np.argmax(array) #returns index of max value in array
array[:, 0:3:2] #select columns 0, 2 for every row
indices = np.array[1,1,2,3]

a[indices] #returns the values of 'a' at the indices
a[a<mean] #masks all the values that do not fulfill the condition
```

**Other (more comlex) functions**

