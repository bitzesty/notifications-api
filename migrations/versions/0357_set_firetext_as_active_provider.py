"""

Revision ID: 5235109e7268
Revises: 07ed5bddc724
Create Date: 2021-04-14 23:32:09.513520

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '5235109e7268'
down_revision = '07ed5bddc724'


def upgrade():
    op.get_bind()
    op.execute("update provider_details set active = True where identifier = 'firetext'")


def downgrade():
    op.get_bind()
    op.execute("update provider_details set active = False where identifier = 'firetext'")
