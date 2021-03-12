# How to setup clients to use the Catalyst Notify API

The Catalyst Notify service is based upon [GOV.UK Notify](https://www.notifications.service.gov.uk/), a well-established platform used by UK Government agencies to deliver SMS, email and physical (paper) messages.

To help government agencies integrate with the Notify service, [alphagov](https://github.com/alphagov/) maintain a collection of clients for most popular languages:

* [Java Client](https://github.com/alphagov/notifications-java-client)
* [Python Client](https://github.com/alphagov/notifications-python-client)
* [.NET Client](https://github.com/alphagov/notifications-net-client)
* [Ruby Client](https://github.com/alphagov/notifications-ruby-client)
* [PHP Client](https://github.com/alphagov/notifications-php-client)
* [Node.js Client](https://github.com/alphagov/notifications-node-client)

By default, each of the above clients will send API requests to the `gov.uk` production API. Since you're reading this documentation, it's likely you'll want to interact with the Catalyst Notify API, instead.

Each of the `alphagov` clients supports the passing of a new `baseurl` parameter, allowing the clients to be connected to the Catalyst Notify API:

* **Java**: Offers an [alternative constructor](https://github.com/alphagov/notifications-java-client/blob/ac4a437b63d28c98ee9e5b6a5ffb8111882949a6/src/main/java/uk/gov/service/notify/NotificationClient.java#L74-L80) that takes a `baseURL` as a compulsory argument.

* **.NET**: Offers an [alternative constructor](https://github.com/alphagov/notifications-python-client/blob/ec19d4dd08e2037df867aa5a7171849183f0b6e3/notifications_python_client/base.py#L17-L37) that takes `baseURL` as a compulsory argument.

* **Ruby**: Offers a [single constructor](https://github.com/alphagov/notifications-ruby-client/blob/6a681081878cfa972b56b42ebd6018c63f9ac5d3/lib/notifications/client.rb#L28-L30) that supports a `base_url` parameter. Constructor arguments ultimately get sent to `Notifications::Client::Speaker#initialize` where `@base_url` is set.

* **PHP**: Offers a [single constructor](https://github.com/alphagov/notifications-php-client/blob/master/src/Client.php#L67-L160) that takes `baseURL` as an optional argument.

* **Node.js**: Offers a [single constructor](https://github.com/alphagov/notifications-node-client/blob/master/client/api_client.js) that dynamically handles 1 or 2 arguments, allowing you to pass `urlBase` as the first parameter and `apiKeyid` as the second.
