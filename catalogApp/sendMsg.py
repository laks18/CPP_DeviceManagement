import boto3
from botocore.exceptions import ClientError

class Publisher:
    
    def send_SMS_message(self,mobile, my_message):
        try:
            sns_client = boto3.client('sns', region_name='us-east-1')
            print('\ndelivering the message {} to {}...\n'.format(my_message, mobile))
            sns_client.publish(PhoneNumber=mobile, Message=my_message)
        except ClientError as e:
            return False
        return True