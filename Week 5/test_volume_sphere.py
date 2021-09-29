

from volume_sphere import volume_of_sphere
from pytest import approx
import pytest

def test_volume_of_sphere():
    assert volume_of_sphere(4) == approx(268.0825731)
    assert volume_of_sphere(10) == approx(4188.790205)
    assert volume_of_sphere(-2) == approx(-33.51032164)

pytest.main(["-v", "--tb=line", "-rN", "test_volume_sphere.py"])