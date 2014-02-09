import pygame, sys
from pygame.locals import *
from random import choice

####################
#########
######### Evalua si el jugador 1 = computadora o 2 = humano
######### gano o perdio usando las todas las convinaciones posibles
#########
##########################################################33
def check_move(num, mat):

	diagonal1 = [[0, 2], [1, 1], [2, 0]]
	diagonal2 = [[0, 0], [1, 1], [2, 2]]

	horiz1    = [[0, 0], [0, 1], [0, 2]] 
	horiz2 	  = [[1, 0], [1, 1], [1, 2]]
	horiz3 	  = [[2, 0], [2, 1], [2, 2]]

	verti1    = [[0, 0], [1, 0], [2, 0]]
	verti2 	  = [[0, 1], [1, 1], [2, 1]]
	verti3 	  = [[0, 2], [1, 2], [2, 2]]

	if mat[diagonal1[0][0]][diagonal1[0][1]] == num and mat[diagonal1[1][0]][diagonal1[1][1]] == num and mat[diagonal1[2][0]][diagonal1[2][1]] == num:
		return True
	elif mat[diagonal2[0][0]][diagonal2[0][1]] == num and mat[diagonal2[1][0]][diagonal2[1][1]] == num and mat[diagonal2[2][0]][diagonal1[2][1]] == num:
		return True
	elif mat[horiz1[0][0]][horiz1[0][1]] == num and mat[horiz1[1][0]][horiz1[1][1]] == num and mat[horiz1[2][0]][horiz1[2][1]] == num:
		return True
	elif mat[horiz2[0][0]][horiz2[0][1]] == num and mat[horiz2[1][0]][horiz2[1][1]] == num and mat[horiz2[2][0]][horiz2[2][1]] == num:
		return True
	elif mat[horiz3[0][0]][horiz3[0][1]] == num and mat[horiz3[1][0]][horiz3[1][1]] == num and mat[horiz3[2][0]][horiz3[2][1]] == num:
		return True
	elif mat[verti1[0][0]][verti1[0][1]] == num and mat[verti1[1][0]][verti1[1][1]] == num and mat[verti1[2][0]][verti1[2][1]] == num:
		return True
	elif mat[verti2[0][0]][verti2[0][1]] == num and mat[verti2[1][0]][verti2[1][1]] == num and mat[verti2[2][0]][verti2[2][1]] == num:
		return True
	elif mat[verti3[0][0]][verti3[0][1]] == num and mat[verti3[1][0]][verti3[1][1]] == num and mat[verti3[2][0]][verti3[2][1]] == num:
		return True
	else:
		return False

## Inicializacion de las librerias ##
pygame.init()
## FPS del programa ##
fps = pygame.time.Clock()

## Tamanioo de la ventana
height = 600
width  = 600
bloque_largo = height / 3 ## Ancho ##
bloque_ancho = width / 3 ## largo ##
size = height, width + 50
ventana = pygame.display.set_mode(size)

## coordenadas iniciales ##
mouse_x, mouse_y = 0, 0

## Colores ##
blanco =   pygame.Color(255, 255, 255)
negro  =   pygame.Color(0, 0, 0)
rojo   =   pygame.Color(255, 0, 0)
azul   =   pygame.Color(0, 0, 255)

#####################################
######## Elementos Juego  ###########
#####################################

turno_jugador = True
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] ## -0 vacio, 1 computadora, 2 jugador

######################################

