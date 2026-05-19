d = {"a": 1, "b": 2, "c": 3}

print("Dictionary:", d)

# # 1. get()
print("get('a'):", d.get("a"))

# # 2. keys()
print("Keys:", d.keys())

# # 3. values()
print("Values:", d.values())

# # 4. items()
print("Items:", d.items())

# # 5. update()
d.update({"d": 4})
print("After update:", d)

# # 6. pop()
d.pop("b")
print("After pop:", d)

# 7. popitem()
d.popitem()
print("After popitem:", d)

# 8. clear()
temp = d.copy()
temp.clear()
print("After clear:", temp)

# 9. copy()
d2 = d.copy()
print("Copy of dictionary:", d2)

# 10. setdefault()
d.setdefault("e", 5)
print("After setdefault:", d)