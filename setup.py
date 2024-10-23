from cx_Freeze import setup, Executable

setup(
    name="Snake Game",
    version="1.0",
    description="Juego de Snake",
    executables=[Executable("snake.py")]
)
