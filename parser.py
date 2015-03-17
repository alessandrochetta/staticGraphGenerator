__author__ = 'alessandro'

import os
from glob import glob
from Utility import Class
from Utility import Instance
from Utility import Tokenizen_file
from Utility import ClassCollection


# Fundamental types
#
fundamental_types = ['bool', 'char', 'int', 'short', 'long', 'float', 'double', 'wchar_t', 'char16_t', 'char32_t', 'String', 'string']

# TODO: represent inheritance in the graph, multiple class inheritance, check whether the xml file is made by flex
#       deal with spaces in the source path
#

# output files declaration________________________________
# log file
log = open('staticGraphGenerator.log', 'w')
#
# json file
json_file = open('graph_visualizator/graph.json', 'w')
#
# xml file (file in which all the information about classes are stored)
xml_file = open('graph_xml.xml', 'w')

# input file retrieving_____________________________
# 'source/' is the directory in which source files are stored
file_list = [y for x in os.walk('source/') for y in glob(os.path.join(x[0], '*.cpp'))]
file_list += [y for x in os.walk('source/') for y in glob(os.path.join(x[0], '*.h'))]
#
# write in the log all the file found
log.write('Source files found: ' + str(len(file_list)) + ' \n')
for f in file_list:
    log.write('\t' + f + '\n')

# Files analysis____________________________________
# lexer converts cpp files in token in the xml format
for file_name in file_list:
    os.system("./lexer " + file_name)

# input xml file retrieving_________________________
# 'source/' is the directory in which source files are stored
file_list = [y for x in os.walk('source/') for y in glob(os.path.join(x[0], '*.xml'))]
#
# write in the log all the file found
log.write('Xml files found: ' + str(len(file_list)) + '\n')
for f in file_list:
    log.write('\t' + f + '\n')

print '\n'

# classes data structure
class_collection = ClassCollection()

