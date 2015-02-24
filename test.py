json_file.write('{"nodes":[\n')
log.write('\nClass found: ' + str(len(class_list)) + '\n')

for i in range(0, len(class_list)):
    log.write('\t' + class_list[i] + '\n')
    if class_list[i] in fundamental_types:
        group = '3'
    else:
        group = '1'

    if i == len(class_list)-1:
        json_file.write('{"name":"'+class_list[i]+'","group":' + group + '}\n')
    else:
        json_file.write('{"name":"'+class_list[i]+'","group":' + group + '},\n')
    if class_list[i] not in class_dictionary:
        class_dictionary[class_list[i]] = i

json_file.write('],\n"links":[\n')

for i in range(0, len(links)):
    l = links[i]

    if i == len(links)-1:
        json_file.write('{"source":' + str(class_dictionary[l.source]) + ',"target":' + str(class_dictionary[l.target]) + ',"value": ' + str(l.linktype) + ' }\n')
    else:
        json_file.write('{"source":' + str(class_dictionary[l.source]) + ',"target":' + str(class_dictionary[l.target]) + ',"value": ' + str(l.linktype) + ' },\n')
json_file.write(']}')