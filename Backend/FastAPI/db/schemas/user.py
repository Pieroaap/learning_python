from db.models.user import User

def user_schema(user) -> dict:
    """
    Converts a user object to a dictionary.
    
    Args:
        user: The user object to convert.
        
    Returns:
        A dictionary representation of the user.
    """
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "surname": user["surname"],
        "age": user["age"]
    }

def users_schema(users) -> list:
    return [User(**user) for user in users] if users else []