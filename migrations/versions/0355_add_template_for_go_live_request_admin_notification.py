"""

Revision ID: 1dc64fef5092
Revises: e12edee68895
Create Date: 2021-03-16 12:51:15.736512

"""
from datetime import datetime

from alembic import op
from flask import current_app
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '1dc64fef5092'
down_revision = 'e12edee68895'

email_template_id = '63ec0cba-6178-4bdf-b44c-fbab042e4f4e'


def upgrade():
    template_insert = """
        INSERT INTO templates (id, name, template_type, created_at, content, archived, service_id, subject,
        created_by_id, version, process_type, hidden)
        VALUES ('{}', '{}', '{}', '{}', '{}', False, '{}', '{}', '{}', 1, '{}', false)
    """
    template_history_insert = """
        INSERT INTO templates_history (id, name, template_type, created_at, content, archived, service_id, subject,
        created_by_id, version, process_type, hidden)
        VALUES ('{}', '{}', '{}', '{}', '{}', False, '{}', '{}', '{}', 1, '{}', false)
    """

    email_template_content = '\n'.join([
        "Hi,",
        "",
        "A Catalyst Notify service, ((service_name)), has requested to go live.",
        "",
        "Please review their request as soon as possible by following the link below:",
        "",
        "((service_dashboard_url))",
        "",
        "Thanks,",
        "",
        "Catalyst Notify Team",
    ])

    email_template_name = "Notify admins fo new go-live request"
    email_template_subject = 'A service has requested to go-live'

    op.execute(
        template_history_insert.format(
            email_template_id,
            email_template_name,
            'email',
            datetime.utcnow(),
            email_template_content,
            current_app.config['NOTIFY_SERVICE_ID'],
            email_template_subject,
            current_app.config['NOTIFY_USER_ID'],
            'normal'
        )
    )

    op.execute(
        template_insert.format(
            email_template_id,
            email_template_name,
            'email',
            datetime.utcnow(),
            email_template_content,
            current_app.config['NOTIFY_SERVICE_ID'],
            email_template_subject,
            current_app.config['NOTIFY_USER_ID'],
            'normal'
        )
    )

    # If you are copying this migration, please remember about an insert to TemplateRedacted,
    # which was not originally included here either by mistake or because it was before TemplateRedacted existed
    op.execute(
        """
            INSERT INTO template_redacted (template_id, redact_personalisation, updated_at, updated_by_id)
            VALUES ('{}', '{}', '{}', '{}')
            ;
        """.format(email_template_id, False, datetime.utcnow(), current_app.config['NOTIFY_USER_ID'])
    )

def downgrade():
    op.execute("DELETE FROM notifications WHERE template_id = '{}'".format(email_template_id))
    op.execute("DELETE FROM notification_history WHERE template_id = '{}'".format(email_template_id))
    op.execute("DELETE FROM template_redacted WHERE template_id = '{}'".format(email_template_id))
    op.execute("DELETE FROM templates_history WHERE id = '{}'".format(email_template_id))
    op.execute("DELETE FROM templates WHERE id = '{}'".format(email_template_id))
