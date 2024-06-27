import fastapi as fapi
import pydantic as pyd


class Fact(pyd.BaseModel):
    id: int
    fact: str


facts = [
    Fact(id=0, fact='All computer data can ultimately be broken down to 1s and 0s.'),
    Fact(id=1, fact='The moon landing was not fake.'),
    Fact(id=2, fact='Vaccines work.'),
    Fact(id=3, fact='The greatest genre of music is gangster rap.')
]

app = fapi.FastAPI()


@app.get('/fact')
async def get_all():
    return facts


@app.get('/fact/{id}')
async def get_by_id(id: int):
    return facts[id]


@app.post('/fact')
async def add(fact: str):
    new_fact = Fact(id=len(facts), fact=fact)
    facts.append(new_fact)
    return new_fact