# Parsing___________________________________________
# here xml files are parsed
for f in file_list:
    tok_file = Tokenizen_file(f)
    #
    # Token analysis
    #
    current_class = Class(f)
    for i in range(0, tok_file.size):
        # Scope recognition_________________________
        #
        if tok_file.token_at(0).token == 'TOK_CLASS' \
                and tok_file.token_at(1).token == 'TOK_ID'\
                and tok_file.token_at(2).token == 'TOK_COLON'\
                and tok_file.token_at(3).token == 'TOK_ACCESS'\
                and tok_file.token_at(4).token == 'TOK_ID':
            current_class = class_collection.class_from_name(tok_file.token_at(1).text)
            superclass = class_collection.class_from_name(tok_file.token_at(4).text)
            current_class.superclasses.append(superclass)
            current_class.set_file_name(f)
            current_class.set_line(tok_file.token_at(0).line)
            # set the class at tok_file.token_at(4) as superclass
            superclass.set_superclass()
            print "class changed in (subclass)" + current_class.name
            tok_file.next()
            continue

        if tok_file.token_at(0).token == 'TOK_CLASS' \
                and tok_file.token_at(1).token == 'TOK_ID'\
                and tok_file.token_at(2).token == 'TOK_COLON'\
                and tok_file.token_at(3).token == 'TOK_ID':
            current_class = class_collection.class_from_name(tok_file.token_at(1).text)
            superclass = class_collection.class_from_name(tok_file.token_at(3).text)
            current_class.superclasses.append(superclass)
            current_class.set_file_name(f)
            current_class.set_line(tok_file.token_at(0).line)
            # set the class at tok_file.token_at(3) as superclass
            superclass.set_superclass()
            print "class changed in (subclass)" + current_class.name
            tok_file.next()
            continue

        if tok_file.token_at(0).token == 'TOK_CLASS' and tok_file.token_at(1).token == 'TOK_ID':
            current_class = class_collection.class_from_name(tok_file.token_at(1).text)
            current_class.set_file_name(f)
            current_class.set_line(tok_file.token_at(0).line)
            print "class changed in " + current_class.name
            tok_file.next()
            continue

        if not current_class.class_scope \
            and tok_file.token_at(0).token == 'TOK_ID' \
            and tok_file.token_at(1).token == 'TOK_COLON_COLON'\
            and tok_file.token_at(2).token == 'TOK_ID'\
                and tok_file.token_at(3).token == 'TOK_LPAREN':
            par_count = 1
            token_index = 4
            while par_count != 0 and token_index <= tok_file.size:
                if tok_file.token_at(token_index).token == 'TOK_LPAREN':
                    par_count += 1
                if tok_file.token_at(token_index).token == 'TOK_RPAREN':
                    par_count -= 1
                token_index += 1

            if tok_file.token_at(token_index).token == 'TOK_CONST':
                token_index += 1

            if tok_file.token_at(token_index).token == 'TOK_LBRACE':
                current_class = class_collection.class_from_name(tok_file.token_at(0).text)
                current_class.set_file_name(f)
                current_class.set_line(tok_file.token_at(0).line)
                tok_file.next()
                print "class changed in " + current_class.name
                continue

        if not current_class.class_scope \
            and tok_file.token_at(0).token == 'TOK_ID' \
            and tok_file.token_at(1).token == 'TOK_COLON_COLON'\
            and tok_file.token_at(2).token == 'TOK_OPERATOR':
            token_index = 3
            par_count = 0
            while par_count != 1 and token_index <= tok_file.size:
                if tok_file.token_at(token_index).token == 'TOK_LPAREN':
                    par_count = 1
                token_index += 1

            while par_count != 0 and token_index <= tok_file.size:
                if tok_file.token_at(token_index).token == 'TOK_LPAREN':
                    par_count += 1
                if tok_file.token_at(token_index).token == 'TOK_RPAREN':
                    par_count -= 1
                token_index += 1

            if tok_file.token_at(token_index).token == 'TOK_CONST':
                token_index += 1

            if tok_file.token_at(token_index).token == 'TOK_LBRACE':
                current_class = class_collection.class_from_name(tok_file.token_at(0).text)
                current_class.set_file_name(f)
                current_class.set_line(tok_file.token_at(0).line)
                tok_file.next()
                print "class changed in " + current_class.name
                continue

        if tok_file.token_at(0).token == 'TOK_LBRACE':
            current_class.class_parentheses_increase()
            tok_file.next()
            continue
        if tok_file.token_at(0).token == 'TOK_RBRACE':
            current_class.class_parentheses_decrease()
            tok_file.next()
            continue

        if not current_class.class_scope:
            #print "this token is out of any scope: " + tok_file.token_at(0).token
            tok_file.next()
            continue

        #
        # Increment current class size
        current_class.increase_size(tok_file.token_at(0))

        # Declaration analysis____________________________________________________________________________________
        #
        # Basic declaration
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_ID' \
                and tok_file.token_at(2).token == 'TOK_SEMI':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'basic', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        #
        # Pointer declaration
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_MULT' \
                and tok_file.token_at(2).token == 'TOK_ID'\
                and tok_file.token_at(3).token == 'TOK_SEMI':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'pointer', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        # Pointer declaration Point * const p;
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_MULT' \
                and tok_file.token_at(2).token == 'TOK_CONST'\
                and tok_file.token_at(3).token == 'TOK_ID'\
                and tok_file.token_at(4).token == 'TOK_SEMI':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'pointer', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        #
        # Reference declaration
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_AMP' \
                and tok_file.token_at(2).token == 'TOK_ID'\
                and tok_file.token_at(3).token == 'TOK_SEMI':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'reference', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        # Reference declaration constant
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_AMP' \
                and tok_file.token_at(2).token == 'TOK_CONST'\
                and tok_file.token_at(3).token == 'TOK_ID'\
                and tok_file.token_at(4).token == 'TOK_SEMI':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'reference', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        #
        # Copy constructor declaration
        # possible polymorphism
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_ID' \
                and tok_file.token_at(2).token == 'TOK_ASSIGN'\
                and tok_file.token_at(3).token == 'TOK_ID':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'cpy_constr', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        # Copy constructor declaration id * id = new id
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_MULT' \
                and tok_file.token_at(2).token == 'TOK_ID'\
                and tok_file.token_at(3).token == 'TOK_ASSIGN'\
                and tok_file.token_at(4).token == 'TOK_NEW_OPERAND'\
                and tok_file.token_at(5).token == 'TOK_ID':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'cpy_constr', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        # Copy constructor declaration id * id = id
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_MULT' \
                and tok_file.token_at(2).token == 'TOK_ID'\
                and tok_file.token_at(3).token == 'TOK_ASSIGN'\
                and tok_file.token_at(4).token == 'TOK_ID':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'cpy_constr', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        #
        # Constructor invocation Point P()
        if tok_file.token_at(0).token == 'TOK_ID' \
                and tok_file.token_at(1).token == 'TOK_ID' \
                and tok_file.token_at(2).token == 'TOK_LPAREN':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(0).text)
            current_class.instances.append(Instance(instantiated_class, 'constr', tok_file.token_at(0).line, f))
            tok_file.next()
            continue
        # Constructor invocation new Point
        if tok_file.token_at(0).token == 'TOK_NEW_OPERAND' \
                and tok_file.token_at(1).token == 'TOK_ID':
            instantiated_class = class_collection.class_from_name(tok_file.token_at(1).text)
            current_class.instances.append(Instance(instantiated_class, 'constr', tok_file.token_at(1).line, f))
            tok_file.next()
            continue

        tok_file.next()

