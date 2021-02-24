import json

from app.clients.sms import SmsClient
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

class TwilioClient(SmsClient):
    '''
    Twilio SMS client.
    '''

    def init_app(self, current_app, statsd_client, *args, **kwargs):
        super(SmsClient, self).__init__(*args, **kwargs)
        self.current_app = current_app
        self.twilio_sid = current_app.config.get('TWILIO_SID')
        self.twilio_auth_token = current_app.config.get('TWILIO_AUTH_TOKEN')
        self.from_number = current_app.config.get('FROM_NUMBER')
        self.name = 'twilio'
        self.statsd_client = statsd_client

    def get_name(self):
        return self.name

    def record_outcome(self, response):
        response_json = json.loads(response.content)
        status_code = response.status_code
        error_code = response_json.get('code', None)

        if error_code:
            with open('app/clients/sms/twilio_error_codes.json') as f:
                error_mappings = json.load(f)
                error = error_mappings.get(str(error_code), None)

            self.statsd_client.incr("clients.twilio.error")
            log_message = "Received {} response from Twilio. Error {} ({})".format(status_code, error_code, error.get('message'))
        else:
            self.statsd_client.incr("clients.twilio.success")
            log_message = "Received {} from Twilio API.".format(status_code)

        self.current_app.logger.info(log_message)


    def send_sms(self, to, content, sender=None):
        try:
            client = Client(self.twilio_sid, self.twilio_auth_token)
            message = client.messages.create(
                to=to,
                from_=self.from_number if sender is None else sender,
                body=content
                )
            self.record_outcome(client.http_client.last_response)
        except TwilioRestException as exception:
            self.record_outcome(client.http_client.last_response)
