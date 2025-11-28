from fastapi import FastAPI

app = FastAPI()

mevalar = [
    "tarvuz",
    "qovun",
    "qulupnay",
    "malina",
    "nok"
]


# 1️⃣ GET — Barcha mevalar
@app.get("/mevalar")
def mevalar_list():
    return {
        "message": "ok",
        "data": mevalar
    }


# 2. GET — Boshlanishiga qarab filtrlash
@app.get("/mevalar/start")
def mevalar_start(meva_nomi: str = ""):
    res = [m for m in mevalar if m.startswith(meva_nomi)]
    return {"message": "ok", "data": res}


# 3.GET — Tugashiga qarab filtrlash
@app.get("/mevalar/end")
def mevalar_end(meva_nomi: str = ""):
    res = [m for m in mevalar if m.endswith(meva_nomi)]
    return {"message": "ok", "data": res}


# POST — Meva qo‘shish
@app.post("/mevalar/create/")
def meva_yaratish_page(meva_nomi: str):
    mevalar.append(meva_nomi)
    return {"message": "meva yaratildi"}


# GET — ID bo‘yicha
@app.get("/mevalar/{meva_id}")
def meva_detail_page(meva_id: int):
    return {
        "message": "ok",
        "meva": mevalar[meva_id]
    }

@app.delete("/mevalar/{meva_id}/delete")
def meva_delete_page(meva_id: int):
    mevalar.pop(meva_id)
    return {"message": "meva ochirildi."}

@app.patch("/mevalar/{meva_id}/update")
def meva_update_page(meva_id:int, yangi_nom: str):
    mevalar[meva_id] = yangi_nom
    return {"message" : "meva ozgartirildi."}


@app.get("/")
def home_page():
    return {"message": "hello world"}
