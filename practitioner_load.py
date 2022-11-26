class RowPractitioners:

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
            self.identifier_value[0:-2],
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

    def write_row_practitioner_location(self):
        return ','.join([
            self.practitioner_location_code,
            f'{self.address_line_1} {self.address_line_2} {self.suburb}', # name
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

    def write_row_practitioner_assignment(self):
        return ','.join([
            self.identifier_value[0:-2],
            'Provider_Number', # assignment type code
            self.practitioner_location_code[7:],
            self.identifier_value,
            'N', # default assignment
            '', # start date
            '', # end date
            'N', # print group
            'N', # fax group
            'N', # hl7 group
        ])

def process_file(file_location: str): 
    with open(file_location, 'r') as file:
        print(RowPractitioners.write_row_practitioner_header())
        i = 0
        for line in file:
            row = RowPractitioners(line)
            i += 1
            if row.address_line_1 == 'LEFT PRACTICE':
                continue
            if i == 500:
                break
            # if row.identifier_value == '2084955H':
            #     print(row.practitioner_location_code)
            print(row.write_row_practitioner())

NSW_FILE = "C:\\Users\\60035675\\NSW Health Department\\RIS-PACS Program - MS Teams - SCHN Project\\04. Build, Configuration & KRD\\08 Providers\\Medicare NSWFILE\\NSWFILE 20221127\\NSWFILE_Nov.txt"

process_file(NSW_FILE)

# row = RowPractitioners("ABDEL-MEGEED                  ESAM                                    0070612L18 WOODVALE PL             CASTLE HILL                             2154NSW10454000000000000019760402021167000000000000000000000000000019751822010181DR   ")
# print(f'Last_name is {row.last_name}')
# print(f'First_name is {row.first_name}')
# print(f'Middle_name is {row.middle_name}')
# print(f'Identifier value is {row.identifier_value}')
# print(f'Address_line_1 is {row.address_line_1}')
# print(f'Address_line_2 is {row.address_line_2}')
# print(f'Suburb is {row.suburb}')
# print(f'Postcode is {row.postcode}')
# print(f'State is {row.state}')
# print(f'Practitioner_specialties is {row.practitioner_specialties}')
# print(f'Title is {row.title}')