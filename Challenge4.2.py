# API:
# open_file(file_name) -> file_pointer
# read_data(file_pointer) -> data
# write_data(file_pointer, data)
# close_file(file_pointer)

class File:
    def __init__(self, pointer):
        self.pointer = pointer

    def open(self):
        try: 
            open_file(self.pointer)
        except:
            print("could not open file")


    def read(self):
        try: 
            read_data(self.pointer)
        except:
            print("could not read file")

    def write(self):
        try: 
            write_data(self.pointer)
        except:
            print("could not write to file")

    def close(self):
        try: 
            close_file(self.pointer)
        except:
            print("could not close file")

