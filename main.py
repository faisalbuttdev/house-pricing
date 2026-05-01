from fastapi import Fastapi
app=Fastapi()

@app.get("/")
async def func():
    return f"housepricing"