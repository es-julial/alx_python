def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence
    sequence.append(0)
    if n > 1:
        sequence.append(1)

    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)

    return sequence
