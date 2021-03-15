"""

Revision ID: e12edee68895
Revises: ab8ca793786f
Create Date: 2021-03-15 09:49:56.835337

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'e12edee68895'
down_revision = 'ab8ca793786f'


def upgrade():
    op.add_column('services', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('services_history', sa.Column('description', sa.Text(), nullable=True))



def downgrade():
    op.drop_column('services_history', 'description')
    op.drop_column('services', 'description')
