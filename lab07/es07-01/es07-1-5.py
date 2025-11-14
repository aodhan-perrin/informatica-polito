def same_set(a: list, b: list) -> bool:
	return sorted(set(a)) == sorted(set(b))


a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
b = [11, 11, 7, 9, 16, 4, 1]

print(same_set(a, b))
