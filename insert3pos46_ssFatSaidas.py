# with open("ssFatSaidas_mudado.txt", 'w') as outfile:
#     with open("ssFatSaidas.txt", 'r', encoding='utf-8') as infile:
#         # list_of_lists = []  
#         for line in infile:
#             stripped_line = line.strip()
#             line_list = stripped_line.split("|")
#             final = len(line_list)
#             line_list2="|".join(str(item) for item in range(1, final))
#             outfile.write("%s\n" % line_list2)

with open("ssFatSaidas_mudado.txt", 'w') as outfile:
    with open("ssFatSaidas.txt", 'r', encoding='utf-8') as infile:
        list_of_lists = []  
        for line in infile:
            stripped_line = line.strip()
            line_list = stripped_line.split("|")
            line_list[45]=3   # posição 46
            line_list2="|".join(str(item) for item in line_list)
            outfile.write("%s\n" % line_list2)