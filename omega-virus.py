#!/usr/bin/python

'''
# Insert docopt user help menu here?

# Good resource for game mechanics w/o having to get game manual :D
# https://boardgamegeek.com/thread/372462/omega-virus-human-scum-review

# End docopt
''''

# Lets define some imports! :D
import random
from random import randint

def difficulty()
	# Define the length of the game (these values are probably wrong :D Need to check rulebook.
	# 0 - 30 Minutes
	# 1 - 20 Minutes
	# 2 - 15 Minutes
	;
	
def numPlayers()
	# In the orginal game, the Computer asks each player to enter their secret code at the beginning of the game.
	# This then defines which colors are active. There may be a simpler way of doing this though...
	;
def sectors()
	# Docking Bays (Blue, Green, Red, Yellow)
	# Blue Rooms
	# Green Rooms
	# Red Rooms
	# Yellow Rooms
	# When 9 minutes are left one sector is shut down, and every 3 minutes after this another is shut down.
	
def roomList()
	# Docking Bays (Blue, Green, Red, Yellow)
	# List of rooms
	# Green (open rooms)
	# Blue (requires blue key)
	# Red (requires red key)
	# Yellow (requires yellow key)

def roomContents()
	# Each room can have one of:
	# 1. An ADV
	# 2. An access card
	# 3. A Probe (more on this in a little bit)
	# 4. A hazard
	# 5. The virus (presumably chilling out)
	# 6. Nothing at all

def items()
	# Four of each, to be distributed across the map.
	# Access keys (Blue, Red, Yellow)
	# Decoder - yellow
	# Disruptor - blue
	# Negatron - red
	# Probe
	
def playerBag()
	# A place to define inventory. 
	def bluePlayer()
		blueKey = boolean
		redKey = boolean
		yellowKey = boolean
		blueProbe = boolean
		decoder = boolean
		disruptor = boolean
		negatron = boolean
	# Green
	# Red
	# Yellow
	;
def probes()
	# Probes can move, explore and be attacked just like players. However they cannot attack themselves.
	# Blue
	# Green
	# Red
	# Yellow
	
def rng()
	# Random number generator ranging from 0-2
	rng = randint(0,2)
	
def secretCode()
	# Secret codes let players know where the virus is provided:
	#	a) They enter a room where the virus is
	#	b) They do not have all three weapons
	#	c) Should we let probes find the virus?
	
def userInput()
	# We will need a way for players to input numbers (0,1,2)
	# This is for room numbers, secret codes, and combat
	blueCode = stdin
	greenCode = stdin
	redCode = stdin
	yellowCode = stdin
	
def combat()
	# Combat includes, players attacking one another (or their drones) as well as attaking the virus. 
	# Defender picks a value (0,1 or 2), and the Attacker picks one as well.
	# If both match, then the attacker wins. I.e. the Virus is killed, the player looses an item (at random),
	# or the drone dies.
	
def phrasing()
	# This is a placeholder for all of the phrases that are used throuout the game.
	# --Virus--
	# "You Human Scum!"
	# "Which room?"
	# "Help me! Help me!" (Mockingly)
	# "Blue Sector, Shut Down."
	# "Green Sector, Shut Down."
	# "Red Sector, Shut Down."
	# "Yellow Sector, Shut Down."
	# "You have [time] minutes until -I- take over!"
	# "Mwahahaha!"
	# "You missed!"
	# "You killed me! You, human... scum."
	# "I win!"
	# "[player_color] is attacking [player_color] hahaha"
	# "[player_color] is attacking [player_color] done how amusing"
	#
	# --Computer--
	# "[player_color] enter secret code"
	# "[player_color] help me"
