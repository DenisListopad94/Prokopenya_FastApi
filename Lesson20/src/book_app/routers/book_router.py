from fastapi import APIRouter


router = APIRouter(
    prefix="",
    tags=["Booking"]
)


@router.get("/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


@router.get("/item")
def get_query_types(item_id: int, name: str,) -> dict:
    return {"item_id": item_id, "name": name}


@router.get("/{name}")
def get_types(name: str, id_: int, age: int) -> dict:
    return {"name": name, "item_id": id_, "age": age}
