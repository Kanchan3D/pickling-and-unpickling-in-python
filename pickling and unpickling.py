'''“Pickling” is the process whereby a Python object
    hierarchy is converted into a byte stream,
    and “unpickling” is the inverse operation,
    whereby a byte stream (from a binary file or bytes-like object)
     is converted back into an object hierarchy.'''
import pickle

# data already stored to be converted into byte stream
data=['Ram',99,20]


#pickling
byte=pickle.dumps(data)
print(byte)

#unpickling
data1=pickle.loads(byte)
print(data1)