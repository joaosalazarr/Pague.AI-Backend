import pytest
from app.db.session import SessionLocal
from sqlalchemy import text

def test_database_connection():
    db = None
    try:
        db = SessionLocal()
        result = db.execute(text('SELECT 1'))
        assert result.scalar() == 1
    except Exception as e:
        pytest.fail(f'Não conseguiu conectar ao banco: {e}')
    finally:
        if db:
            db.close()