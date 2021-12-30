import hashlib
import os
import pytest


@pytest.mark.parametrize(
    "a,b",
    [
        ("CODE_OF_CONDUCT", "docs/source/code_of_conduct.rst"),
        ("CONTRIBUTING", "docs/source/contributing.rst"),
    ],
)
def test_files_are_identical(a, b):
    def hash(filename):
        with open(filename, "rb") as f:
            bytes = f.read()  # read entire file as bytes
            return hashlib.sha256(bytes).hexdigest()

    assert hash(a) == hash(b)
