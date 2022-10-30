# AirBnB clone - The console

<p align= "center">
<img src= https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221026%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221026T123011Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=07c2ba8525066a5f354d935b155e1015acf74be6fe53dfc6faedc1e124281562>
</p>

This project is the first step towards building a full web application: the AirBnB clone.

The console or command interpreter create the data model and allows create, update, destroy, store and persist objects to a file (JSON file). This console will be a tool to validate this storage engine.

<h2>Table of Contents</h2>

<li>Objectives<li>
<li>Requirements<li>
<li>Installation and execution<li>
<li>Console commands<li>
<li>Tests<li>
<li>Development enviroment<li>
<li>Authors<li>

<h2>Objectives</h2>

<li>How to create a Python package<li>
<li>How to create a command interpreter in Python using the cmd module<li>
<li>What is Unit testing and how to implement it in a large project<li>
<li>How to serialize and deserialize a Class<li>
<li>How to write and read a JSON file<li>
<li>How to manage datetime<li>
<li>What is an UUID<li>
<li>What is args and how to use it<li>
<li>What is kwargs and how to use it <li>
<li>How to handle named arguments in a function<li>

<h2>Requeriments 📋</h2>
Airbnb was built and tested in Ubuntu 14.04 LTS via Vagrant in VirtualBox. Programming languaje python3

<h2>Installation and execution 🔧</h2>
<li>Clone the repository
$ git clone https://github.com/MasikaII/AirBnB_clone

<h2>Console commands</h2>

<h1>The commands available for this command interpreter are:
Name	Description
*create	Creates a new instance of the class passed by argument.
show	Prints the string representation of an instance.
*destroy	Deletes an instance that was already created.
all	Prints string representation of all instances or of all instances of a specified class.
*update	Updates an instance attribute if exists otherwise create it.
help	Show all commands or display information about a specific command.
quit	Exit the console.
EOF	Exit the console.

<h2>TESTS ⚙️</h2>

<h2>Interactive Mode ⌨️</h2>
<h1>Example 1: Using create, count and all commands</h1>

solid@DESKTOP-6PPFSAT:~/H/AirBnB_clone$ ./console.py
(hbnb) all
[]
(hbnb) create Place
492f60f3-ff1e-43c7-bb11-f8407b04dd59
(hbnb) create BaseModel
99f01e9a-99c0-42af-8c10-c35cadee1d8f
(hbnb) BaseModel.count()
1
(hbnb) all
["[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530)}", "[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236)}"]
(hbnb)

<hi>Example 2: Using basic update with an Id and show command</h1>

(hbnb) update BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f first_name "Betty"
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236), 'first_name': 'Betty'}
(hbnb) Place.update("492f60f3-ff1e-43c7-bb11-f8407b04dd59", "first_name", "John")
(hbnb) show Place 492f60f3-ff1e-43c7-bb11-f8407b04dd59
[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530), 'first_name': 'John'}

<h1>Example 3: Using update with a dictionary</h2>

(hbnb) BaseModel.update("99f01e9a-99c0-42af-8c10-c35cadee1d8f", {'first_name': "Petter", "age": 45})
(hbnb) show BaseModel 99f01e9a-99c0-42af-8c10-c35cadee1d8f
[BaseModel] (99f01e9a-99c0-42af-8c10-c35cadee1d8f) {'id': '99f01e9a-99c0-42af-8c10-c35cadee1d8f', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773211), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 30, 773236), 'first_name': 'Petter', 'age': '45'}

<h1>Example 4: Using destroy and count command</h1>

(hbnb) BaseModel.destroy("99f01e9a-99c0-42af-8c10-c35cadee1d8f")
(hbnb) all
["[Place] (492f60f3-ff1e-43c7-bb11-f8407b04dd59) {'id': '492f60f3-ff1e-43c7-bb11-f8407b04dd59', 'created_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576486), 'updated_at': datetime.datetime(2020, 7, 1, 11, 36, 24, 576530), 'first_name': 'John'}"]
(hbnb) BaseModel.count()
0
(hbnb) quit
solid@DESKTOP-6PPFSAT:~/H/AirBnB_clone$

<h1>Non - Interactive Mode ⌨️</h1>

solid@DESKTOP-6PPFSAT:~/H/AirBnB_clone$ echo "create User" | ./console.py
(hbnb) 55b76419-6009-4b36-b88a-7c2930283f4a
solid@DESKTOP-6PPFSAT:~/H/AirBnB_clone$ echo "show User 55b76419-6009-4b36-b88a-7c2930283f4a" | ./console.py
(hbnb) [User] (55b76419-6009-4b36-b88a-7c2930283f4a) {'id': '55b76419-6009-4b36-b88a-7c2930283f4a', 'created_at': datetime.datetime(2020, 7, 1, 12, 37, 15, 575191), 'updated_at': datetime.datetime(2020, 7, 1, 12, 37, 15, 575237)}

<h2>Development environment 🛠️</h2>
<h1>This project has been tested on Ubuntu 14.06.6 LTS</h1>
<li>Programming languaje Python</li>
<li>The tests are carried out in virtualBox</li>
<li>Development environment manager vagrant</li>
<li>Style guidelines: PEP 8 (version 1.7) || Google Style Python Docstrings</li>

<h2>AUTHORS</h2>

<li>Erick adikah</li> https://github.com/Erickadikah
<li>Stephanie Masika</li> https://github.com/MasikaII/AirBnB_clone
