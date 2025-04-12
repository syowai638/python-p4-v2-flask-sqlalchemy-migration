"""rename department

Revision ID: a43183db16d6
Revises: f25c0c0d3bb5
Create Date: 2025-04-12 20:47:19.300162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a43183db16d6'
down_revision = 'f25c0c0d3bb5'
branch_labels = None
depends_on = None


def upgrade():
    # Correct: Rename the table instead of drop & create
    op.rename_table('department', 'departments')


def downgrade():
    # Revert table name change
    op.rename_table('departments', 'department')

