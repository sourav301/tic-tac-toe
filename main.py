from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from data import InvalidMoveException, Player, Symbol
from state import EndState
from ticTacToeSystem import TicTacToeSystem

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
system = TicTacToeSystem()

PLAYERS = {
    "X": Player("Player X", Symbol.CROSS),
    "O": Player("Player O", Symbol.CIRCLE),
}


class MoveRequest(BaseModel):
    row: int
    col: int
    symbol: str


def board_state():
    game = system.game
    if not game:
        return None
    result = []
    for r in range(game.board.size):
        row = []
        for c in range(game.board.size):
            row.append(game.board.get_cell(r, c).get_symbol().value)
        result.append(row)
    return result


def game_status():
    game = system.game
    if not game:
        return {"status": "no_game"}
    is_over = isinstance(game.state, EndState)
    winner = None
    if is_over and game.winner:
        winner = game.winner.get_symbol().value
    current = game.current_player.get_symbol().value
    return {
        "status": "ended" if is_over else "in_progress",
        "board": board_state(),
        "current_player": current,
        "winner": winner,
    }


@app.post("/game")
def create_game():
    system.create_game(3, player1=PLAYERS["X"], player2=PLAYERS["O"])
    return game_status()


@app.get("/game")
def get_game():
    return game_status()


@app.post("/move")
def make_move(req: MoveRequest):
    if not system.game:
        raise HTTPException(status_code=400, detail="No active game")
    try:
        system.make_move(req.row, req.col, player=PLAYERS[req.symbol])
    except InvalidMoveException as e:
        raise HTTPException(status_code=400, detail=str(e))
    return game_status()


@app.get("/")
def serve_frontend():
    return FileResponse("index.html")
