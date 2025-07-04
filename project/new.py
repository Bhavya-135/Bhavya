import  tkinter as tk 
r=tk.Tk()

r.title('Vignan Bio Tech')
button=tk.Button(r,text="Bio Tech",width=50 ,command=r.destroy)
button.pack()

button =tk.Button(r,text="registration number",width=50,command=r.destroy)
button.pack()


button =tk.Button(r,text="enter",width=50,command=r.destroy)
button.pack() 
r.mainloop()

#it used to draw picriures "canvas"
#"check buttons" is used for multiple options checking
#"entry button" it is used the single line text entry from the userr for multiple thingss
