from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine('sqlite:///banco.db')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Tarefa(Base):
    __tablename__ = 'tarefas'
    id_tarefa = Column(Integer, primary_key=True)
    nome_tarefa = Column(String(40), nullable=False, index=True)
    status = Column(String, nullable=False, index=True)
    data = Column(String(11), nullable=False, index=True)
    horario = Column(String, index=True)
    descricao = Column(String, index=True)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_tarefa(self):
        return {
            "id_tarefa": self.id_tarefa,
            "nome_tarefa": self.nome_tarefa,
            "status": self.status,
            "data": self.data,
            "horario": self.horario,
            "descricao": self.descricao
        }

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
