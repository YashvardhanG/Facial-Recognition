# Facial-Recognition
<!-- LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Yashvardhang/Facial-Recognition">
    <img src="Resources/recognition.png" alt="Logo" width="128" height="128">
  </a>

  <h3 align="center">Facial Recognition</h3>
  <p align="center">
    A simple software built using Python, Numpy and OpenCV
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#working">Working</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contribute">Contribute</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT -->
## About

This **Facial Recognition** project was built in order to study the intricacies of **Facial Biometrics** and, the multiple training models used behind the process. A facial recognition system is a technology capable of matching a human face from a digital image or a video frame against a database of faces, typically employed to authenticate users through ID verification services, works by pinpointing and measuring facial features from a given image <a href = "https://en.wikipedia.org/wiki/Facial_recognition_system">(wiki)</a>. 

Facial recognition systems are primarily employed in facial biometrics and ID verification. You may head on the the <a href="#working">Working</a> section to view the working process of the project.

This project has been developed using the *Python* programming language. This software further will require some modules for its working. The list of required modules and installation commands have been given in the <a href="#requirements">next</a> section.

<!-- REQUIREMENTS -->
## Requirements

To install all the required Python Modules, Pull the project, Open Command Prompt, and then type the following command:

```
 > pip install -r requirements.txt
```

**Note:** Make sure to change the directory to the directory where the project has been stored. 

You may also download all of them individually using the statements below.

List of Pre-Requisite Python Modules:

```
 > pip install opencv-python
 > pip install numpy
 > pip install Pillow
```

<!-- WORKING -->
## Working

Currently, there are a total of two sections in this project.
<ol>
  <li><b>Facial Recognition:</b><br>This section deals with the initial model. It takes your photos, trains your dataset, and then it can further recognise your face using the trained dataset. It'll display the name and the accuracy of the recognition.</li><br>
  <li><b>Facial Biometrics:</b><br>This sections deals with the application of the previous section. It's a sample biometric system through which one can verify their identity. It's training and models are common to the previous one.</li><br>
</ol>

This project uses a pre-exisiting frontal face cascade known as the <a href = "https://github.com/opencv/opencv">haarcascade_frontalface_default</a>. This cascade helps in defining the facial features and hence, in recognition.

<ol>
<li>Photos are captured with the help of OpenCV. All photos are saved locally and no data is transferred or communicated.</li>
<li>By using Numpy, the photos captured are trained and saved in a '.yml' trained model file.</li>
<li>Finally, by using OpenCV and the previously trained model, the software recognises your identity and the percentage of facial matching.</li>
</ol>
<br>

**Note:** Make sure to pull and keep all these codes into a single directory.
<br><br>

Currently, this project is working on the facial biometrics section. If you want to contribute into this project head on to the <a href="#contribute">Contribute</a> section.

<!-- LICENSE -->
## License

Distributed under the MIT License. See <a href = "https://github.com/YashvardhanG/Facial-Recognition/blob/main/LICENSE"> LICENSE </a> for more information.

<!-- contribute -->
## Contribute

Every program is ever evolving and, that is possible only with valuable contributions. Any contributions you make are greatly appreciated. 
<ol>
  <li>Fork the Project</li>
  <li>Create your Feature Branch (git checkout -b functionalities/Feature)</li>
  <li>Commit your Changes (git commit -m 'Add a Feature')</li>
  <li>Push to the Branch (git push origin functionalities/Feature)</li>
  <li>Open a Pull Request</li>
</ol>

<br>If you have any further ideas or comments, go ahead to the next section and feel free to connect! 

<!-- CONTACT -->
## Contact

<p align="center">
  <br>
  <a href="https://www.spiralcosmos.com">
  <img src="https://github.com/YashvardhanG/YashvardhanG/blob/main/Spiral%20Cosmos.png" alt="Logo" width="155" height="140"><br>
  </a>
  <a href = "https://www.spiralcosmos.com">Spiral Cosmos</a>
</p>

<!-- Acknowledgement -->
## Acknowledgements

<ul>
  <li>Cascade for Frontal Face Detection: <a href = "https://github.com/opencv/opencv/tree/master/data/haarcascades">OpenCV (haarcascade_frontalface_default)</a></li>
  <li>Icon: <a href = "https://www.flaticon.com/authors/eucalyp">Flaticon</a>
</ul>

