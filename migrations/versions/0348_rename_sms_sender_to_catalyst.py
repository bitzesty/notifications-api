"""

Revision ID: 898696388198
Revises: e3a56ce85041
Create Date: 2021-03-09 16:43:20.451832

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '898696388198'
down_revision = 'e3a56ce85041'


def upgrade():
    op.get_bind()
    op.execute("update service_sms_senders set sms_sender = 'Catalyst' where id = '286d6176-adbe-7ea7-ba26-b7606ee5e2a4'")


def downgrade():
    op.get_bind()
    op.execute("update service_sms_senders set sms_sender = 'GOVUK' where id = '286d6176-adbe-7ea7-ba26-b7606ee5e2a4'")
