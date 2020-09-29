from gfdx.containers import structures


def test_compound() -> None:
    compound = structures.Compound(name="B12")
    assert compound.name == "B12"
