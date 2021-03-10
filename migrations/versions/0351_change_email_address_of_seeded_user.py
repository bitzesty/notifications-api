"""

Revision ID: 428551b7cf6f
Revises: e17533d246ab
Create Date: 2021-03-10 12:45:08.022940

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import os

revision = '428551b7cf6f'
down_revision = 'e17533d246ab'


def upgrade():
    email_address = "support@" + os.environ.get("NOTIFY_EMAIL_DOMAIN", "example.com")
    op.execute("update users set email_address = '{}' where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'".format(email_address))

def downgrade():
    op.execute("update users set email_address = 'notify-service-user@digital.cabinet-office.gov.uk' where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'")
