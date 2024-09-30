numbers = [float(x) for x in input("Enter numbers: ").split()]
print("Average:", sum(numbers) / len(numbers))
print("Largest:", max(numbers))
print("Smallest:", min(numbers))