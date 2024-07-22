This repository demonstrates how deserialization vulnerabilities can be exploited in Python to execute arbitrary code. It includes an example of serializing a malicious object and deserializing it to execute a script.

## Description
This script demonstrates how malicious code can be embedded within a numpy data structure and executed upon loading. It is intended to educate about security risks associated with deserialization and the use of exec and eval functions.

## Usage

### example.py

This script implements a simple Snake game, which is safe to run.

#### serialization_and_save.py

This script creates a `Malicious` object containing the contents of `example.py`, then serializes and saves it using `numpy`. This object can be disguised as a normal .npz or .npy file.

### load_npy.py

This script loads the serialized object from `malicious.np`, demonstrating the deserialization vulnerability by executing the code in `example.py`.

**Warning**: This script will execute the code contained in `example.py` upon loading the serialized object. Only run this if you understand the security implications.

```
python load_npy.py
```



## Explanation

### Deserialization Vulnerability

Deserialization vulnerabilities occur when an application deserializes data from untrusted sources, potentially leading to arbitrary code execution. In this example, the `Malicious` class reads the content of `example.py` and uses the `__reduce__` method to execute this content upon deserialization.

### Mitigation and Best Practices

To protect against such vulnerabilities:

- Avoid deserializing data from untrusted sources.
- Use safer serialization formats like JSON.
- Validate and sanitize input data before deserializing.
- Limit the use of `pickle` and understand its risks, by setting allow_pickle=False.

## Disclaimer

This repository is for educational purposes only. The techniques demonstrated here can be dangerous if misused. Do not run the provided scripts on production systems or with data you do not trust.

## License

This code is licensed under the [MIT License](LICENSE) and is provided for educational purposes only. Use at your own risk.

## Files

1. **example.py**: A simple Snake game.
2. **serialization_and_save.py**: Script to serialize and save a malicious object.
3. **load_npy.py**: Script to load the serialized object, demonstrating the deserialization vulnerability.





