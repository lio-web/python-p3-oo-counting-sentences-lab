class MyString:
    '''A class to handle strings.'''
    
    def __init__(self, value=""):
        if not isinstance(value, str):
            print("The value must be a string.")
        self._value = value if isinstance(value, str) else ""
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        # Split the string by ".", "?", or "!" followed by optional spaces
        import re
        sentences = re.split(r'[.!?]+\s*', self._value.strip())
        # Filter out any empty strings in the result
        return len([s for s in sentences if s])
