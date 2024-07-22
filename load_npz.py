import numpy as np


def main():
    # when set all_pickle equal to True, numpy is able to call user defined object
    data = np.load('malicious.npz', allow_pickle=True) 
    print("This is normal data")
    print(data["normal_data"])
    input("press enter to continue")

    print("This is malicious data, the code in the example.py will be executed.")
    print("The malicious data can be called as normal data")
    print(data["malicious_data_pyscript"])
    input("press enter to continue")

    print("This another malicious data, the code in the example.exe will be executed.")
    print("The malicious data can also be called as normal data")
    print(data["malicious_data_exe"])

if __name__=="__main__":
    main()
