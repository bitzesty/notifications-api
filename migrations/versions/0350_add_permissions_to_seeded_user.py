"""

Revision ID: e17533d246ab
Revises: 373ca3da3cfe
Create Date: 2021-03-10 12:23:39.706675

"""
from alembic import op
from datetime import datetime
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid

revision = 'e17533d246ab'
down_revision = '373ca3da3cfe'


def upgrade():
    op.get_bind()
    op.execute("update users set platform_admin = True where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'")
    op.execute("INSERT INTO permissions (id, user_id, service_id, permission, created_at) values ('{}', '6af522d0-2915-4e52-83a3-3690455a5fe6', 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553', 'manage_users', '{}')".format(str(uuid.uuid4()), datetime.utcnow()))
    op.execute("INSERT INTO permissions (id, user_id, service_id, permission, created_at) values ('{}', '6af522d0-2915-4e52-83a3-3690455a5fe6', 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553', 'manage_templates', '{}')".format(str(uuid.uuid4()), datetime.utcnow()))
    op.execute("INSERT INTO permissions (id, user_id, service_id, permission, created_at) values ('{}', '6af522d0-2915-4e52-83a3-3690455a5fe6', 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553', 'manage_settings', '{}')".format(str(uuid.uuid4()), datetime.utcnow()))
    op.execute("INSERT INTO permissions (id, user_id, service_id, permission, created_at) values ('{}', '6af522d0-2915-4e52-83a3-3690455a5fe6', 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553', 'send_texts', '{}')".format(str(uuid.uuid4()), datetime.utcnow()))
    op.execute("INSERT INTO permissions (id, user_id, service_id, permission, created_at) values ('{}', '6af522d0-2915-4e52-83a3-3690455a5fe6', 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553', 'send_emails', '{}')".format(str(uuid.uuid4()), datetime.utcnow()))
    op.execute("INSERT INTO permissions (id, user_id, service_id, permission, created_at) values ('{}', '6af522d0-2915-4e52-83a3-3690455a5fe6', 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553', 'send_letters', '{}')".format(str(uuid.uuid4()), datetime.utcnow()))
    op.execute("INSERT INTO permissions (id, user_id, service_id, permission, created_at) values ('{}', '6af522d0-2915-4e52-83a3-3690455a5fe6', 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553', 'manage_api_keys', '{}')".format(str(uuid.uuid4()), datetime.utcnow()))
    op.execute("INSERT INTO permissions (id, user_id, service_id, permission, created_at) values ('{}', '6af522d0-2915-4e52-83a3-3690455a5fe6', 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553', 'view_activity', '{}')".format(str(uuid.uuid4()), datetime.utcnow()))
    op.execute("update users set platform_admin = True where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'")


def downgrade():
    op.execute("update users set platform_admin = False where id = '6af522d0-2915-4e52-83a3-3690455a5fe6'")
    op.execute("DELETE from permissions where user_id = '6af522d0-2915-4e52-83a3-3690455a5fe6' AND permission = 'manage_users'")
    op.execute("DELETE from permissions where user_id = '6af522d0-2915-4e52-83a3-3690455a5fe6' AND permission = 'manage_templates'")
    op.execute("DELETE from permissions where user_id = '6af522d0-2915-4e52-83a3-3690455a5fe6' AND permission = 'manage_settings'")
    op.execute("DELETE from permissions where user_id = '6af522d0-2915-4e52-83a3-3690455a5fe6' AND permission = 'send_texts'")
    op.execute("DELETE from permissions where user_id = '6af522d0-2915-4e52-83a3-3690455a5fe6' AND permission = 'send_emails'")
    op.execute("DELETE from permissions where user_id = '6af522d0-2915-4e52-83a3-3690455a5fe6' AND permission = 'send_letters'")
    op.execute("DELETE from permissions where user_id = '6af522d0-2915-4e52-83a3-3690455a5fe6' AND permission = 'manage_api_keys'")
    op.execute("DELETE from permissions where user_id = '6af522d0-2915-4e52-83a3-3690455a5fe6' AND permission = 'view_activity'")

