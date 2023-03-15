import os

hermes_sample_folders = []

AW = "N:\\DATA\\SGHNM\\Hermes_Sample\\AW\\48.P\\tmp"
BrightView = "N:\\DATA\\SGHNM\\Hermes_Sample\\BrightView\\31.P\\tmp"
Ecam = "N:\\DATA\\SGHNM\\Hermes_Sample\\Ecam\\56.P\\tmp"
GEXsuite = "N:\\DATA\\SGHNM\\Hermes_Sample\\GEXsuite\\54.P\\tmp"
MilleniumMG1 = "N:\\DATA\\SGHNM\\Hermes_Sample\\MilleniumMG\\1\\tmp"
MilleniumMG2 = "N:\\DATA\\SGHNM\\Hermes_Sample\\MilleniumMG\\2\\tmp"
MilleniumMG3 = "N:\\DATA\\SGHNM\\Hermes_Sample\\MilleniumMG\\3\\tmp"
Symbia = "N:\\DATA\\SGHNM\\Hermes_Sample\\Symbia\\8.P\\tmp"

hermes_sample_folders.extend([AW, BrightView, Ecam, GEXsuite, MilleniumMG1, MilleniumMG2, MilleniumMG3, Symbia])
# suids = os.listdir(Symbia)
suids_list = []
status_id = 30

for folder in hermes_sample_folders:
    suids_list.append(os.listdir(folder))

flat_suids = []
for suids in suids_list:
    for suid in suids:
        flat_suids.append(suid)
    
# for suid in flat_suids:
#     sql = f"INSERT INTO OMNI.Omni.sgh_nm (studyuid, status) VALUES ('{suid}', {status_id})"
#     print(sql)
print(len(flat_suids))