import asyncio
from fastapi import FastAPI, WebSocketDisconnect, Form, Depends
from fastapi.responses import HTMLResponse
from typing_extensions import Annotated
from starlette.websockets import WebSocket

import dataset_interface
with open('ui.html', 'r') as file:
    html = file.read()

app = FastAPI()

# we get all the clients we have, so we could send changes to all users
ws_clients = []
def get_ws_clients():
    return ws_clients


# notifying clients with new data
def notify_all(clients):
    json_data = dataset_interface.get_dataset().to_json()
    futures = []
    for ws in clients:
        try:
            futures.append (ws.send_text(json_data))
        except WebSocketDisconnect:
            clients.remove(ws)
            print('Websocket disconnect: ', ws)
    return futures

# main page route
@app.get("/")
async def get():
    return HTMLResponse(html)

# update route
# it is updating dataset file and calling notify_all function
@app.post("/update")
async def update(column: Annotated[str, Form()], clients=Depends(get_ws_clients)):
    dataset_interface.update_column(column)
    json_data = dataset_interface.get_dataset().to_json()
    await asyncio.wait(notify_all(clients))
    return {"message": json_data}

# websockets route
# acsepting new clients, sending updates to them and removing clients
# if something goes not as we expected
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, clients=Depends(get_ws_clients)):
    await websocket.accept()
    print('Websocket connected')
    json_data = dataset_interface.get_dataset().to_json()
    await websocket.send_text(json_data)
    clients.append(websocket)
    try:
        while True:
            _ = await websocket.receive_text()
    except WebSocketDisconnect:
        clients.remove(websocket)
