"""

Revision ID: 02700689d4f8
Revises: 5235109e7268
Create Date: 2021-04-16 21:18:02.099371

"""
from alembic import op
import sqlalchemy as sa


revision = '02700689d4f8'
down_revision = '5235109e7268'


def upgrade():
    op.get_bind()
    op.execute("update provider_details set supports_international = True where identifier = 'twilio'")


def downgrade():
    op.get_bind()
    op.execute("update provider_details set supports_international = False where identifier = 'twilio'")
