from pathlib import Path
from database.manager import DatabaseManager

def main():
    db = DatabaseManager(Path("./data/recipes.sqlite3"))
    print(db.test())


if __name__ == "__main__":
    main()
