from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer 
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy import inspect

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)  
    endereco = Column(String(9))  

    contas = relationship("Conta", back_populates="cliente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf}, endereco={self.endereco})"

class Conta(Base):
    __tablename__ = "contas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(Float)
    id_cliente = Column(Integer, ForeignKey("clientes.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="contas")

    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo})"

# print(Cliente.__tablename__)
# print(Conta.__tablename__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
# print(inspetor_engine.has_table("Clientes"))
# print(inspetor_engine.get_table_names())
# print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    Walter = Cliente(
        nome = 'walter',
        cpf = '123.456.789-12',
        endereco= '98765-432',
        contas = [Conta(
            tipo='conta-corrente',
            agencia='lontra',
            num='2425',
            saldo='700.00',
        )]
    )

    Joao_Pedro = Cliente(
        nome = 'jotape',
        cpf = '123.456.789-12',
        endereco= '12345-678',
        contas = [Conta(
            tipo='poupança',
            agencia='lontra',
            num='1234',
            saldo='54000.00',
        )]
    )

    Fernanda = Cliente(
        nome = 'fernanda',
        cpf = '789.456.123-12',
        endereco= '78956-123',
        contas = [Conta(
            tipo='conta-corrente',
            agencia='minas',
            num=7879,
            saldo='50.00',
        )]
    )

    session.add_all([Walter, Joao_Pedro, Fernanda])

    session.commit()

stmt_order = select(Cliente)
print('\nRecuperando informações dos Clientes')
for result in session.scalars(stmt_order):
    print(result)

stmt_conta = select(Conta)
print('Recuperando informações das Contas')
for conta in session.scalars(stmt_conta):
    print(conta)

# stmt_join = select(Cliente.nome, Conta.agencia).join_from(Conta, Cliente)
# for result in session.scalars(stmt_join):
#     print(result)

# connection = engine.connect()
# results = connection.execute(stmt_join).fetchall()
# print("\nExecutando statment a partir da conecction")
# for result in results:
#     print(result)

stmt_count = select(func.count('*')).select_from(Cliente)
print("\nTotal de instâncias em Clientes")
for result in session.scalars(stmt_count):
    print(result)