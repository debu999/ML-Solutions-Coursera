def seq_cls(immutable):
    if immutable:
        cls = tuple
    else:
        cls = list
    return cls


tp = seq_cls(immutable = True)
ls = seq_cls(False)

t1 = tp("Debabrata")
print(t1)
# ('D', 'e', 'b', 'a', 'b', 'r', 'a', 't', 'a')
print(type(t1))
# <class 'tuple'>

l1 = ls("Debabrata")
print(l1)
# ['D', 'e', 'b', 'a', 'b', 'r', 'a', 't', 'a']
print(type(l1))
# <class 'list'>
# Conditional statement in return is in PEP 308
def seq_cls1(immutable):
    return tuple if immutable else list



tp1 = seq_cls1(immutable = True)
ls1 = seq_cls1(False)

t2 = tp1("Debabrata")
print(t2)
# ('D', 'e', 'b', 'a', 'b', 'r', 'a', 't', 'a')
print(type(t2))
# <class 'tuple'>

l2 = ls1("Debabrata")
print(l2)
# ['D', 'e', 'b', 'a', 'b', 'r', 'a', 't', 'a']
print(type(l2))
# <class 'list'>