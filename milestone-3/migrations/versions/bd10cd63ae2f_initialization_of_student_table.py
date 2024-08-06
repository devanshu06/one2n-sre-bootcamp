"""Initialization of Student Table

Revision ID: bd10cd63ae2f
Revises: 
Create Date: 2024-08-06 13:49:28.647091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd10cd63ae2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);
    """)


def downgrade():
    op.execute("""
    DROP TABLE students;
    """)
