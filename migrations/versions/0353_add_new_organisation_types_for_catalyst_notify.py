"""

Revision ID: ab8ca793786f
Revises: 65fa84b9271b
Create Date: 2021-03-11 16:41:34.595043

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = 'ab8ca793786f'
down_revision = '65fa84b9271b'


def upgrade():
    op.get_bind()
    op.execute("INSERT INTO organisation_types (name, annual_free_sms_fragment_limit, is_crown) values ('charity', 25000, 'False')")
    op.execute("INSERT INTO organisation_types (name, annual_free_sms_fragment_limit, is_crown) values ('community_interest', 25000, 'False')")

def downgrade():
    op.get_bind()
    op.execute("DELETE from organisation_types where name = 'charity'")
    op.execute("DELETE from organisation_types where name = 'community_interest'")
