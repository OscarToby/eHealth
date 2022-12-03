practitioners = "practitioners.csv"
karisma_practitioners = "practitioners from Karisma.csv"
no_dup_file = "Test_load.csv"


# with open(practitioners, 'r') as file_p, \
# open(karisma_practitioners, 'r') as file_k, \
# open(no_dup_file, 'w') as file_d:
#     file_p_lines = file_p.readlines()
#     dict_p = zip(file_p_lines[:6], file_p_lines[6:])
#     print([i for i in dict_p])

# def compare_practitioners(practitioners, karisma_practitioners, no_dup_file: str):
#     with open(practitioners, 'r') as file_p, \
#     open(karisma_practitioners, 'r') as file_k, \
#     open(no_dup_file, 'w') as file_d:
#         file_p_lines = file_p.readlines()
#         file_k_lines = file_k.readlines()
#         for i in range(len(file_k_lines)):
#             if file_p_lines[i][:6] != file_k_lines[i][:6]:
#                 file_d.write(file_p_lines[i])

# compare_practitioners(Practitioner_File, Karisma_File, New_Practitioners)

def new_practitioners(practitioners, karisma_practitioners, no_dup_file):
    with open(practitioners, 'r') as file_p, \
    open(karisma_practitioners, 'r') as file_k, \
    open(no_dup_file, 'w') as file_d:
        file_p_lines = file_p.readlines()
        file_k_lines = file_k.readlines()
        practitioners_p_set = set()
        practitioners_k_set = set()
        for line in file_p_lines:
            practitioners_p_set.add(line[:6])
        for line in file_k_lines:
            practitioners_k_set.add(line[:6])
        new_practitioners = practitioners_p_set.symmetric_difference(practitioners_k_set)
        for prac in new_practitioners:
            file_d.write(prac+'\n')


new_practitioners(practitioners, karisma_practitioners, no_dup_file)

# def process_practitioner_file(HIC_file, new_file, karisma_practitioners, new_practitioners: str): 
#     with open(HIC_file, 'r') as file_r, \
#     open(new_file, 'r+') as file_n, \
#     open(karisma_practitioners, 'r') as file_k, \
#     open(new_practitioners, 'w') as file_d:
#         file_n.write(RowHICFile.write_row_practitioner_header()+'\n')
#         previous_practitioner_code = ''
#         for line in file_r:
#             row = RowHICFile(line)
#             if row.address_line_1 == 'LEFT PRACTICE':
#                 continue
#             if previous_practitioner_code == row.identifier_value[:-2]:
#                 continue
#             file_n.write(row.write_row_practitioner()+'\n')
#             previous_practitioner_code = row.identifier_value[:-2]
#         file_n_lines = file_n.readlines()
#         file_k_lines = file_k.readlines()
#         practitioners_n_set = set()
#         practitioners_k_set = set()
#         for line in file_n_lines:
#             practitioners_n_set.add(line[:6])
#         for line in file_k_lines:
#             practitioners_k_set.add(line[:6])
#         new_practitioners = practitioners_n_set.symmetric_difference(practitioners_k_set)
#         file_d.write(RowHICFile.write_row_practitioner_header()+'\n')
#         previous_practitioner_code = ''
#         for line in file_r:
#             row = RowHICFile(line)
#             if row.address_line_1 == 'LEFT PRACTICE':
#                 continue
#             if previous_practitioner_code == row.identifier_value[:-2]:
#                 continue
#             if row.identifier_value[:-2] not in new_practitioners:
#                 continue
#             file_d.write(row.write_row_practitioner()+'\n')
#             previous_practitioner_code = row.identifier_value[:-2]
