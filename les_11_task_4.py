def fake_string(init_string: str, old_word: str, new_word: str, nums: int) -> str:
    """Replacing a word in a string"""
    return init_string.replace(old_word, new_word, nums)


print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))
print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2))
