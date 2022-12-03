class RowHICFile:

    def __init__(self,input_row: str):

        self.last_name = input_row[0:30].strip()
        self.first_name = input_row[30:50].strip().capitalize()
        self.middle_name = input_row[50:70].strip().capitalize()
        self.identifier_value = input_row[70:78]
        self.address_line_1 = input_row[78:105].strip()
        self.address_line_2 = input_row[105:129].strip()
        self.suburb = input_row[129:145].strip()
        if self.suburb.isnumeric():
            self.suburb = ''
        self.postcode = input_row[145:149]
        self.practitioner_location_code = f'{self.identifier_value}_{self.address_line_1}_{self.address_line_2}_{self.suburb}'
        self.practitioner_location_code = (self.practitioner_location_code
            .replace('/','_')
            .replace(' ','_')
            .replace("'",'_')
            .replace('&','AND')
            )
        self.state = input_row[149:152]
        self.practitioner_specialties = input_row[152:170] 
        while self.practitioner_specialties[len(self.practitioner_specialties)-3:] == '000':
            self.practitioner_specialties = self.practitioner_specialties[:len(self.practitioner_specialties)-3]
        v = (len(self.practitioner_specialties) // 3) - 1
        practitioner_specialty_list = list(self.practitioner_specialties)
        for i in range(v):
            practitioner_specialty_list.insert(len(self.practitioner_specialties) - (i + 1) * 3, ',')
        self.practitioner_specialties = "".join(practitioner_specialty_list)
        self.title = input_row[226:230].strip()

    @staticmethod
    def write_row_practitioner_header():
        return ','.join([
            'Practitioner Code',
            'Expiry Date',
            'Title',
            'First Name',
            'Surname',
            'Phone',
            'Email',
            'Specialties',
            'Invoicing',
            'Reporting Provider',
            'Associated Domain User',
            'Is Contracted'
        ])

    def write_row_practitioner(self):
        return ','.join([
            self.identifier_value[:-2],
            '', # expiry date
            self.title,
            f'{self.first_name} {self.middle_name}',
            self.last_name,
            '', # phone
            '', # email
            f'"{self.practitioner_specialties}"',
            'NONE', # invoicing
            'N', # reporting provider
            '', # associated domain user
            'N', # is contracted
        ])

    @staticmethod
    def write_row_practitioner_location_header():
        return ','.join([
            'Practitioner Location Code',
            'Name',
            'Description',
            'Expiry Date',
            'Phone',
            'Fax',
            'Address Line 1',
            'Address Line 2',
            'Address Line 3',
            'Suburb',
            'Postcode',
            'Country',
            'Email'
        ])

    def write_row_practitioner_location(self):
        return ','.join([
            self.practitioner_location_code,
            f'{self.address_line_1.title()} {self.address_line_2.title()} {self.suburb.title()}', # name
            f'{self.address_line_1} {self.address_line_2} {self.suburb}', # description
            '', # expiry date
            '', # phone
            '', # fax
            self.address_line_1,
            self.address_line_2,
            '', # address line 3
            self.suburb,
            self.postcode,
            'Australia', # country
            '', # email
        ])

    @staticmethod
    def write_row_practitioner_assignment_header():
        return ','.join([
            'Practitioner Code',
            'Assignment Type Code',
            'Location Code',
            'Identifier Value',
            'Is Default Assignment',
            'Start Date',
            'End Date',
            'Print Group Member',
            'Fax Group Member',
            'HL7 Group Member',
        ])

    def write_row_practitioner_assignment(self):
        return ','.join([
            self.identifier_value[0:-2],
            'Provider_Number', # assignment type code
            self.practitioner_location_code[7:], # location code
            self.identifier_value,
            'N', # default assignment
            '', # start date
            '', # end date
            'N', # print group
            'N', # fax group
            'N', # hl7 group
        ])

# def process_file_test(file_location: str): 
#     with open(file_location, 'r') as file:
#         print(RowPractitioners.write_row_practitioner_header())
#         i = 0
#         for line in file:
#             row = RowPractitioners(line)
#             i += 1
#             if row.address_line_1 == 'LEFT PRACTICE':
#                 continue
#             if i == 500:
#                 break
#             # if row.identifier_value == '2084955H':
#             #     print(row.practitioner_location_code)
#             print(row.write_row_practitioner())

def process_practitioner_file(HIC_file, new_file: str): 
    with open(HIC_file, 'r') as file_r, \
    open(new_file, 'w') as file_n:
        file_n.write(RowHICFile.write_row_practitioner_header()+'\n')
        previous_practitioner_code = ''
        for line in file_r:
            row = RowHICFile(line)
            if row.address_line_1 == 'LEFT PRACTICE':
                continue
            if previous_practitioner_code == row.identifier_value[:-2]:
                continue
            file_n.write(row.write_row_practitioner()+'\n')
            previous_practitioner_code = row.identifier_value[:-2]

def new_practitioners(practitioners, karisma_practitioners, import_file: str):
    with open(practitioners, 'r') as file_p, \
    open(karisma_practitioners, 'r') as file_k, \
    open(import_file, 'w') as file_import:
        file_p_lines = file_p.readlines()
        file_k_lines = file_k.readlines()
        practitioners_p_set = set()
        practitioners_k_set = set()
        for line in file_p_lines:
            practitioners_p_set.add(line[:6])
        for line in file_k_lines:
            practitioners_k_set.add(line[:6])
        n_practitioners = practitioners_p_set.symmetric_difference(practitioners_k_set)
        file_import.write(RowHICFile.write_row_practitioner_header()+'\n')
        for line in file_p:
            if line[:6] not in n_practitioners:
                continue
            file_import.write(line)
 

def process_practitioner_location_file(HIC_file, new_file: str):
    with open(HIC_file, 'r') as file_r, \
    open(new_file, 'w') as file_w:
        file_w.write(RowHICFile.write_row_practitioner_location_header()+'\n')
        for line in file_r:
            row = RowHICFile(line)
            if row.address_line_1 == 'LEFT PRACTICE':
                continue
            file_w.write(row.write_row_practitioner_location()+'\n')


def process_practitioner_assignment_file(HIC_file, new_file: str):
    with open(HIC_file, 'r') as file_r, \
    open(new_file, 'w') as file_w:
        file_w.write(RowHICFile.write_row_practitioner_assignment_header()+'\n')
        for line in file_r:
            row = RowHICFile(line)
            if row.address_line_1 == 'LEFT PRACTICE':
                continue
            file_w.write(row.write_row_practitioner_assignment()+'\n')


NSW_FILE = "C:\\Users\\60035675\\NSW Health Department\\RIS-PACS Program - MS Teams - SCHN Project\\04. Build, Configuration & KRD\\08 Providers\\Medicare NSWFILE\\NSWFILE 20221127\\NSWFILE_Nov.txt"

Practitioner_File = "Practitioners.csv"
Practitioner_Location_File = "Practitioner Locations.csv"
Karisma_File = "C:\\Users\\60035675\\Desktop\\Practitioners\\Practitioners from Karisma.csv"
#New_Practitioners = 'New Practitioners.csv'

#process_practitioner_file(NSW_FILE, Practitioner_File)

#process_practitioner_location_file(NSW_FILE, Practitioner_Location_File)

temp_file = 'temporary_file.csv'
karisma_practitioners = "practitioners from Karisma.csv"
import_file = "new practitioners.csv"

#process_practitioner_file(NSW_FILE, temp_file, karisma_practitioners, new_practitioners)

new_practitioners(Practitioner_File, karisma_practitioners, import_file)