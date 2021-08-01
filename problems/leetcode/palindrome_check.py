def is_palindrome(s: str) -> bool:
    start = 0
    end = len(s) - 1

    while start < end:
        if (s.isnumeric() or s.isalpha()) and s[start].lower() != s[end].lower():
            return False
        start = start + 1
        end = end - 1
    return True


def main():
    # s = "A man, a plan, a canal: Panama"
    # s = "AMMA"
    s = "race a car"
    print(is_palindrome(s))


if __name__ == "__main__":
    main()
