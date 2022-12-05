EXCLUDED_SPECIALTIES = ('', '207', '208', '209', '668', '670', '671', '672')

class RowHICFile:

    def __init__(self,input_row: str):

        self.last_name = input_row[0:30].strip()
        self.first_name = input_row[30:50].strip().capitalize()
        self.middle_name = input_row[50:70].strip().capitalize()
        self.identifier_value = input_row[70:78]
        self.practitioner_code = self.identifier_value[:6]
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
    def get_row_practitioner_header():
        return ','.join([
            'Practitioner Code',
            'Expiry Date',
            'Title',
            'First Name',
            'Surname',
            'Phone',
            'Email',
            'Specialities',
            'Invoicing Level',
            'Reporting Provider',
            'Associated Domain User',
            'Is Contracted'
        ])

    def get_row_practitioner(self):
        specialty = ','.join([str(int(s)) for s in self.practitioner_specialties.split(',') if s not in EXCLUDED_SPECIALTIES])
        return ','.join([
            self.identifier_value[:-2],
            '', # expiry date
            self.title,
            f'{self.first_name} {self.middle_name}',
            self.last_name,
            '', # phone
            '', # email
            f'"{specialty}"',
            'NONE', # invoicing
            'N', # reporting provider
            '', # associated domain user
            'N', # is contracted
        ])
    
    def has_valid_specialties(self):
        if self.practitioner_specialties == '':
            return False
        if any([s for s in self.practitioner_specialties.split(',') if s not in EXCLUDED_SPECIALTIES]):
            return True
        return False

    @staticmethod
    def get_row_practitioner_location_header():
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

    def get_row_practitioner_location(self):
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
    def get_row_practitioner_assignment_header():
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

    def get_row_practitioner_assignment(self, is_default: bool):
        return ','.join([
            self.identifier_value[0:-2],
            'Provider_Number', # assignment type code
            self.practitioner_location_code[7:], # location code
            self.identifier_value,
            'Y' if is_default else 'N', # default assignment
            '', # start date
            '', # end date
            'N', # print group
            'N', # fax group
            'N', # hl7 group
        ])


def get_Karisma_practitioners(Karisma_practitioners_extract: str) -> set:
    with open(Karisma_practitioners_extract, 'r') as file_e:
        existing_practitioners_set = set()
        count = 0
        for line in file_e:
            count += 1
            if count == 1:
                continue
            existing_practitioners_set.add(line[:6])
    return existing_practitioners_set


def process_practitioner_file(HIC_file: str, new_file: str, karisma_practitioners: set): 
    with open(HIC_file, 'r') as file_r, \
    open(new_file, 'w') as file_n:
        file_n.write(RowHICFile.get_row_practitioner_header()+'\n')
        previous_practitioner_codes = set()
        for line in file_r:
            row = RowHICFile(line)
            if row.address_line_1 == 'LEFT PRACTICE':
                continue
            if row.practitioner_code in previous_practitioner_codes:
                continue
            if not row.has_valid_specialties():
                continue
            if row.practitioner_code in karisma_practitioners:
                continue
            file_n.write(row.get_row_practitioner()+'\n')
            previous_practitioner_codes.add(row.practitioner_code)


def get_Karisma_practitioner_locations(Karisma_practitioner_locations_extract: str) -> set:
    with open(Karisma_practitioner_locations_extract, 'r') as file_e:
        existing_practitioner_locations_set = set()
        count = 0
        for line in file_e:
            count += 1
            if count == 1:
                continue
            existing_practitioner_locations_set.add(line[:8])
        return existing_practitioner_locations_set
            

# Need access to data warehouse to get existing identifier values, exlude them and import the rest
def process_practitioner_location_file(HIC_file: str, new_file: str, karisma_practitioner_locations: set):
    with open(HIC_file, 'r') as file_r, \
    open(new_file, 'w') as file_w:
        file_w.write(RowHICFile.get_row_practitioner_location_header()+'\n')
        for line in file_r:
            row = RowHICFile(line)
            if row.address_line_1 == 'LEFT PRACTICE':
                continue
            if row.practitioner_code in karisma_practitioner_locations:
                continue
            file_w.write(row.get_row_practitioner_location()+'\n')


def process_practitioner_assignment_file(HIC_file: str, new_file: str):
    with open(HIC_file, 'r') as file_r, \
    open(new_file, 'w') as file_w:
        file_w.write(RowHICFile.get_row_practitioner_assignment_header()+'\n')
        default_location_assigned = set()
        for line in file_r:
            row = RowHICFile(line)
            if row.address_line_1 == 'LEFT PRACTICE':
                continue
            file_w.write(row.get_row_practitioner_assignment(row.practitioner_code not in default_location_assigned)+'\n')
            default_location_assigned.add(row.practitioner_code)


NSW_FILE = "C:\\Users\\60035675\\NSW Health Department\\RIS-PACS Program - MS Teams - SCHN Project\\04. Build, Configuration & KRD\\08 Providers\\Medicare NSWFILE\\NSWFILE 20221127\\NSWFILE_Nov.txt"

Karisma_Practitioners = "Practitioners from Karisma.csv"
New_Practitioners_For_Karisma = "new practitioners.csv"

Karisma_Practitioner_Locations = "practitioner locations from Karisma.csv"
New_Practitioner_Locations_For_Karisma = "New Practitioner Locations.csv"

Karisma_Practitioner_Location_Assignments = "Practitioner Location Assignments From Karisma.csv"
New_Practitioner_Assignments = "New Practitioner Assignments.csv"

# Create new practitioner file to be loaded into Karisma
# existing_practitioners_set = get_Karisma_practitioners(Karisma_Practitioners)
# process_practitioner_file(NSW_FILE, New_Practitioners_For_Karisma, existing_practitioners_set)

# Create new practitioner locations file to be loaded into Karisma
existing_practitioner_location_set = get_Karisma_practitioner_locations(Karisma_Practitioner_Locations)
process_practitioner_location_file(NSW_FILE, New_Practitioner_Locations_For_Karisma, existing_practitioner_location_set)