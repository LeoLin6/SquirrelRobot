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

<iframe width="560" height="315" src="https://www.youtube.com/embed/upieNQVjNqw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Second Milestone

Next step is to make a robot capable of driving around the outside terrian. To suit that outdoor requirement, I chose a tank chassis for my robot. The components for this step is: wires, breadboard, battery packs, motor driver, and motors. First step I made a circuit diagram to plan out the electrical components. Basically, the raspiberry pi controls the motor driver, and the motor driver is then connected to the motors to power them. At last, I looked into the documentation for raspiberry pi to send signals using its ports, and wrote the code for the robot to run on keyboard.

# Final Milestone

