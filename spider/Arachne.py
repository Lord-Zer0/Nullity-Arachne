# Arachne.py
# ======================================================================================================================
# Project Arachne. Main python script.
# (c) Nullity Corp, 2017
# version 1.0.0
# path: ./spider/Arachne.py
# repo link: git@github.com:Lord-Zer0/Nullity-Arachne.git
# last edit: 11/02/2017
# edited by: Connor McCauley (git:Lord-zer0)
# see README.md for further Documentation, contributions, FAQ
# ======================================================================================================================
# ======================================================================================================================

# BASE SETUP
# ======================================================================================================================

# import needed resources
from socket import *
import statistics
import numpy as np
import matplotlib.pyplot as plt
import time

# define network connection
TCP_PORT = 8080                 # define default port using TCP
TIMEOUT = 10                    # set to timeout after 5 seconds
TEST_IP = ''                    # set localhost for testing

# standard message
msg = "Hello World!"

# SOCKETS FOR WEB CRAWLER
# ======================================================================================================================

# create TCP client socket. SOCK_STREAM is used here.
nativeSocket = socket(AF_INET, SOCK_STREAM)
# set timeout to default
nativeSocket.timeout(TIMEOUT)

# GET REQUESTS
# ======================================================================================================================
def spiderget():
    nativeSocket.send(msg.encode())
