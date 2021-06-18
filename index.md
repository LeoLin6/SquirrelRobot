# Squrrel chasing robot (object detection)
I wanted to create a robot to chase the squirrels and other animals in my yard away because they are eating the plants:( So the general idea is to have a outdoors wheeled vehicle that is autonomous, it drives around on its own and follow the squirrel by tracking it in the camera. 

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Leo L | Monta Vista High School | Electrical Engineering | Incoming Junior

<html>
  <img src="https://th.bing.com/th/id/R24c9e8340b2965bc271c3e8866cfb555?rik=MsvkVa4FWkEejQ&riu=http%3a%2f%2fassets.libsyn.com%2fcontent%2f3981369&ehk=LLQvS3SXn65HrTPbEkl%2feF%2bA7pBY2IMpS%2fyjzVZdA7A%3d&risl=&pid=ImgRaw">
</html>

# First Milestone
  

My first milestone was setting up my raspberry pi and connecting the nessary camera component. I had to install Raspiberru pi imager on the SD card and plug it into the raspberry board, then it powered up. Next, because I didn't have a spare monitor, I had to set up VNC to remotely view and control my raspberry. Now I can control the raspberry from a window on my personal computer. 

<html>
  <img src=".\Squirrel\nanonet.png">
</html>

Next, i want to test out object detection. So i went on nanonets, which is a AI training API website. They asked for 50 pictures of squirrels, and I learned that boxing(annotating) the squirrels in the pictures manually helps the model to be trained to identify squirrels. After the training is complete and tested for accuracy, I get a piece of python code that calls my unique nanonets model API. I can insert it anywhere in my python code and it will return me a json file stating where the squirrel is in the picture by coordinates. Nanonets has a tester itself, so I uploaded a squirrel picture I have not used before, and got a result with the squirrel annotated :) 

# Final Milestone
My final milestone is the increased reliability and accuracy of my robot. I ameliorated the sagging and fixed the reliability of the finger. As discussed in my second milestone, the arm sags because of weight. I put in a block of wood at the base to hold up the upper arm; this has reverberating positive effects throughout the arm. I also realized that the forearm was getting disconnected from the elbow servo’s horn because of the weight stress on the joint. Now, I make sure to constantly tighten the screws at that joint. 

Cool video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/DTvS9lvRxZ8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


# Second Milestone
My final milestone is the increased reliability and accuracy of my robot. I ameliorated the sagging and fixed the reliability of the finger. As discussed in my second milestone, the arm sags because of weight. I put in a block of wood at the base to hold up the upper arm; this has reverberating positive effects throughout the arm. I also realized that the forearm was getting disconnected from the elbow servo’s horn because of the weight stress on the joint. Now, I make sure to constantly tighten the screws at that joint.

[![Third Milestone](https://res.cloudinary.com/marcomontalbano/image/upload/v1612574014/video_to_markdown/images/youtube--y3VAmNlER5Y-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=y3VAmNlER5Y&feature=emb_logo "Second Milestone"){:target="_blank" rel="noopener"}


[![First Milestone](https://res.cloudinary.com/marcomontalbano/image/upload/v1612574117/video_to_markdown/images/youtube--CaCazFBhYKs-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=CaCazFBhYKs "First Milestone"){:target="_blank" rel="noopener"}
