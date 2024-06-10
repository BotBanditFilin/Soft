def is_palindrome(data):
    normalized_data = ''.join(data.split()).lower()
    return normalized_data == normalized_data[::-1]

import sys
input_string = sys.stdin.read().strip()

if is_palindrome(input_string):
    print("YES")
else:
    print("NO")
