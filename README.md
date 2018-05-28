<h1>CROFT</h1>
<li>Customizable, Remote, Oculus Rift, Farming, Tool.</li>
<li>  <i>A tool that takes the busy work out of monitoring plants. Implements several sensors on a wifi capable development board, a server that is connected to a database, and a virtual reality user interface where users can interact with the data</i></li>
<h2>Contents</h2>
<a href="#abstract"> 1. Description</a><br>
<a href="#usage">2. Software Required for Use</a><br>
<a href="#compilation">3. Compilation</a><br>
<a href="#execution">4. Running the server</a><br>
<a href="#about">5. About</a><br>
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
<b>Oculus Rift</b>
<p> There are several things that you will need to download to use the Oculus Rift and Edit the code.
Before you go to download the software to use the Oculus Rift, Follow this link to download the application that will check to see if your computer has the capabilities of running an Oculus Rift. <a href="https://ocul.us/compat-tool">compatability tool</a>
</p>
<h4 id="compilation">Compilation</h4>

<h4 id="execution">Running the server</h4>
  
<h3 id="about">About</h3>
The following technologies compromise this project:
<li>C++</li>
<li>Cygwin</li>
<li>Ncurses</li>
