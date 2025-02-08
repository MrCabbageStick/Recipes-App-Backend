from pathlib import Path
from database.manager import DatabaseManager
from fastapi import FastAPI

app = FastAPI()
db = DatabaseManager(Path("./data/recipes.sqlite3"))

@app.get("/all_recipes")
async def get_all_recipes(country_code: str):
    return db.getAllRecipesShort(country_code)

def main():
    ...


if __name__ == "__main__":
    main()
