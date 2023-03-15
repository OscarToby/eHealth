import hl7, pprint

test_file = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Final-Delta-CHW\\Sample-HL7.txt"
input_file = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Final-Delta-CHW\\Sample-HL7.txt"
output_file = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Final-Delta-CHW\\Output-Sample-HL7.txt"
ExtractedReport = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Final-Delta-CHW\\ExtractedReport.txt"

with open(test_file, 'r') as f:
    contents = f.read()

contents = contents.replace('\n','\r')

msg = hl7.parse(contents)
#print.pprint(msg)

print(msg[2][25])