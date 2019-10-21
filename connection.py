from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_string = 'postgresql://postgres:"senha"@localhost:5432/"nome_da_base"'

engine = create_engine(db_string)
Session = sessionmaker(bind=engine)

