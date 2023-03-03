import csv

referrers_extract = "Referrers.csv"
full_practitioner_list = "Practitioners from Karisma.csv"

referrers_set = set()
with open(referrers_extract, 'r') as re:
    reader = csv.reader(re, delimiter=',')
    for row in reader:
        referrers_set.add(row[0][:6])
        referrers_set.add(row[1][:6])

referrers_excluded_from_5k = 'dirty_practitioners.txt'

original_referrers_set = set()
with open(full_practitioner_list, 'r') as file_p:
    reader1 = csv.reader(file_p, delimiter=',')
    for row in reader1:
        original_referrers_set.add(row[0])

referrers_to_keep = set(referrers_set).intersection(original_referrers_set)

referrers_exlusion = set(referrers_set).difference(referrers_to_keep)

with open(referrers_excluded_from_5k, 'w') as exlusion:
    for referrer in referrers_exlusion:
        exlusion.write(referrer+'\n')

# with open('clean_practitioners.txt', 'w') as cp:
#     for referrers in referrers_to_keep:
#         cp.write(referrers+'\n')

# with open("practitioners_to_be_kept_v2.csv", 'w') as file_w:
#     for referrer in referrers_set:
#         file_w.write(referrer+'\n')

# def get_referrers_5k(referrers_extract_siemens: str) -> set:
#     with open(referrers_extract_siemens, 'r') as file_e:
#         referrers_set = set()
#         count = 0
#         for line in file_e:
#             count += 1
#             if count == 1:
#                 continue
#             referrers_set.add(line[:6])
#             referrers_set.add(line[10:16])
#     return referrers_set


# def write_practitioner_file(practitioners_to_keep, referrers_set):
#     with open(practitioners_to_keep, 'w') as file_w:
#         for referrer in referrers_set:
#             file_w.write(referrer+'\n')



practitioners_to_keep = "Practitioners_to_be_kept.csv"
# referrers_set = get_referrers_5k(referrers_extract)
# write_practitioner_file(practitioners_to_keep, referrers_set)

# referrers_set = get_referrers_5k(referrers_extract)
# print(len(referrers_set))