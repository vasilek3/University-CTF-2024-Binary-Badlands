# Input two arrays as strings
signals = list(map(int, input().split(", ")))  # First input array as a string
weights = list(map(int, input().split(", ")))  # Second input array as a string

def max_signals_amount(signals, weights):
    modified_signals = []
    for i in range(len(signals)):
        modified_signals.append(signals[i] * weights[i])
    print(modified_signals)
    max_number = -10 ** 9
    for start in range(len(modified_signals)):
        neutral_number = 1
        for end in range(start, len(modified_signals)):
            neutral_number *= modified_signals[end]
            max_number = max(max_number, neutral_number)

    return max_number

print(max_signals_amount(signals, weights))

# author: voloshka_3 / vasilek_3 
# name: Weighted Starfield
# level: medium
