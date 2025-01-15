from pathlib import Path
import sqlite3
from .query_classes import IngredientGroup

class DatabaseManager:
    db_path: Path

    def __init__(self, db_path: Path):
        self.db_path = db_path

    def _connect(self):
        return sqlite3.connect(self.db_path)

    # Helper method to execute a query
    def _execute(self, query: str, params: tuple[any, ...] = ()):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor
        

    def test(self):
        curr = self._execute(*IngredientGroup.ingredientGroups("pl", 1))
        return [IngredientGroup(*row) for row in curr.fetchall()]