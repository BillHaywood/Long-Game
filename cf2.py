import tkinter
menu = 0
def adv1():
	global menu
	menu = 1
	print(menu)
	return menu
def adv2():
	global menu
	menu = 2
	print(menu)
	return menu
def adv3():
	global menu
	menu = 3
	print(menu)
	return menu
def adv4():
	global menu
	menu = 4
	print(menu)
	return menu
def adv5():
	global menu
	menu = 5
	print(menu)
	return menu
def adv6():
	global menu
	menu = 6
	print(menu)
	return menu
main = tkinter.Tk()
main.title("Menu")
while menu == 0:
	frame = tkinter.Frame(main)
	frame.pack()
	text = tkinter.Label(frame, text="""This is some text.
	Which is multiline
	And not too long, ideally
	
	
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac mi
	porttitor, ornare leo id, condimentum felis. Donec sodales justo
	enim, eget pellentesque massa lacinia quis. Proin iaculis nunc orci,
	et maximus leo molestie ac. Donec non bibendum massa. Donec iaculis
	vulputate cursus. In sodales luctus sagittis. Proin nisi arcu,
	mollis vel justo eu, pharetra euismod lectus. Cras finibus, sapien
	non faucibus eleifend, nisl arcu lobortis nisi, eget accumsan magna
	felis non purus. Nam libero sapien, convallis quis magna in,
	efficitur sagittis nisi. Vestibulum in tempor orci. Curabitur vel
	varius tellus. Curabitur lacinia ultrices nibh. Maecenas mollis eu
	nunc ac sollicitudin. In fermentum lorem orci, sed euismod arcu
	feugiat sed. Duis pellentesque est urna, et pellentesque massa
	scelerisque non. Proin tempor eros et imperdiet feugiat.
	
	In vel iaculis nunc. Praesent a pretium tellus. Aenean in elit
	congue, interdum turpis et, mattis nunc. In et turpis maximus,
	consectetur mauris vel, auctor augue. Maecenas consectetur blandit
	tortor, non sodales massa hendrerit a. Aliquam non dolor sed leo
	dapibus mollis. Nunc ultricies elit erat, in sollicitudin risus
	euismod a. Praesent sit amet interdum justo. Nulla feugiat laoreet
	urna. Maecenas quis aliquam metus.
	
	Morbi convallis ex magna, sit amet luctus dolor elementum eu. Nullam
	eu porta quam, sit amet tempor velit. Donec venenatis fringilla
	mollis. Morbi a vestibulum justo, vel dignissim nibh. Integer
	convallis sem id purus efficitur laoreet. Integer laoreet arcu sed
	nisi maximus dictum. Pellentesque euismod auctor urna a efficitur.
	Mauris ut tellus a nisi egestas rutrum ac in dolor. Pellentesque
	suscipit, ex vitae tincidunt commodo, nisi sapien malesuada felis,
	ut malesuada eros lorem ut neque. Morbi vehicula purus sit amet
	augue accumsan iaculis. Mauris eleifend est vel magna volutpat, nec
	hendrerit lectus dictum. Integer a tincidunt dolor. Fusce eget
	aliquet est, ac tincidunt magna.
	
	Proin lobortis justo massa, nec mollis mi commodo vel. Sed ante
	tortor, sollicitudin tristique auctor pretium, facilisis non turpis.
	Quisque condimentum vestibulum ante, ac pretium est pellentesque at.
	Suspendisse porta dictum odio, eget pulvinar turpis bibendum at.
	Nulla interdum, justo ac rutrum pretium, nisi tellus condimentum
	dui, et interdum ligula ligula a elit. Maecenas volutpat sapien
	arcu, vitae feugiat magna mollis quis. Aenean tincidunt ipsum magna,
	eget euismod purus tempor a. Vestibulum sit amet rhoncus ipsum. Nam
	aliquet tellus a risus elementum, eu ullamcorper sem sodales. Cras
	fermentum metus nec elit eleifend scelerisque. Phasellus nec ligula
	at lacus bibendum bibendum ut et justo. Cras scelerisque, mauris
	auctor sollicitudin interdum, leo metus commodo metus, bibendum
	bibendum eros nulla efficitur velit. Aenean at nibh at dui interdum
	aliquet ac et metus. In aliquam eleifend dignissim. Ut sem dui,
	fringilla viverra faucibus auctor, porttitor sed felis. Vestibulum
	maximus facilisis rhoncus.
	
	Vestibulum auctor vel diam et convallis. Duis id sapien ac neque
	venenatis faucibus et a nisl. Ut condimentum risus eu dolor lacinia,
	in finibus est facilisis. Phasellus vel odio ornare, commodo tortor
	eget, placerat velit. Fusce ullamcorper imperdiet sagittis. Morbi
	varius metus in lacus consectetur porttitor. Duis facilisis molestie
	est a gravida. Suspendisse ullamcorper porta lobortis. Aliquam nec
	iaculis elit.
	""")
	text.pack()
	button0 = tkinter.Button(frame, text="Continue", width=25, command= frame.destroy)
	button0.pack(side = 'bottom')
	button1 = tkinter.Button(frame, text='One', width=25, command=adv1)
	button1.pack(side = 'left')
	button2 = tkinter.Button(frame, text='Two', width=25, command=adv2)
	button2.pack(side = 'right')
	break
while menu == 1:
	frame2 = tkinter.Frame(main)
	frame2.pack()
	button0 = tkinter.Button(frame2, text="Continue", width=25, command=frame2.destroy)
	button0.pack(side = 'bottom')
	button1 = tkinter.Button(frame2, text='Three', width=25, command=adv3)
	button1.pack(side = 'left')
	button2 = tkinter.Button(frame2, text='Four', width=25, command=adv4)
	button2.pack(side = 'left')
	break
while menu == 2:
	frame3 = tkinter.Frame(main)
	frame3.pack()
	button0 = tkinter.Button(frame3, text="Continue", width=25, command=frame3.destroy)
	button0.pack(side = 'bottom')
	button1 = tkinter.Button(frame3, text='Five', width=25, command=adv5)
	button1.pack(side = 'left')
	button2 = tkinter.Button(frame3, text='Six', width=25, command=adv6)
	button2.pack(side = 'left')
	break
main.mainloop()
