This rest based API basically runs on AWS Lambda and Runs each time somebody interacts with it on my portfolio website.
All images are sent in base-64 from Angular frontend to this service so we filter the base-64 string of unneccessary information, and then image goes into Amazon lambda and it returns labels,
We then send those labels into bedrock LLM, we are using Amazon Titan G1.

<img width="1470" alt="Screenshot 2024-06-27 at 12 05 09 PM" src="https://github.com/kanwar280/ImageRekognition/assets/67856691/8a167590-8c0c-49cc-9b53-d2db90239a3c">
