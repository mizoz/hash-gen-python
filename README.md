# Hash Generator Python

[![PyPI Version](https://img.shields.io/pypi/v/hash-gen-python?style=flat-square)](https://pypi.org/project/hash-gen-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/hash-gen-python?style=flat-square)](https://pypi.org/project/hash-gen-python/)
[![License](https://img.shields.io/pypi/l/hash-gen-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/hash-gen-python?style=flat-square)](https://pypi.org/project/hash-gen-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/hash-gen-python?style=flat-square)](https://github.com/mizoz/hash-gen-python)

> A Python CLI tool for generating cryptographic hashes (MD5, SHA1, SHA256, SHA512).

## Features

- Generate MD5 hashes
- Generate SHA1 hashes
- Generate SHA256 hashes
- Generate SHA512 hashes
- File hashing support
- Python API for integration

## Installation

### From PyPI

```bash
pip install hash-gen-python
```

### From Source

```bash
git clone https://github.com/mizoz/hash-gen-python.git
cd hash-gen-python
pip install -e .
```

## Usage

### Command Line

```bash
# Generate SHA256 hash
hash-gen "Hello World"

# Generate MD5 hash
hash-gen --algo md5 "Hello World"

# Hash a file
hash-gen --file myfile.txt
```

### Python API

```python
from hash_gen import HashGenerator

gen = HashGenerator()

# Generate hash
hash_value = gen.sha256("Hello World")
print(hash_value)
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-a, --algo` | Hash algorithm (md5, sha1, sha256, sha512) |
| `-f, --file` | Hash a file |

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
