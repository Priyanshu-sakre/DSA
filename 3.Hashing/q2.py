def getFrequencies(v: List[int]) -> List[int]:
    n = len(v)
    hashMap = {}
    for num in v:
        hashMap[num] = hashMap.get(num, 0) + 1

    minFreq = float("inf")
    minElement = float("inf")
    maxFreq = float("-inf")
    maxElement = float("inf")

    for key, freq in hashMap.items():
        if freq > maxFreq or freq == maxFreq and key < maxElement:
            maxFreq = freq
            maxElement = key
        if freq < minFreq or freq == minFreq and key < minElement:
            minFreq = freq
            minElement = key
    return [maxElement, minElement]
