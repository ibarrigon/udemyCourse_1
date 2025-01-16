[go back](../course_code.md)

# Images

This course module shows how to work with images, and use some kind of arrays (numpy)

## Libraries

1. numpy
2. opencv-python

# Show Images

## Errors

In ther first file work_images.py, when we work inside the docker container, we get an error. We need further 
investigation to work with this.

Excat message:
qt.qpa.xcb: could not connect to display
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/usr/local/lib/python3.12/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
 
Available platform plugins are: xcb.

Aborted (core dumped)

Explanation: 
It's normal, we are running a docker container, with no window. To run the file work_images.py you require a python's
local install.

This is not the objective of doing the course, but maybe in a future i can connect docker (linux) with Windows computer.

## Comments

If we change images to news.jpg, we can see that there are limitations for this work. Maybe this model isn't the 
most accurately one?

# Connect cameras

There is the "same" error. We can't connect the program (inside the docker) to the camera. We need to investigate, but
after some research (google, StackOverflow, ...) there is no response that can work for the current code. Need more 
research
