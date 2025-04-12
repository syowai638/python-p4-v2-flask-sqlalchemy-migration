"""rename address

Revision ID: 96d60ad189a7
Revises: a43183db16d6
Create Date: 2025-04-12 20:56:41.928306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96d60ad189a7'
down_revision = 'a43183db16d6'
branch_labels = None
depends_on = None


def upgrade():
    # Rename the column instead of drop/create
    op.alter_column('departments', 'address', new_column_name='location')


def downgrade():
    # Rename it back
    op.alter_column('departments', 'location', new_column_name='address')
