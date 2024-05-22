This rest based API basically runs on AWS Lambda and Runs each time somebody interacts with it on my portfolio website.
All images are sent in base-64 from Angular frontend to this service so we filter the base-64 string of unneccessary information, and then image goes into Amazon lambda and it returns labels,
We then send those labels into bedrock LLM, we are using Amazon Titan G1, it was the cheapest one.

It looks something like this right now, but the UI will be changes in a couple days.
<img width="1470" alt="Screenshot 2024-05-22 at 2 54 24 AM" src="https://github.com/kanwar280/ImageRekognition/assets/67856691/72796860-c7c9-4946-b5c6-5a1e0983f1dc">
