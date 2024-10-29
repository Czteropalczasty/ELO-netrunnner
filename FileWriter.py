class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'w') as file:
            pass  # This will clear the file

    def write(self, line, new_line=False):
        with open(self.file_path, 'a') as file:  # Open file in append mode
            file.write(line)  # Append the line followed by a newline
            if new_line:
                file.write("<br>\n")
            else:
                file.write("\n")