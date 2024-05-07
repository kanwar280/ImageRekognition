import json
import base64
import boto3


def lambda_handler(event, context):
  
    return {
        'statusCode': 200,
        'body': json.dumps(imageAnalyzer(event))
    }

def imageAnalyzer(event):
    
    image_bytes = event['base64img']
    img_b64decoded = base64.b64decode(image_bytes + '==')
    
    img_modified = str(img_b64decoded);
    rek_client = boto3.client('rekognition')
    response = rek_client.detect_labels(Image={'Bytes':img_b64decoded})

    labels = response['Labels']
    print(f'Found {len(labels)} labels in the image:')
    label_names = ''
    for label in labels:
        name = label['Name']
        confidence = label['Confidence']

        if confidence>60:
            print(name + " | " + str(confidence))
            label_names = label_names + name + ","

    return label_names
