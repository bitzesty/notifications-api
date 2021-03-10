"""

Revision ID: e3a56ce85041
Revises: 93fdd95e5ed3
Create Date: 2021-03-09 15:44:32.303444

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'e3a56ce85041'
down_revision = '93fdd95e5ed3'


def upgrade():
    op.get_bind()
    op.execute("update services set name = 'Catalyst Notify' where id = 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553'")


def downgrade():
    op.get_bind()
    op.execute("update services set name = 'GOV.UK Notify' where id = 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553'")
