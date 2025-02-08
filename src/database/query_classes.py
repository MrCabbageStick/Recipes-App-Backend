'''
Dataclasses, with queries, representing query fields.
'''

from dataclasses import dataclass

@dataclass
class TranslatedIngredientGroup:
    id: int
    fallback_name: str
    translated_name: str

    @staticmethod
    def ingredientGroups(country_code: str, recipe_id: int) -> tuple[str, tuple[str, int]]:
        return (
            """SELECT
                ingredient_group.id,
                ingredient_group.fallback_name,
                ingredient_group_translation.name
            FROM ingredient_group
            LEFT JOIN
                ingredient_group_translation
                ON ingredient_group_translation.ingredient_group_id = ingredient_group.id
                AND ingredient_group_translation.country_code = ?
            WHERE ingredient_group.recipe_id = ?""",
            (country_code, recipe_id)
        )
    

@dataclass
class TranslatedIngredient:
    id: int
    fallback_name: str
    translated_name: str
    amount: float
    unit: str
    percentage: float
    notes: str

    @staticmethod
    def ingredientGroupIngredients(country_code: str, recipe_id: int) -> tuple[str, tuple[str, int]]:
        return (
            """SELECT 
                recipe_ingredient.ingredient_id,
                ingredient.fallback_name,
                ingredient_translation.name,
                recipe_ingredient.amount,
                unit.symbol,
                recipe_ingredient.percentage,
                recipe_ingredient.notes
            FROM recipe_ingredient
            LEFT JOIN 
                ingredient_translation
                ON ingredient_translation.ingredient_id = recipe_ingredient.ingredient_id
                AND ingredient_translation.country_code = ?
            INNER JOIN 
                ingredient
                ON ingredient.id = recipe_ingredient.ingredient_id
            INNER JOIN
                unit
                ON unit.id = recipe_ingredient.unit_id
            WHERE
                recipe_ingredient.ingredient_group_id = ?""",
            (country_code, recipe_id)
        )

@dataclass
class BareTranslatedIngredient:
    id: int
    fallback_name: str
    translated_name: str

    @staticmethod
    def allRecipeIngredients(country_code: str, recipe_id: int) -> tuple[str, tuple[str, int]]:
        return (
            """SELECT 
                recipe_ingredient.ingredient_id,
                ingredient.fallback_name,
                ingredient_translation.name
            FROM ingredient_group
            INNER JOIN recipe_ingredient
                ON recipe_ingredient.ingredient_group_id = ingredient_group.id
            LEFT JOIN ingredient_translation
                ON ingredient_translation.ingredient_id = recipe_ingredient.ingredient_id
                AND ingredient_translation.country_code = ?
            INNER JOIN ingredient
                ON ingredient.id = recipe_ingredient.ingredient_id
            WHERE
                ingredient_group.id = ?
            GROUP BY
                recipe_ingredient.ingredient_id""",
            (country_code, recipe_id)
        )

@dataclass
class Language:
    country_code: str
    language_name: str
    icon: str

    @staticmethod
    def stepsLanguages(recipe_id: int) -> tuple[str, tuple[int]]:
        return (
            """SELECT 
                recipe_step.country_code,
                language.language_name,
                language.icon
            FROM recipe_step
            INNER JOIN language
                ON language.country_code = recipe_step.country_code
            WHERE 
                recipe_step.recipe_id = ?
            GROUP BY
                recipe_step.country_code""",
            (recipe_id, )
        )
    
    @staticmethod
    def recipeNameLanguages(recipe_id: int) -> tuple[str, tuple[int]]:
        return (
            """SELECT 
                language.country_code,
                language.language_name,
                language.icon
            FROM recipe_name_translation
            INNER JOIN language
                ON language.country_code = recipe_name_translation.country_code
            WHERE 
                recipe_name_translation.recipe_id = ?
            GROUP BY
                recipe_name_translation.country_code""",
            (recipe_id, )
        )

    @staticmethod
    def ingredientLanguages(ingredient_id: int) -> tuple[str, tuple[int]]:
        return (
            """SELECT 
                language.country_code,
                language.language_name,
                language.icon
            FROM ingredient_translation
            INNER JOIN language
                ON language.country_code = ingredient_translation.country_code
            WHERE 
                ingredient_translation.ingredient_id = ?
            GROUP BY
                ingredient_translation.country_code""",
            (ingredient_id, )
        )
    
    @staticmethod
    def ingredientLanguages(ingredient_group_id: int) -> tuple[str, tuple[int]]:
        return (
            """SELECT 
                language.country_code,
                language.language_name,
                language.icon
            FROM ingredient_group_translation
            INNER JOIN language
                ON language.country_code = ingredient_group_translation.country_code
            WHERE 
                ingredient_group_translation.ingredient_group_id = ?
            GROUP BY
                ingredient_group_translation.country_code""",
            (ingredient_group_id, )
        )


@dataclass
class TranslatedRecipe:
    id: int
    fallback_name: str
    translated_name: str

    @staticmethod
    def translatedRecipe(recipe_id: int, country_code:str) -> tuple[str, tuple[int, str]]:
        return (
            """SELECT 
                recipe.id,
                recipe.fallback_name,
                recipe_name_translation.name
            FROM
                recipe
            LEFT JOIN recipe_name_translation
                ON recipe_name_translation.recipe_id = recipe.id
                AND recipe_name_translation.country_code = ?
            WHERE 
                recipe.id = ?""",
            (country_code, recipe_id)
        )
    

@dataclass
class RecipeShort:
    id: int
    fallback_name: str
    translated_name: str

    @staticmethod
    def translatedRecipes(country_code: str) -> tuple[str, tuple[str]]:
        return (
            """SELECT
                recipe.id,
                recipe.fallback_name,
                recipe_name_translation.name
            FROM recipe
            LEFT JOIN recipe_name_translation
                ON recipe_name_translation.recipe_id = recipe.id
                AND recipe_name_translation.country_code = ?""",
            (country_code, )
        )