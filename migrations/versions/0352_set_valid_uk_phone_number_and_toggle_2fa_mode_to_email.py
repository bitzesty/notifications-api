"""

Revision ID: 65fa84b9271b
Revises: 428551b7cf6f
Create Date: 2021-03-10 13:17:24.647527

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '65fa84b9271b'
down_revision = '428551b7cf6f'


def upgrade():
    op.execute("update users set mobile_number = '+447123456789' where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'")
    op.execute("update users set auth_type = 'email_auth' where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'")


def downgrade():
    op.execute("update users set mobile_number = '+441234123412' where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'")
    op.execute("update users set auth_type = 'sms_auth' where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'")
