numbers = {
    "high": 100,
    "medium": 50,
    "low": 10,
}

result = []
for elem in numbers.values():
    result.append(int(elem / 2))

print(result)  # [50, 25, 5]
