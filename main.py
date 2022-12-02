# Minecraft Server Creator v1.2 It's very easy to create a server for playing on macOS!
# Author: Kunitsa Bogdan
# Instagram: https://www.instagram.com/wwxriyy
# Telegram: https://t.me/wwwrixy
# Date 2.12.2022

# Libraries:
# pip3 install requests
# pip3 install PyQt5
# Version Python 3.11

import sys
import os
import requests
import craftbukkits
from PyQt5.QtWidgets import QLabel, QTextEdit, QMainWindow, QApplication, QPushButton, QComboBox
from PyQt5.QtGui import QIcon
from requests import get

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # App
        self.setWindowTitle("MCServer Creator v1.2")
        self.setGeometry(0, 0, 600, 350)

        # QLabel
        self.label = QLabel('Server name:', self)
        self.label.move(10, 10)
        self.label.adjustSize()
        # QTextEdit
        self.server_name = QTextEdit(self)
        self.server_name.move(10, 30)
        self.server_name.setFixedSize(150, 26)
        # QLabel
        self.label2 = QLabel('Server ip adress:\nIf skipped, the Ip4 address will be taken automatically.', self)
        self.label2.move(10, 60)
        self.label2.adjustSize()
        # QTextEdit
        self.server_ip = QTextEdit(self)
        self.server_ip.move(10, 95)
        self.server_ip.setFixedSize(150, 26)
        # QLabel
        self.label3 = QLabel('Server port:\nIf skipped, the port will be taken automatically (25565)', self)
        self.label3.move(10, 124)
        self.label3.adjustSize()
        # QTextEdit
        self.server_port = QTextEdit(self)
        self.server_port.move(10, 160)
        self.server_port.setFixedSize(150, 26)
        self.server_port.setText('25565')
        # QLabel
        self.label6 = QLabel('Server maximum players:', self)
        self.label6.move(10, 190)
        self.label6.adjustSize()
        # QTextEdit
        self.server_max_players = QTextEdit(self)
        self.server_max_players.move(10, 210)
        self.server_max_players.setFixedSize(150, 26)
        self.server_max_players.setText('100')
        # QLabel
        self.label7 = QLabel("Path to server folder:", self)
        self.label7.move(10, 240)
        self.label7.adjustSize()
        # QTextEdit
        self.server_path = QTextEdit('MyServer', self)
        self.server_path.move(10, 260)
        self.server_path.setFixedSize(580, 26)
        # QLabel
        self.label4 = QLabel('Server version:', self)
        self.label4.move(360, 10)
        self.label4.adjustSize()
        # QComboBox
        craftbukkit_image = QIcon('images/craftbukkit.png')
        self.server_version = QComboBox(self)
        self.server_version.addItem(craftbukkit_image, '1.19.2')
        self.server_version.addItem(craftbukkit_image, '1.19')
        self.server_version.addItem(craftbukkit_image, '1.18.2')
        self.server_version.addItem(craftbukkit_image, '1.18.1')
        self.server_version.addItem(craftbukkit_image, '1.18')
        self.server_version.addItem(craftbukkit_image, '1.17.1')
        self.server_version.addItem(craftbukkit_image, '1.17')
        self.server_version.addItem(craftbukkit_image, '1.16.5')
        self.server_version.setGeometry(353, 30, 164, 26)
        # QLabel
        self.label5 = QLabel('Server difficulty:', self)
        self.label5.move(360, 60)
        self.label5.adjustSize()
        # QComboBox
        self.server_difficulty = QComboBox(self)
        self.server_difficulty.addItems(['Peaceful', 'Easy', 'Normal', 'Hard'])
        self.server_difficulty.setGeometry(353, 80, 164, 26)
        # QLabel
        self.label8 = QLabel('Server access:', self)
        self.label8.move(360, 105)
        self.label8.adjustSize()
        # QComboBox
        self.server_access = QComboBox(self)
        self.server_access.addItems(['License', 'Pirate'])
        self.server_access.setGeometry(353, 125, 164, 26)

        # QPushButton (Create server)
        self.create_server_button = QPushButton('Create server', self)
        self.create_server_button.move(470, 315)
        self.create_server_button.setFixedSize(130, 26)
        self.create_server_button.clicked.connect(self.create_server)

        # QLabel (Status)
        self.status_label = QLabel('Status: null', self)
        self.status_label.move(10, 290)
        self.status_label.adjustSize()

        # QLabel (Info)
        self.info_label = QLabel('Software creator Kunitsa Bogdan\nInstagram: @wwxriyy Telegram: @wwwrixy', self)
        self.info_label.move(10, 310)
        self.info_label.adjustSize()

        # Show all wigets
        self.show()

    # Function for QPushButton (Create server)
    def create_server(self):
        # Creating server
        server_name = self.server_name.toPlainText()
        server_version = self.server_version.currentText()
        server_ip = self.server_ip.toPlainText()
        server_port = self.server_port.toPlainText()
        server_difficulty = self.server_difficulty.currentText()
        server_max_players = self.server_max_players.toPlainText()
        server_path = self.server_path.toPlainText()
        server_access = self.server_access.currentText()

        # Create folder for user path
        os.mkdir(str(server_path))

        # If server ip = null
        if server_ip == "":
            try:
             server_ip = get('https://api.ipify.org').text
             print("[Log] Server automatically selected ip address: " + str(server_ip))
             self.status_label.setText('Status: Automatically selected ip address: ' + str(server_ip))
             self.status_label.adjustSize()
            except:
                print("[Log] Error connection. No network!")
                self.status_label.setText('Status: Error connection. No network!')
                self.status_label.adjustSize()
        else:
            print("[Log] Server ip address: " + str(server_ip))

        # If server port = null
        if server_port == "":
            server_port = "25565"
            print("[Log] Server automatically selected port: " + str(server_port))
            self.status_label.setText('Status: Automatically selected port: ' + str(server_port))
            self.status_label.adjustSize()
        else:
            print("[Log] Server port: " + str(server_port))
        # If server access license or pirate
        if server_access == "License":
            online_mod = "true"
        else:
            online_mod = "false"

        print("[Log] Server name: " + str(server_name))
        print("[Log] Server version: " + str(server_version))
        print("[Log] Server difficulty: " + str(server_difficulty))
        print("[Log] Server maximum players: " + str(server_max_players))
        print("[Log] Server access: " + str(server_access))
        print("[Log] Server path: " + str(server_path))

        # Write log file
        log_file = open(str(server_path) + '/logs.txt', 'w')
        log_file.write("[Log] Server name: " + str(server_name) + "\n[Log] Server version: " + str(server_version) + "\n[Log] Server difficulty: " + str(server_difficulty) + "\n[Log] Server maximum players: " + str(server_max_players) + "\n[Log] Server port: " + str(server_port) + "\n[Log] Server ip adress: " + str(server_ip) + "\n[Log] Server access: " + str(server_access) + "\n[Log] Server path: " + str(server_path))

        # Create server.properties file
        server_properties_file = open(str(server_path) + '/server.properties', 'w')
        server_properties_file.write("motd=" + str(server_name) + "\nserver-ip=" + str(server_ip) + "\ndifficulty=" + str(server_difficulty) + "\nmax-players=" + str(server_max_players) + "\nserver-port=" + str(server_port))
        server_properties_file.close()

        # Create eula file
        server_eula_file = open(str(server_path) + '/eula.txt', 'w')
        server_eula_file.write("eula=true")
        server_eula_file.close()

        # Download craftbukkits
        if server_version == "1.19.2":
            r = requests.get(craftbukkits.CRAFTBUKKIT1_19_2, allow_redirects=True)
            open(str(server_path) + '/craftbukkit1_19_2.jar', 'wb').write(r.content)
            server_starter_command = open(str(server_path) + '/ServerStarter.command', 'w')
            server_starter_command.write('#!/bin/bash\ncd "$(dirname "$0")"\njava -Xmx3000M -Xms3000M -jar craftbukkit1_19_2.jar nogui')
            server_starter_command.close()

        elif server_version == "1.19":
            r = requests.get(craftbukkits.CRAFTBUKKIT1_19, allow_redirects=True)
            open(str(server_path) + '/craftbukkit1_19.jar', 'wb').write(r.content)
            server_starter_command = open(str(server_path) + '/ServerStarter.command', 'w')
            server_starter_command.write('#!/bin/bash\ncd "$(dirname "$0")"\njava -Xmx3000M -Xms3000M -jar craftbukkit1_19.jar nogui')
            server_starter_command.close()

        elif server_version == "1.18.2":
            r = requests.get(craftbukkits.CRAFTBUKKIT1_18_2, allow_redirects=True)
            open(str(server_path) + '/craftbukkit1_18_2.jar', 'wb').write(r.content)
            server_starter_command = open(str(server_path) + '/ServerStarter.command', 'w')
            server_starter_command.write('#!/bin/bash\ncd "$(dirname "$0")"\njava -Xmx3000M -Xms3000M -jar craftbukkit1_18_2.jar nogui')
            server_starter_command.close()

        elif server_version == "1.18.1":
            r = requests.get(craftbukkits.CRAFTBUKKIT1_18_1, allow_redirects=True)
            open(str(server_path) + '/craftbukkit1_18_1.jar', 'wb').write(r.content)
            server_starter_command = open(str(server_path) + '/ServerStarter.command', 'w')
            server_starter_command.write('#!/bin/bash\ncd "$(dirname "$0")"\njava -Xmx3000M -Xms3000M -jar craftbukkit1_18_1.jar nogui')
            server_starter_command.close()

        elif server_version == "1.18":
            r = requests.get(craftbukkits.CRAFTBUKKIT1_18, allow_redirects=True)
            open(str(server_path) + '/craftbukkit1_18.jar', 'wb').write(r.content)
            server_starter_command = open(str(server_path) + '/ServerStarter.command', 'w')
            server_starter_command.write('#!/bin/bash\ncd "$(dirname "$0")"\njava -Xmx3000M -Xms3000M -jar craftbukkit1_18.jar nogui')
            server_starter_command.close()

        elif server_version == "1.17.1":
            r = requests.get(craftbukkits.CRAFTBUKKIT1_17_1, allow_redirects=True)
            open(str(server_path) + '/craftbukkit1_17_1.jar', 'wb').write(r.content)
            server_starter_command = open(str(server_path) + '/ServerStarter.command', 'w')
            server_starter_command.write('#!/bin/bash\ncd "$(dirname "$0")"\njava -Xmx3000M -Xms3000M -jar craftbukkit1_17_1.jar nogui')
            server_starter_command.close()

        elif server_version == "1.17":
            r = requests.get(craftbukkits.CRAFTBUKKIT1_17, allow_redirects=True)
            open(str(server_path) + '/craftbukkit1_17.jar', 'wb').write(r.content)
            server_starter_command = open(str(server_path) + '/ServerStarter.command', 'w')
            server_starter_command.write('#!/bin/bash\ncd "$(dirname "$0")"\njava -Xmx3000M -Xms3000M -jar craftbukkit1_17.jar nogui')
            server_starter_command.close()

        elif server_version == "1.16.5":
            r = requests.get(craftbukkits.CRAFTBUKKIT1_16_5, allow_redirects=True)
            open(str(server_path) + '/craftbukkit1_16_5.jar', 'wb').write(r.content)
            server_starter_command = open(str(server_path) + '/ServerStarter.command', 'w')
            server_starter_command.write('#!/bin/bash\ncd "$(dirname "$0")"\njava -Xmx3000M -Xms3000M -jar craftbukkit1_16_5.jar nogui')
            server_starter_command.close()

        self.status_label.setText("Status: Server created! Open: " + str(server_path))
        self.status_label.adjustSize()

# Run application
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())