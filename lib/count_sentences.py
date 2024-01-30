#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''  # Use a private attribute to store the value
        self.value = value  # Use the setter for initial assignment

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        temp_value = self._value.replace('?', '.').replace('!', '.')
        sentences = [sentence for sentence in temp_value.split('.') if sentence]
        return len(sentences)


