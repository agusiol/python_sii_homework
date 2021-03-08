class FunWithWords:
    """Class with funccitions checking words if words/phreases
    are anagram or palindrom"""

    def __init__(self, text):
        self.text = text

    def is_palindrom(self):
        text = self.text.lower().replace(" ", "").strip('.!?')
        return text == text[::-1]

    def is_anagram(self, text2):
        text1 = sorted((c for c in self.text.lower() if c not in ' !.,'))
        text2 = sorted((c for c in text2.lower() if c not in ' !.,'))
        return text1 == text2

    def is_panagram(self):
        pass


# a = FunWithWords("A to kawa kota?")
# print(a.is_palindrom())
