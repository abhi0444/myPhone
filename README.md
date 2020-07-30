# myPhone (Currently client needs some changes to have it running) #

An alternative to Your Phone. (myPhone is still in very initial development stage)

## Purpose ##
<p>This app is focused on P2P sharing between two devices(mainly pc and a phone). It aims at providing an easy and faster data transfer. </p>

## Features ##
* File transfer and sharing.
* Faster and easy to use.
* Android to linux based pc tranfer.(to be included)
* Safe and reliable.(after implementation of authentication system)

## Scope ##
  * Android app for file transfering and sharing.
  * GUI for linux.
  * Achieving higher transfer speeds.
  * May include a windows app.
  * Password and Security.

## Built with ##
  * Python(for networking). 
  * HTML,CSS and Javascript(GUI development).
  * Kotlin and java (Android App). (To be done)
  
## Installation ##
 * Clone the repo.
     ```sh
    git clone https://github.com/taru-garg/myPhone.git
    ```
 * Open the repo.
 
   *   #### **Server side** ####
         ```sh
         cd server
         pip install -r requirements_server.txt
         cd ..
         ```
    *  #### **Client side** ####
          ```sh
          cd client
          pip install -r requirements_client.txt
          cd ..
          ```
## Running the app ##
 
 * **Server**
   ```sh
   cd server
   python myPhone_server.py
   ```
  * **Client**
    ```sh
    cd client
    python myPhone_client.py
    ```
