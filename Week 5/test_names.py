from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Stewart", "Rowley") == "Rowley; Stewart"
    assert make_full_name("Emily", "Rowley") == "Rowley; Emily"

def test_extract_given_name():
    assert extract_given_name("Rowley; Stewart") == "Stewart"
    assert extract_given_name("Rowley; Emily") == "Emily"

def test_extract_family_name():
    assert extract_family_name("Rowley; Stewart") == "Rowley"
    assert extract_family_name("Rowley; Emily") == "Rowley"

# def test_extract_family_name(") == "Rowley"
    
    
    



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])