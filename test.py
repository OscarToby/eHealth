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