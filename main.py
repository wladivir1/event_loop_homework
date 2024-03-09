import asyncio
import datetime

import aiohttp

from models import SwapiPeople, init_db
from configDB import engine, Session



async def link(session, url):
        response = await session.get(url)
        return await response.json()
        

async def links_all(session, urls):
    return await asyncio.gather(*(link(session, url) for url in urls))
    
async def homeworld_get(url):
    async with aiohttp.ClientSession() as session:
        result = await link(session, url)

        return result.get("name")
 
async def films_get(list_urls):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(link(session, url) for url in list_urls))

    return ", ".join(result["title"] for result in results)

async def list_name_get(list_urls):
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(link(session, url) for url in list_urls))

    return ", ".join(result["name"] for result in results)

async def insert_db(list_person):
    models = []
    async with Session() as session:     
        for list_json in list_person:
            model = SwapiPeople(
                        name=list_json["name"],
                        height=list_json["height"],
                        mass=list_json["mass"],
                        hair_color=list_json["hair_color"],
                        skin_color=list_json["skin_color"],
                        eye_color=list_json["eye_color"],
                        birth_year=list_json["birth_year"],
                        gender=list_json["gender"],
                        homeworld=await homeworld_get(list_json["homeworld"]),
                        films=await films_get(list_json["films"]),
                        species=await list_name_get(list_json["species"]),
                        vehicles=await list_name_get(list_json["vehicles"]),
                        starships=await list_name_get(list_json["starships"]),
                    ) 
            
                
            models.append(model)
           
        session.add_all(models)
        await session.commit() 
    
async def main():
    await init_db()
    session = aiohttp.ClientSession()
    url = [f"https://swapi.py4e.com/api/people/?page={i}" for i in range(1, 10)]
    person = await links_all(session, url)
    list_json = [p for page in person for p in page["results"]]
    
    await insert_db(list_json)
    await session.close()
    await engine.dispose()
    
if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main())
    print(datetime.datetime.now() - start)