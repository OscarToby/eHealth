import hl7, pprint

# pprint.pprint(msg)

hl7_file = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Final-Delta-CHW\\ORU-HL7.txt"
output_hl7_file = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Final-Delta-CHW\\ORU-HL7-Output.txt"
siemens_hl7 = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Final-Delta-CHW\\Siemens_Reports.txt"
siemens_hl7_output = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Final-Delta-CHW\\Siemens_Reports_Output.txt"

def remove_special_characters(hl7):
    hl7 = hl7.replace('\n','\r')
    hl7 = hl7.replace('\X0D', '')
    hl7 = hl7.replace('\X0A', '\n')
    hl7 = hl7.replace('\\', '')
    return hl7

# with open(hl7_file, 'r') as f:
#     contents = f.read()

# contents = remove_special_characters(contents)
# hl7_msgs = hl7.parse(contents)
# bulk_msgs = []
# OBR_field = 5

# for msg in hl7_msgs:
#     if msg[0] == ['OBX']:
#         bulk_msgs.append(msg[5])

# with open(output_hl7_file, 'w') as output:
#     for msg in bulk_msgs:
#         msg = str(msg)
#         msg = msg.strip()
#         output.write(msg)

with open(siemens_hl7, 'r') as r:
    siemens_contents = r.read()

siemens_contents = siemens_contents.replace('"','')

with open(siemens_hl7_output, 'w') as siemens_r:
    siemens_r.write(siemens_contents)