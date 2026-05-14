from app.db.session import SessionLocal
from app.models.lesson import BoardLesson
from app.models.exercise import TerminalExercise
from app.db.base import Base
from app.db.session import engine

def seed_db():
    # Ensure tables are created
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Check if we already seeded to avoid duplicates
    existing_lesson = db.query(BoardLesson).filter_by(title="Manejo de Variables y Memoria en Python").first()
    if existing_lesson:
        print("Database already seeded!")
        db.close()
        return

    # 1. Create a dummy BoardLesson
    lesson = BoardLesson(
        title="Manejo de Variables y Memoria en Python",
        theory_content="En Python, las variables son referencias a objetos en memoria. Si asignas una lista a otra variable, ambas apuntan a la misma lista.",
        syntax_tips="Usa id() para comprobar si dos variables apuntan al mismo objeto en memoria.",
        language="Python"
    )
    db.add(lesson)
    db.commit()
    db.refresh(lesson)

    # 2. Create the TerminalExercise related to memory/variables
    exercise = TerminalExercise(
        lesson_id=lesson.id,
        title="Referencias a Listas",
        problem_statement="Dadas dos variables, `lista_a` y `lista_b`. Si `lista_b = lista_a` y modificas `lista_b`, ¿qué pasa con `lista_a`? Escribe un código que demuestre esto modificando `lista_b` para que ambas listas terminen siendo `[1, 2, 3, 4]`.",
        initial_code="lista_a = [1, 2, 3]\nlista_b = lista_a\n# Tu código aquí\n\nprint(lista_a)",
        expected_output="[1, 2, 3, 4]",
        difficulty="Medium"
    )
    db.add(exercise)
    db.commit()

    print("Database successfully seeded with Python variable/memory management exercise!")
    db.close()

if __name__ == "__main__":
    seed_db()
