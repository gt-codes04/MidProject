from app.calculation import CalculationFactory
import pytest

def test_factory_add():
    c = CalculationFactory.create("add",5,7)
    assert c.get_result()==12

def test_factory_invalid():
    with pytest.raises(Exception):
        CalculationFactory.create("nope",1,2)
