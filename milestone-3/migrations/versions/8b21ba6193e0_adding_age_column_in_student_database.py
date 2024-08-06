"""Adding age column in student database

Revision ID: 8b21ba6193e0
Revises: bd10cd63ae2f
Create Date: 2024-08-06 13:57:43.908816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b21ba6193e0'
down_revision = 'bd10cd63ae2f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    ALTER TABLE students
    ADD COLUMN age INT;
    """)


def downgrade():
    op.execute("""
    ALTER TABLE students
    DROP COLUMN age;
    """)
