from typing import Dict, List

from pydantic import BaseModel


class Compound(BaseModel):
    name: str


class Nutrient(BaseModel):
    name: str
    compound: str


class Food(BaseModel):
    name: str
    nutrients: List[Nutrient]

    def wow(self) -> str:
        return self.name.upper()


class Country(BaseModel):
    code: int
    name: str
    # food dict should be food_name : Food object
    # ex: wheat: Food()
    foods: Dict[str, Food]


c = Country(
    code=1,
    name="USA",
    foods=dict(
        wheat=Food(name="wheat", nutrients=[Nutrient(name="B12", compound="niaocin")]),
        oil=Food(name="oil", nutrients=[Nutrient(name="weird", compound="")]),
    ),
)

print(f"Name: {c.name}", "---", c.foods["wheat"].nutrients)
print(c.foods["wheat"].wow())