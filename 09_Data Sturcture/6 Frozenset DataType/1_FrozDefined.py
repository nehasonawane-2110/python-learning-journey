# Frozenset data Type - 
# - A frozenset is a set that cannot be chnage after it is created (immutable set)
# 1) structure - frozenset(iterable)
# - created using frozenset () function
# - elements are written inside iterablle (list, tuple, set)
fs = frozenset({1, 2, 3, 4})
print(fs)
print(type(fs))

# 2) Type Od data - (heterogeneous)
# - can store mmltiple data types
fs = frozenset({1, 's', 3.15, True})
print(fs)
print(type(fs))

# 3) sequence - unorered
# - no indexing on ordered maintained 
fs = frozenset({1, 'a', 30})
print(fs)

# 4) Changable (immutable)
# - it is read only
# - cannot add, remove, update elements

fs = frozenset({10, 20})
print(fs)
# fs.add(23) 
print(fs)


# 5) unique elements are present