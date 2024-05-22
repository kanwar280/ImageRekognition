import json
import base64
import boto3



def lambda_handler(event, context):
  
    return {
        'statusCode': 200,
        'body': json.dumps(imageAnalyzer(event))
    }
def interact_with_LLM(prompt):
    bedrock_client = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-east-1')
    
    parameters = {
        "maxTokenCount":512,
        "stopSequences":[],
        "temperature":0,
        "topP":0.9}
    body = json.dumps({"inputText": prompt, "textGenerationConfig": parameters})
    modelId = "amazon.titan-text-express-v1" # change this to use a different version from the model provider
    accept = "application/json"
    contentType = "application/json"
    response = bedrock_client.invoke_model(
    body=body, modelId=modelId, accept=accept, contentType=contentType)
    
    response_body = json.loads(response.get("body").read())
    response_text_titan = response_body.get("results")[0].get("outputText")
    return response_text_titan

def imageAnalyzer(event):
    
    
    
    image_bytes = event['base64img']
    img_b64decoded = base64.b64decode(image_bytes + '==')
    
    img_modified = str(img_b64decoded);
    rek_client = boto3.client('rekognition')
    response = rek_client.detect_labels(Image={'Bytes':img_b64decoded})

    labels = response['Labels']
    print(f'Found {len(labels)} labels in the image:')
    label_names = ''
    labelss = []
    for label in labels:
        name = label['Name']
        confidence = label['Confidence']
        #print(f'> Label "{name}" with confidence {confidence:.2f}')
        if confidence>60:
            labelss.append(name)
#            label_names = label_names + name + ","
    
    prompt = "Human: Please provide a human readible and Understandable summary of an image based on these labels: "
    for i in range(len(labelss)):
        prompt = prompt + labelss[i]+", "
    prompt = prompt + " Assistant: "
    response_text = interact_with_LLM(prompt)
    return response_text
