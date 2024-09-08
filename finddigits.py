import math
def findDigits(n):
     
    # factorial exists only for n>=0
    if (n < 0):
        return 0;
 
    # base case
    if (n <= 1):
        return 1;
 
    # else iterate through n and 
    # calculate the value
    digits = 0;
    for i in range(2, n + 1):
        digits += math.log10(i);
 
    return math.floor(digits) + 1;
 
# Driver code 
print(findDigits(2000));