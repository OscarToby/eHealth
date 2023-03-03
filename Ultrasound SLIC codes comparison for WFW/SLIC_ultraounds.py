import pandas as pd

WFW_Ultrasound_Codes = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Ultrasound SLIC codes comparison for WFW\\CDN_US_codes.xlsx"
SLIC_Ultrasound_Codes = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Ultrasound SLIC codes comparison for WFW\\US SLIC codes.xlsx"

df_WFW = pd.read_excel(WFW_Ultrasound_Codes)
existing_ultrasound_codes = df_WFW['SLIC_CODE'].tolist()

df_SLIC = pd.read_excel(SLIC_Ultrasound_Codes)
new_ultrasound_codes = df_SLIC['Service Type Code_(M)'].tolist()

set_existing_codes = set(existing_ultrasound_codes)
set_new_codes = set(new_ultrasound_codes)

unused_codes = set_existing_codes.symmetric_difference(set_new_codes)
print(len(unused_codes))

# unused_codes_text = "C:\\Users\\60035675\\Desktop\\PythonCourse\\eHealth\\Ultrasound SLIC codes comparison for WFW\\unused_codes_text.txt"
# with open(unused_codes_text, 'w') as document:
#     for code in unused_codes:
#         document.write(f'{code} \n')
