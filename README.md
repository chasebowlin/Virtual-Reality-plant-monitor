<h1>CROFT</h1>
<li>Customizable, Remote, Oculus Rift, Farming, Tool.</li>
<li>  <i>A tool that takes the busy work out of monitoring plants. Implements several sensors on a wifi capable development board, a server that is connected to a database, and a virtual reality user interface where users can interact with the data</i></li>
<h2>Contents</h2>
<a href="#abstract"> 1. Description</a><br>
<a href="#usage">2. Software Required for Use</a><br>
<a href="#compilation">3. Compilation</a><br>
<a href="#about">4. About</a><br>
<hr>
<h3 id="abstract">Description</h3>
<p> This project was designed to take the busy work out of monitoring your plants' enviroment and tracking the history of how your plants have been doing.
The idea stemed from the need to insure the best living conditions for plants without constant human interaction. 
By implementing technology, promoting a healthy environment for a plant(s) is much simpler even if the user does not have a green thumb.
</p>
<p> Another main idea for this project was to allow a user to keep track of multiple plants at once unlike many products on the market now that can only allow to see data about one plant by connecting to each device via bluetooth.
The application gathers all the data from each of the different photons, which each photon represents one plant, into one place and is displayed in one easy to use user application.
THis project was also designed to be far cheaper than the leading IoT plant monitoring devices. </p>
<h4> Three Major Components: </h4>
<b> The Photon </b>
<li> Arduino like development board with built in WiFi capabilities </li>
<li> DHT11 Sensor to measure temperature and humidity </li>
<li> Photoresistor to measure light intensity in lumens </li>
<li> soil moisture sensor </li>
<li> continously sends data about a plant's environment to the server </li>
<li><i><a href="https://docs.particle.io/datasheets/photon-(wifi)/photon-datasheet/">documentation about Particle Photon here</a></i></li>
<p></p>
<b>The Server</b>
<li> Python 3.6 </li>
<li> creates and connects to a SQLite Database where all information about each photon and its sensor readings are stored </li>
<li> calculates the ephemiris of the Sun </li>
<li> runs in the background with any computer </li>
<p></p>
<b> The User Interface </b>
<li> runs on the Oculus Rift </li>
<li> built using the Unity Engine </li>
<li> a virtual reality environment where a user can see and interact with their plants and the data about them </li>

<p>Overall, This project is only a beginning of what could be accomplished.
There will be more updates to come making this project larger and able to be used by more people.
The next major update will come in the form of the user interface being able to work with Android via Google VR. 
</p>
<hr>



<h3 id="usage">Usage</h3>
<p> This documentation is for Windows users and there will be documentation later for Linux and Mac.
All software needed to compile and run the code will be easily done via the download links provided
</p>
<p></p>
<h4>Downloads</h4>
<b>Python 3.6 and PyCharm</b>
<p>To compile and run the server code, I recommend using PyCharm as your main IDE which can be downloaded <a href="https://www.jetbrains.com/pycharm/">here</a>.
From within the PyCharm IDE, it is very strait forward to configure it with Python 3.6. </p>
<b>Unity Editor</b>
<p>You can download the Unity Editor from this link <a href="https://unity3d.com/get-unity/download">here</a>.
There are several assets that will needed to be downloaded to make sure the application can run.
The first is the Graph And Chart Software published by Prousource Labs which can be found <a href="https://assetstore.unity.com/packages/tools/gui/graph-and-chart-78488">here</a>.
  The next asset needed to be downloaded is Lowpoly Flowers by Chlyang which is found <a href="https://assetstore.unity.com/packages/3d/vegetation/plants/lowpoly-flowers-47083">here</a>.
  The last one is the Curved VR Keyboard by Handcrafted VR which from <a href="https://assetstore.unity.com/packages/tools/input-management/curved-vr-keyboard-77177">here</a>

<b>Oculus Rift</b>
<p> There are several things that you will need to download to use the Oculus Rift and Edit the code.
Before you go to download the software to use the Oculus Rift, Follow this link to download the application that will check to see if your computer has the capabilities of running an Oculus Rift. <a href="https://ocul.us/compat-tool">compatability tool</a>
</p>
<p>If your computer is capable of handling the Oculus Rift, then download the Oculus drivers from <a href="https://www.oculus.com/download_app/?id=1582076955407037">here</a>.
You will also need the Oculus Utilities for Unity which can be downloaded from <a href="https://developer.oculus.com/downloads/package/oculus-utilities-for-unity-5/">here</a>
</p> 
  
<h4 id="compilation">Compilation</h4>
<p>
To run the code for the Particle Photon, go to <a href="build.particle.io/">build.particle.io</a> and either create an account or sign in. After, just copy and paste the Photon code into the online Editor and flash your photon which will update the firmware.
</p>
<p>
For the server code, just download the code from this repository and add it into the PyCharm IDE and press run.
</p>
<p>
For the User interface, download all the prefabs, scenes, and scripts included in this repository and put them in the right folders. Open the scene in the Unity editor and include all the assets that were downloaded. Make sure that all scriptws and Game objects are linked correctly and run the scene.
</p>
<hr>
  
<h3 id="about">About</h3>
<p>This project was written using the Particle web IDE, PyCharm, and the Unity Editor including MonoDevelop. Classes used were Adafruit_DHT.h and all assets downloaded from the Unity Asset Store.</p>
<p></p>
Languages include:
<li>C++ (for Arduino)</li>
<li>Python 3.6</li>
<li>SQL</li>
<li>C#</li>
<p>If you would like to use any of the code from this project, please annotate this as its origin.</p>
<p>Authored by <a href="https://www.linkedin.com/in/chase-bowlin/">Chase Bowlin</a></p>

