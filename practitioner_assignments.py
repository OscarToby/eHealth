def get_referrers(referrers_extract: str) -> set:
    with open(referrers_extract, 'r') as file_e:
        referrers_set = set()
        count = 0
        for line in file_e:
            count += 1
            if count == 1:
                continue
            referrers_set.add(line[:8])
    return referrers_set

def process_referrer_assignment_file(assignments_for_Kestral: str, new_file: str, referrers_set: set):
    with open(assignments_for_Kestral, 'r') as file_r, \
    open(new_file, 'w') as file_n:
        count = 0
        for line in file_r:
            if count == 0:
                file_n.write(line)
            if line[26:34] in referrers_set:
                file_n.write(line)
            count += 1


referrers_extract = "referrers.csv"
assignments_for_Kestral = "Assignment_for_Kestral_202212062055.csv"
new_file = "referrers_5k.csv"

referrers_set = get_referrers(referrers_extract)
print(len(referrers_set))
#process_referrer_assignment_file(assignments_for_Kestral, new_file, referrers_set)

