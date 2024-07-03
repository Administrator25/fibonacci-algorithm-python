def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def fibonacci_up_to_value(max_value):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= max_value:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print("Die ersten 10 Fibonacci-Zahlen sind:")
print(fibonacci_sequence(10))

print("Fibonacci-Zahlen bis zu einem maximalen Wert von 100:")
print(fibonacci_up_to_value(100))
