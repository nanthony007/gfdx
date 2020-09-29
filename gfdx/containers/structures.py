from typing import Dict, List, Tuple, Union

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


# c = Country(
#     code=1,
#     name="USA",
#     foods=dict(
#         wheat=Food(
#             name="wheat",
#             intake=12,
#             nutrients=[Nutrient(name="B12", compound="niaocin")],
#         ),
#         oil=Food(
#             name="oil", intake=1.15, nutrients=[Nutrient(name="weird", compound="")]
#         ),
#     ),
# )

# print(f"Name: {c.name}", "---", c.foods["wheat"].nutrients)
# print(c.foods["wheat"].wow())