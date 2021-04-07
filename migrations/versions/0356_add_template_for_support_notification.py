"""

Revision ID: 07ed5bddc724
Revises: 1dc64fef5092
Create Date: 2021-04-05 22:38:09.532413

"""
from datetime import datetime
from alembic import op
from flask import current_app


revision = '07ed5bddc724'
down_revision = '1dc64fef5092'

email_template_id = '82456472-ca40-4dda-9328-d08af07fade5'


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
        "There is new support request.",
        "",
        "Message:",
        "((message))",
        "Name:",
        "((name))",
        "Email:",
        "((email))",
        "",
        "Thanks,",
        "",
        "Catalyst Notify Team",
    ])

    email_template_name = "Notify admins about new support request"
    email_template_subject = 'New support request'

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
