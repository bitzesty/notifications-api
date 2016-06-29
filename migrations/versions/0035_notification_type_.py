"""empty message

Revision ID: 0035_notification_type
Revises: 0034_pwd_changed_at_not_null
Create Date: 2016-06-29 10:48:55.955317

"""

# revision identifiers, used by Alembic.
revision = '0035_notification_type'
down_revision = '0034_pwd_changed_at_not_null'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('notifications', sa.Column('notification_type', sa.String(), nullable=True))
    op.execute('update notifications set notification_type = (select distinct(template_type) '
               'from templates where templates.id = notifications.template_id)')
    op.alter_column('notifications', 'notification_type', nullable=False)

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notifications', 'notification_type')
    ### end Alembic commands ###
