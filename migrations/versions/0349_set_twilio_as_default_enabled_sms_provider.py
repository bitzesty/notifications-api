"""

Revision ID: 373ca3da3cfe
Revises: 898696388198
Create Date: 2021-03-09 16:49:58.504055

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid

revision = '373ca3da3cfe'
down_revision = '898696388198'


def upgrade():
    op.get_bind()
    op.execute("update provider_details set active = False where identifier = 'mmg'")
    op.execute("update provider_details set active = False where identifier = 'firetext'")
    op.execute("INSERT INTO provider_details (id, display_name, identifier, priority, notification_type, version, active) values ('{}', 'Twilio', 'twilio', 10, 'sms', 1, true)".format(str(uuid.uuid4())))

def downgrade():
    op.get_bind()
    op.execute("update provider_details set active = True where identifier = 'mmg'")
    op.execute("update provider_details set active = True where identifier = 'firetext'")
    op.execute("delete from provider_details where identifier = 'twilio'")
