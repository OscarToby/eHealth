ORU_File = "C:\\IS Migration Split Files\\Original_Zipped_Files\\Bulk-G\\Bulk-ORU.hl7"

special_char_counts = {"\x07": 0, "\x08": 0, "\x0C": 0, "\x0B": 0}

new_special_char_counts = {"\x07": 0, "\x08": 0, "\x0C": 0, "\x0B": 0}

# Open the file for reading
with open(ORU_File, 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Loop through each character in the line
        for char in line:
            # Check if the character is one of the special characters
            if char in special_char_counts:
                # If so, increment the count for that special character
                special_char_counts[char] += 1

for char, count in special_char_counts.items():
    print(F"Found {count} occurences of special character '{char}'.")

oru_file_special_characters_removed = "C:\\IS Migration Split Files\\Original_Zipped_Files\\Bulk-G\\Bulk-ORU_new.hl7"

# Open the file for reading
with open(ORU_File, 'r') as file:
    # Read the file into a string and replace the special characters with an empty string
    file_content = file.read()
    for char in special_char_counts:
        file_content = file_content.replace(char, "")

# Open the file for writing and write the modified string back to the file
with open(oru_file_special_characters_removed, 'w+') as file:
    file.write(file_content)

    # Loop through each line in the file
    for line in file:
        # Loop through each character in the line
        for char in line:
            # Check if the character is one of the special characters
            if char in new_special_char_counts:
                # If so, increment the count for that special character
                new_special_char_counts[char] += 1

# Print the counts for each special character
for char, count in new_special_char_counts.items():
    print(f"Found {count} occurrences of special character '{char}'.")
