#!/usr/bin/python3

from os import listdir, system, remove, rename
from colorsys import rgb_to_hls, hls_to_rgb
from shutil import copy2

def darken(code):
	rgb_hex = str(code).lower().strip()	
	# Split into r, g, and b whilst converting to decimal values
	r_var = int(list(rgb_hex)[0]+list(rgb_hex)[1], 16)/255.0
	g_var = int(list(rgb_hex)[2]+list(rgb_hex)[3], 16)/255.0
	b_var = int(list(rgb_hex)[4]+list(rgb_hex)[5], 16)/255.0	
	# Converts to hsl
	h_var = round(rgb_to_hls(r_var, g_var, b_var)[0]*255)
	l_var = round(rgb_to_hls(r_var, g_var, b_var)[1]*255)
	s_var = round(rgb_to_hls(r_var, g_var, b_var)[2]*255)	
	# Makes lighter code
	if l_var < 10:
		l2_var = 0
	else:
		l2_var = l_var-10	
	r2_var = round(hls_to_rgb(h_var/255.0, l2_var/255.0, s_var/255.0)[0]*255)
	g2_var = round(hls_to_rgb(h_var/255.0, l2_var/255.0, s_var/255.0)[1]*255)
	b2_var = round(hls_to_rgb(h_var/255.0, l2_var/255.0, s_var/255.0)[2]*255)	
	if len(hex(r2_var)[2:]) == 1:
		r_hex = "0"+hex(r2_var)[2:]
	else:
		r_hex = hex(r2_var)[2:]	
	if len(hex(g2_var)[2:]) == 1:
		g_hex = "0"+hex(g2_var)[2:]
	else:
		g_hex = hex(g2_var)[2:]	
	if len(hex(b2_var)[2:]) == 1:
		b_hex = "0"+hex(b2_var)[2:]
	else:
		b_hex = hex(b2_var)[2:]
	return r_hex+g_hex+b_hex # the lighter code

for symbol in listdir("symbols-android/")+listdir("symbols-desktop/"):
	print("Making "+symbol)
	now_sym = [line for line in open("symbols/"+symbol, 'r')]
	light_rgb = now_sym[0].split(" -->")[0].replace("<!-- color: #","")
	copy2("background.svg", "background.svg.tmp")
	f1 = open("background.svg.tmp", "r")
	f2 = open("/home/josh/Programs/Icons/Numix/script-o/input/templates/circle/background.svg", "w")
	for line in f1:
		f2.write(line.replace('color:#ffffff', 'color:#'+light_rgb).replace('color:#000000', 'color:#'+darken(light_rgb)))
	f1.close()
	f2.close()
	copy2("symbols/"+symbol, "input/symbols/"+symbol)
	system("./numix-kit -t circle")
	remove("input/symbols/"+symbol)