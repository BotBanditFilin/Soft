import sys
import re

def is_correct_mobile_phone_number_ru(number):
    pattern = re.compile(r'^(8|\+7)[-\s]?(\(?\d{3}\)?)[-\\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})$')
    return bool(pattern.match(number))

input_string = sys.stdin.read().strip()

if is_correct_mobile_phone_number_ru(input_string):
    print("YES")
else:
    print("NO")
