__author__ = 'alessandro'
from xml.dom import minidom

class Tokenizen_file:
    """it represents the xml file that contains all the information about the related cpp file and the tokens"""

    def __init__(self, file_name):
        self.line_no = 0
        self.file_name = file_name
        self.file_tree = minidom.parse(file_name)
        self.item_list = self.file_tree.getElementsByTagName('line')
        self.size = len(self.item_list)

    def token_at(self, i):
        if i >= self.size or i + self.line_no >= self.size:
            return Token("TOK_DONT_CARE", 0, "")
        token = self.item_list[self.line_no + i].attributes['token'].value
        line = self.item_list[self.line_no + i].attributes['number'].value
        text = self.item_list[self.line_no + i].attributes['text'].value
        return Token(token, line, text)

    def next(self):
        self.line_no += 1

    def size(self):
        return self.size


class Token:

    def __init__(self, token, line, text):
        self.token = token
        self.text = text
        self.line = line


class ClassCollection:

    def __init__(self):
        self.classes = []

    def add_class(self, class_to_insert):
        class_present = False
        for c in self.classes:
            if c.name == class_to_insert.name:
                class_present = True
        if not class_present:
            self.classes.append(class_to_insert)

    def index_of(self, class_obj):
        return self.classes.index(class_obj)

    def class_from_name(self, name):
        """creates or return the class with that name"""
        for c in self.classes:
            if c.name == name:
                return c
        new_class = Class(name)
        self.classes.append(new_class)
        return new_class



class Class:
    """object to keep information about the current class"""

    def __init__(self, file_name):
        self.name = self.class_name_from_file_name(file_name)
        self.file = ''
        self.line = 0
        self.superclasses = []
        self.instances = []
        self.class_parentheses = 0
        self.class_scope = False
        self.is_superclass = False

    def set_file_name(self, file_name):
        self.file = file_name

    def set_line(self, line):
        self.line = line

    def set_superclass(self):
        self.is_superclass = True

    def class_name_from_file_name(self, file_name):
        file_name_split = file_name.split('/')
        file_name_w_extension = file_name_split.pop()
        file_name_w_extension_split = file_name_w_extension.split('.')
        return file_name_w_extension_split[0]

    def change_class(self, name):
        self.class_parentheses = 0
        self.class_scope = True
        self.name = name

    def class_parentheses_increase(self):
        if self.class_parentheses == 0:
            self.class_scope = True
        self.class_parentheses += 1

    def class_parentheses_decrease(self):
        self.class_parentheses -= 1
        if self.class_parentheses == 0:
            self.class_scope = False


class Instance:
    """information about the call"""

    def __init__(self, class_instantiated, call_type, code_line, file_name):
        self.call_type = call_type
        self.class_instantiated = class_instantiated
        self.code_line = code_line
        self.file_name = file_name