while True:
	## Fondo de Ventana ##
	ventana.fill(blanco)

	###########################################################
	###########################################################
	##########  										#######
	##########         DIBUJO DE LOS ELEMENTOS 			#######  
	##########											#######
	###########################################################
	###########################################################

	stroke = 5 ## grosor ##

	## Lineas Verticales ##	
	pygame.draw.line(ventana, negro, (bloque_largo, 0), (bloque_largo, width), stroke) ## 1ra linea ##
	pygame.draw.line(ventana, negro, (bloque_largo * 2, 0), (bloque_largo * 2, width), stroke) ## 2da linea ##

	## Lineas Horizontales ##	
	pygame.draw.line(ventana, negro, (0, bloque_ancho), (height, bloque_ancho), stroke) ## 3ra linea
	pygame.draw.line(ventana, negro, (0, bloque_ancho * 2), (height, bloque_ancho * 2), stroke) ## 4ta linea

	###########################
	##### Dibujar X o O #######
	###########################
	for fila in range(3):
		for columna in range(3):
			if matriz[fila][columna] != 0:
				x = 0
				y = 0				
				###########################
				if columna == 0:
					y = 0
					y_fin = bloque_largo - 1
				elif columna == 1:
					y = bloque_largo
					y_fin = bloque_largo * 2 - 1
				elif columna == 2:
					y = bloque_largo * 2
					y_fin = width
				###########################
				if fila == 0:
					x = 0
					x_fin = bloque_ancho - 1
				elif fila == 1:
					x = bloque_ancho
					x_fin = bloque_ancho * 2 - 1
				elif fila == 2:
					x = bloque_ancho * 2
					x_fin = height
				###########################
				imagen = ''

				if matriz[fila][columna] == 2:
					imagen = pygame.image.load('firefox_mod.png')
				else:
					imagen = pygame.image.load('google_mod.png')

				x = ((x + x_fin) - imagen.get_height()) / 2
				y = ((y + y_fin) - imagen.get_width()) / 2

				ventana.blit(imagen, (x, y))


	############ Mueve CPU ################
	if turno_jugador == False:
		movs = []
		for i in range(3):
			for j in range(3):
				if matriz[i][j] == 0:
					movs.append([i, j])				
		if len(movs) > 0:
			x, y = choice(movs)
			matriz[x][y] = 1
			if(check_move(1, matriz)):
				print "Perdiste"
			turno_jugador = True
		else:
			matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]			
			turno_jugador = True
			print "empate"

	############################################################
	############################################################
	#############             EVENTOS           ################
	############################################################
	############################################################
	for event in pygame.event.get():
		if event.type == QUIT: ## Evento de salida ##
			pygame.quit() ## Cerrar librerias ##
			sys.exit()	  ## Cerrar aplicacion 	
		elif event.type == MOUSEBUTTONUP: ## Presion de un boton del mouse ##
			if event.button in (1, 3) and turno_jugador == True: ## Presion del boton izquierdo o derecho del mouse ##
				mouse_x, mouse_y = event.pos ## Coordenadas del mouse ##
				vector_x = -1
				vector_y = -1
				## Coordennadas en X ##
				if mouse_x in range(0, bloque_largo):
					vector_x = 0
				elif mouse_x in range(bloque_largo, bloque_largo * 2):
					vector_x = 1
				elif mouse_x in range(bloque_largo * 2, height + 1):
					vector_x = 2

				## Coordenadas en Y ##
				if mouse_y in range(0, bloque_ancho):
					vector_y = 0
				elif mouse_y in range(bloque_ancho, bloque_ancho * 2):
					vector_y = 1
				elif mouse_y in range(bloque_ancho * 2, width + 1):
					vector_y = 2
				if  matriz[vector_x][vector_y] == 0:
					matriz[vector_x][vector_y] = 2 ## se crea el movimiento
					if(check_move(2, matriz)):
						print "Ganaste";
					turno_jugador = False
					#print matriz ## Depuracion

		elif event.type == KEYDOWN: ## Envento de tecla presionada ##
			if event.key == K_ESCAPE: ## Tecla ESC presionada ##
				pygame.event.post(pygame.event.Event(QUIT)) ## Salir ##


	##### Actualizacion del panel ######
	pygame.display.update() ## Actualiza la ventana ##
	fps.tick(30) ## Espera, para que corra a 30 fps ##
