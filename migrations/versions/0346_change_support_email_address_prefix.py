"""

Revision ID: 93fdd95e5ed3
Revises: 0345_move_broadcast_provider
Create Date: 2021-03-09 12:16:26.045409

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '93fdd95e5ed3'
down_revision = '0345_move_broadcast_provider'


def upgrade():
    op.get_bind()
    op.execute("update services set email_from = 'noreply' where id = 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553'")


def downgrade():
    op.get_bind()
    op.execute("update services set email_from = 'gov.uk.notify' where id = 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553'")