# data structures to support the file writing
#
# remove external classes
# external classes are the classes that are not declared in the code
internal_classes = []
for c in class_collection.classes:
    if c.external:
        continue
    internal_classes.append(c)

links = []
# dependencies links
for c in class_collection.classes:
    if c.external:
        continue
    for i in c.instances:
        if i.class_instantiated.external:
            continue
        links.append([internal_classes.index(c), internal_classes.index(i.class_instantiated), 0])
#
# hierarchical links
for c in class_collection.classes:
    if c.external:
        continue
    for s in c.superclasses:
        if s.external:
            continue
        links.append([internal_classes.index(c), internal_classes.index(s), 1])

#
#
#
# json file print
json_file.write('{"nodes":[\n')

for i in range(0, len(internal_classes)):
    temp_class = class_collection.classes[i]

    if temp_class.is_superclass:
        group = '1'
    else:
        group = '0'

    if len(temp_class.superclasses) > 0:
        is_subclass = 1
    else:
        is_subclass = 0

    if i == len(internal_classes)-1:
        json_file.write('{"name":"'+ temp_class.name+'","group": ' + str(group) + ',"subclass": ' + str(is_subclass) + ' }\n')
    else:
        json_file.write('{"name":"'+temp_class.name+'","group":' + str(group) + ',"subclass": ' + str(is_subclass) + ' },\n')

json_file.write('],\n"links":[\n')


for i in range(0, len(links)):
    l = links[i]

    if i == len(links)-1:
        json_file.write('{"source":' + str(links[i][0]) + ',"target":' + str(links[i][1]) + ',"value":' + str(links[i][2]) + ' }\n')
    else:
        json_file.write('{"source":' + str(links[i][0]) + ',"target":' + str(links[i][1]) + ',"value":' + str(links[i][2]) + ' },\n')

json_file.write(']}')

#
#
# write xml file
xml_file.write('<classes>\n')
for c in class_collection.classes:
    # print class informations
    xml_file.write('\t<class name="' + c.name + '" size="' + str(c.size) +
                   '" external="' + str(c.external) + '" file="' + c.file + '" line="' + c.line + '">\n')
    # print class superclasses
    xml_file.write('\t<superclasses>\n')
    for s in c.superclasses:
        xml_file.write('\t\t<superclass name="' + s.name + '"/>\n')
    xml_file.write('\t</superclasses>\n')
    # print class instances
    xml_file.write('\t<instances>\n')
    for i in c.instances:
        xml_file.write('\t\t<instance name="' + i.class_instantiated.name + '" file="' + i.file_name +
                       '" line="' + i.code_line + '"/>\n')
    xml_file.write('\t</instances>\n')
    xml_file.write('\t</class>\n')
xml_file.write('</classes>')


#
#
#
# print in the console for a quick feedback

print "\nclasses\n"

for c in class_collection.classes:
    if c.external:
        print c.name + " - EXTERNAL "
    else:
        print c.name + " size: " + str(c.size) + " - at line " + str(c.line) + " in " + c.file

    if c.is_superclass:
        print "is superclass"
    if len(c.superclasses) > 0:
        print " super classes: "
        for s in c.superclasses:
            print " " + s.name
    if len(c.instances) > 0:
        print " instances: "
        for i in c.instances:
            print " " + i.class_instantiated.name + " type: " + i.call_type + " - at line " + i.code_line + " in " + i.file_name