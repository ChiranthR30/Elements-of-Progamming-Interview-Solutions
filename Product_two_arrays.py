#multiply two arrays
def multiply_arrays(arr1, arr2):
    len1, len2 = len(arr1), len(arr2)
    
    # Initialize a result array with zeros
    result = [0] * (len1 + len2)
    
    # Multiply the digits and update the result array
    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            product = arr1[i] * arr2[j]
            p1, p2 = i + j, i + j + 1  # Position indices for two digits in the result
            total = product + result[p2]  # Add the product and any existing value at p2
            result[p1] += total // 10  # Carry to the previous position
            result[p2] = total % 10  # Update the current position
    
    # Remove leading zeros from the result
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    
    return result

# Example usage:
num1 = [2, 3]  # Represents the number 23
num2 = [4, 5]  # Represents the number 45
result = multiply_arrays(num1, num2)
print(result)  # Output: [1, 0, 3, 5] (represents 23 * 45 = 1035)
