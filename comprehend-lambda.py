import json
import boto3

def lambda_handler(event,context):
    text="""
    India is the best country out there. 
    """

    client_sentiment = boto3.client("comprehend")
    response = client_sentiment.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )

    print (response)

    translate = boto3.client(service_name='translate',
                             region_name='ca-central-1',
                             use_ssl=True)

    result = translate.translate_text(Text=text,
                                      SourceLanguageCode='en',
                                      TargetLanguageCode='en' )
    
    print('TranslateText: ' + result.get('TranslatedText'))
    print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
    print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))

    return {
        'statusCode' : 200,
        'body' : json.dumps('Hello from Lambda'),
        'Translated' : result.get('TranslatedText'),
        'Response': response

    }