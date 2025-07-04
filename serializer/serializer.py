def convertfastapi(fastapi) -> dict:
    return {
        "id": str(fastapi.get("_id", "")),
        "name": fastapi.get("name", ""),
        "email": fastapi.get("email", "")
    }

def convertfastapis(fastapis) -> list:
    return [convertfastapi(fastapi) for fastapi in fastapis]
