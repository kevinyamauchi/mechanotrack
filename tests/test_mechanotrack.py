import mechanotrack


def test_imports_with_version():
    assert isinstance(mechanotrack.__version__, str)
