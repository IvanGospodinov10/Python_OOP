def vowel_filter(function):
    def wrapper():
        filtered_vowels = ["a", "e", "i", "o", "u", "y"]
        result = function()
        return [el for el in result if el.lower() in filtered_vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
