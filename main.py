from tkinter import *
import tkinter.messagebox

class BMI:

    def __init__(self, root):
        self.root = root
        self.root.title("Body Mass Index(BMI)")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='Gray')

        #==================== Main_frame, Right_frame and Left_frame =================================

        MainFrame = Frame(self.root, bd=20, width=1350, height=700, padx=10, pady=10, bg="Gray", relief=RIDGE)
        MainFrame.grid() #It organizes the widgets in grid (table-like structure) before placing in the parent widget.

        LeftFrame = Frame(MainFrame, bd=10, width=600, height=600, padx=10, pady=13, bg="red", relief=RIDGE)
        LeftFrame.pack(side=LEFT)  #pack() = It organizes the widgets in blocks before placing in the parent widge.

        RightFrame = Frame(MainFrame, bd=10, width=560, height=600, padx=10, pady=10, bg="yellow", relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        #================================ Child_of_Left_Frame ===============================================
        LeftFrame_0 = Frame(LeftFrame, bd=5, width=712, height=143, padx=5, bg="sky blue", relief=RIDGE)
        LeftFrame_0.grid(row=0, column=0)

        LeftFrame_1 = Frame(LeftFrame, bd=5, width=712, height=170, padx=5, pady=5, relief=RIDGE)
        LeftFrame_1.grid(row=4, column=0)

        LeftFrame_2 = Frame(LeftFrame, bd=5, width=712, height=168, padx=5, pady=6, relief=RIDGE)
        LeftFrame_2.grid(row=2, column=0)

        LeftFrame_3 = Frame(LeftFrame, bd=5, width=712, height=95, padx=5, pady=5, relief=RIDGE)
        LeftFrame_3.grid(row=3, column=0)

        #================================= Child_of_Right_Frame =================================================
        RightFrame_0 = Frame(RightFrame, bd=5, width= 522, height=200, padx=5, pady=2, relief=RIDGE)
        RightFrame_0.grid(row=0, column=0)

        RightFrame_1 = Frame(RightFrame, bd=5, width=522, height=280, padx=5, relief=RIDGE)
        RightFrame_1.grid(row=1, column=0)

        RightFrame_2 = Frame(RightFrame, bd=5, width=522, height=95, padx=5, pady=2, bg="Gray",relief=RIDGE)
        RightFrame_2.grid(row=2, column=0)

        #==================================Declaring Variable=================================================

        var1 = StringVar()
        var2 = StringVar()
        var3 = DoubleVar()
        var4 = DoubleVar()
        #===========================================  Button Coding =================================================

        def BMI_Cal():   #Calculate BMI
            P_height = (var1.get())
            P_weight = (var2.get())

            self.txtBMIResult.delete("1.0",END)
            if P_height.isdigit() or P_weight.isdigit(): #string_name.isdigit() method returns True if all the characters are digits, otherwise False.
                P_height = float(P_height) #type casting convert in float
                P_weight = float(P_weight)
                BMI = float('%.2f'%(P_weight / (P_height * P_height))) #Formula of BMI
                self.txtBMIResult.insert(END,BMI) #Display on txtBMIResult box
                var3.set(P_height)
                var4.set(P_weight)
                return True
            else:
                tkinter.messagebox.showwarning("Body Mass Index(BMI)","Please enter a valid number")
                var1.set("")
                var2.set("")
                var3.set(0)
                var4.set(0)
                self.txtBMIResult.delete("1.0", END)

        def Reset():
            var1.set("")
            var2.set("")
            var3.set(0)
            var4.set(0)
            self.txtBMIResult.delete("1.0", END)

        def Exit():
            s_Exit =tkinter.messagebox.askyesno("Body Mass Index(BMI)", "Confirm if you want to exit")
            if s_Exit > 0:
                root.destroy()
                return
        #=================================== Labelling and Implementation==============================================

        self.lblTitle = Label(LeftFrame_0, text="Body Mass Index(BMI) Calculator", padx=17, pady=30,bd=1,bg="sky blue",
                              font=('arial', 30, 'bold'), width=27)
        self.lblTitle.pack()

        self.BodyHeight = Scale(RightFrame_0, variable=var3, from_=0.00, to=3.00, tickinterval=0.50, orient=HORIZONTAL,
                                state=DISABLED, label="Height in Meters",font=('arial', 10,'bold'),length=503)
        self.BodyHeight.grid(row=1,column=0)

        self.BodyWeight = Scale(RightFrame_2, variable=var4, from_=1, to=500, tickinterval=50, orient=HORIZONTAL,
                                state=DISABLED, label="Weight in Kilograms", font=('arial', 10, 'bold'),length=503)
        self.BodyWeight.grid(row=3, column=0)

        self.lblBMITable = Label(RightFrame_1, font=('arial', 20, 'bold'), text="\tBMI Table")
        self.lblBMITable.grid(row=0, column=0)

        self.txtBMITable = Text(RightFrame_1,height=12, width=53, bd=16,font=('arial', 12, 'bold'))
        self.txtBMITable.grid(row=1,column=0,columnspan=3)

        self.txtBMITable.insert(END, '\tMeaning\t\t\t'+"BMI\n\n")
        self.txtBMITable.insert(END, '\tNormal Weight\t\t\t' + "19.00 to 24.99\n\n")
        self.txtBMITable.insert(END, '\tOver Weight\t\t\t' + "25.00 to 29.99\n\n")
        self.txtBMITable.insert(END, '\tObesity Level I\t\t\t' + "30 to 34.99\n\n")
        self.txtBMITable.insert(END, '\tObesity Level II\t\t\t' + "35.00 to 39.99\n\n")
        self.txtBMITable.insert(END, '\tObesity Level III\t\t\t' + "Greater than 40\n\n")
#=================================================================================================================

        self.lblheight = Label(LeftFrame_2,text="Enter Height in Meters:",font=('arial', 20, 'bold'),width=25, bd=2,
                               justify=LEFT)
        self.lblheight.grid(row=0, column=0, padx=15)
        self.txtheight = Entry(LeftFrame_2, textvariable=var1, font=('arial', 19, 'bold'), bd=5, width=15,
                               justify=RIGHT)
        self.txtheight.grid(row=0, column=1, pady=10)

        self.lblWeight = Label(LeftFrame_2, text="Enter Weight in Kilogram:", font=('arial', 20, 'bold'),width=25, bd=2,
                               justify=LEFT)
        self.lblWeight.grid(row=1, column=0)
        self.txtBodyweight = Entry(LeftFrame_2, textvariable=var2, font=('arial', 19, 'bold'), bd=5, width=15,
                                   justify=RIGHT)
        self.txtBodyweight.grid(row=1, column=1, pady=10)

        self.lblBMIResult = Label(LeftFrame_3, text="Your BMI Result is:",width=20,padx=3,pady=30, font=('arial',20, 'bold'), bd=2)
        self.lblBMIResult.grid(row=0, column=0)
        self.txtBMIResult = Text(LeftFrame_3, padx=105, pady=7, font=('arial', 19, 'bold'), bd=5,bg="sky blue",
                                  relief="sunk", width=8,height=1)
        self.txtBMIResult.grid(row=0, column=1)
        #========================================== Creating Button =========================================================

        self.btnBMI = Button(LeftFrame_1, text="Calculate BMI", padx=6, pady=3, bd=4, width=12,font=('arial', 20, 'bold'),
                             height=2, command=BMI_Cal)
        self.btnBMI.grid(row=3, column=0)

        self.btnReset = Button(LeftFrame_1, text="Reset", padx=5, pady=3, bd=4, width=12, font=('arial', 20, 'bold'),
                               height=2,command=Reset)
        self.btnReset.grid(row=3, column=1)

        self.btnExit = Button(LeftFrame_1, text="Exit", padx=5, pady=3, bd=4, width=12, font=('arial', 20, 'bold'),
                              height=2, command=Exit)
        self.btnExit.grid(row=3, column=2)

if __name__ == '__main__':
    root = Tk()  # root is the name of the main window object
    app = BMI(root)
    root.mainloop() # mainloop() is used w hen your application is ready to run