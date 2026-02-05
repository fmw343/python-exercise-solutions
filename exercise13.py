def fibonacci(steps):
    seq = [0, 1]
    
    for n in range(steps):
        seq.append(seq[n] + seq[n + 1])
        print(seq[n])

fibonacci(12)
