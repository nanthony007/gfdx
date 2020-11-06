import pprint
from typing import List

from pydantic import BaseModel


class Compound(BaseModel):
    name: str


class Nutrient(BaseModel):
    name: str
    compounds: List[Compound] = list()
    recommendation_status: str = ""


class Food(BaseModel):
    name: str
    nutrients: List[Nutrient] = list()

    def wow(self) -> str:
        return self.name.upper()


class Country(BaseModel):
    code: int
    name: str = "default"
    # food dict should be food_name : Food object
    # ex: wheat: Food()
    foods: List[Food] = list()


c = Country(
    code=1,
    name="USA",
    foods=[
        Food(
            name="wheat",
            intake=12,
            nutrients=[Nutrient(name="B12", compound="niaocin")],
        ),
        Food(name="oil", intake=1.15, nutrients=[Nutrient(name="weird", compound="")]),
    ],
)


printer = pprint.PrettyPrinter(indent=2)
printer.pprint(c.dict())
