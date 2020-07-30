# WiFi Attendance System

WiFi Attendance System is a Python based web application that automatically detects when youre employees arrive, take breaks and leaves the office. This is a weekend project that hopefully would become widely used.

  - Python3 and Flask Based
  - Uses SQLite Database, you may use another as it uses SQLAlchemy
  - *NIX Systems Supported

# Scan Methods:

  - ARP Scan - Uses MAC Address, Listens to Devices on the Network
  - Ping - Uses IP Address, IPv4 is supported at the moment
  - Port Scan - Uses IP Address and Port, connects to the device on the specified port


# Installation

Install python3, python3-pip and python3-venv
```sh
$ sudo apt install python3`
$ sudo apt install python3-pip
$ sudo apt install python3-venv
```
Clone this Repository and Change Directory to it
```sh
$ git clone git@github.com:mimmi/wifi-attendance.git
$ cd wifi-attendance
```
Activate Python Virtual Environment
```sh
$ . venv/bin/activate
```
Install Dependencies
```sh
$ pip3 install -r requirements.txt
```
Initialize the Database
```sh
$ flask db init
$ flask db migrate -m "Installation"
$ flask db upgrade
```

# Run Development Server
You may use the flask development server to test out the Application before launching:
```sh
$ export FLASK_APP=main.py
$ flask run --host=0.0.0.0:5000
```

# Production

Check out the various deployment options for python flask applications: https://flask.palletsprojects.com/en/1.1.x/deploying/

# Todos

 - Completion of Scans
 - Support IPv6
 - Support Multiple VLAN's

License
----

MIT

**Free Software**
