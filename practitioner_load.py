class RowPractitioners:

    def __init__(self,input_row: str):

        self.last_name = input_row[0:30].strip()
        self.first_name = input_row[30:50].strip()
        self.middle_name = input_row[50:70].strip()
        self.identifier_value = input_row[70:78]
        self.address_line_1 = input_row[78:105].strip()
        self.address_line_2 = input_row[105:129].strip()
        self.address_line_3 = input_row[129:145].strip()
        self.postcode = input_row[145:149]
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

    def write_row(self):
        pass

    # def split_row():
    # practitioner_code,
    # expiry_date, 
    # title, 
    # first_name, 
    # surname, 
    # phone, 
    # email, 
    # specialties, 
    # invoicing, 
    # reporting_provider, 
    # associated_domain_user, 
    # is_contracted

row = RowPractitioners("AARON                         HAROLD              NEHEMIAH            0467331XLEFT PRACTICE              19 KALLAROO RD          1995279         2066NSW02115000000000000019881262006070000000000000000000000000000019772162011273DR  C")
print(row.last_name)
print(row.first_name)
print(row.middle_name)
print(row.identifier_value)
print(row.address_line_1)
print(row.address_line_2)
print(row.address_line_3)
print(row.postcode)
print(row.state)
print(row.practitioner_specialties)
print(row.title)