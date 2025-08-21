from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///informal_worker.db"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session