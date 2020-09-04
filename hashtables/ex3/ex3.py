def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    num = {}
    result = []
    
    for arr in arrays:
        for i in range(len(arr)):
            if arr[i] in num:
                num[arr[i]] += 1
                if num[arr[i]] == len(arrays):
                    result.append(arr[i])
            else:
                num[arr[i]] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
