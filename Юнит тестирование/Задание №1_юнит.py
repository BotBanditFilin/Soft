def is_palindrome(data):
    normalized_data = ''.join(data.split()).lower()
    return normalized_data == normalized_data[::-1]

def test_is_palindrome():
    tests = [
        ("А роза упала на лапу Азора", True),
        ("радар", True),
        ("привет", False),
        ("", True),
        ("Аргентина манит негра", True),
        ("Я вижу зверей в зазеркалье", False),
        ("Не палиндром", False)
    ]

    for test_str, expected in tests:
        result = is_palindrome(test_str)
        if result != expected:
            print("NO")
            return
    print("YES")

test_is_palindrome()
