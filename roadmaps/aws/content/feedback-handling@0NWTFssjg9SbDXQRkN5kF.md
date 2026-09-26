# Feedback Handling

SES can receive delivery notifications, bounces, and complaint feedback from recipient mail servers. These events are delivered via SNS or SQS and should be processed to remove invalid addresses and maintain a clean sending list. Ignoring bounce and complaint feedback leads to reputation damage and account suspension.

Visit the following resources to learn more:

- [@official@Feedbacks](https://aws.amazon.com/ses/faqs)