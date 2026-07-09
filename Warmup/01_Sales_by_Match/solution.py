def sockMerchant(n, ar):
    # Dictionary to store frequency of each sock color
    freq = {}

    # Count frequency of each color
    for color in ar:
        if color in freq:
            freq[color] += 1
        else:
            freq[color] = 1

    # Count pairs
    pairs = 0
    for count in freq.values():
        pairs += count // 2

    return pairs
