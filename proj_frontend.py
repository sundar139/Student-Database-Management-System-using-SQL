#front end
from tkinter import *
import tkinter.messagebox
import proj_backend as pb 

class Student:
     
    def __init__(self,root):
       self.root=root 
       self.root.title("Student Database Management System")
       self.root.geometry(newGeometry="1328x750+0+0")
       self.root.config(bg="#DC7633")
       #ASSIGNING SOME VARIABLES TO STORE OUR ENTRY FILELD VALUES
       StdId=StringVar()
       Firstname=StringVar()
       Surname=StringVar()
       DoB=StringVar()
       Age=StringVar()
       Gender=StringVar()
       Address=StringVar()
       Mobile=StringVar()
    
       ###########################FUNCTIONS########################
       pb.StudentData()
       def iExit():
              iExit=tkinter.messagebox.askyesno("DTU's Student DBMS","Confirm if you want to exit")
              if iExit>0:
                     root.destroy()
                     return
       def ClearData():
              self.txtStdId.delete(0,END)
              self.txtFirstname.delete(0,END)
              self.txtSurname.delete(0,END)
              self.txtDob.delete(0,END)
              self.txtAge.delete(0,END)
              self.txtGender.delete(0,END)
              self.txtAdress.delete(0,END)
              self.txtMobile.delete(0,END) 
       pb.StudentData()             
       def AddData():
              if(len(StdId.get())!=0):
                     
                     pb.AddStdRec(StdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                     studentlist.delete(0,END)
                     studentlist.insert(END,(StdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))

       def DisplayData():
              studentlist.delete(0,END)
              for row in pb.ViewData():
                  studentlist.insert(END,row)

       def DisplayNames():
              studentlist.delete(0,END)
              for row in pb.ViewNames():
                  studentlist.insert(END,row)
       
       def DisplayNumbers():
              studentlist.delete(0,END)
              for row in pb.ViewMobile():
                  studentlist.insert(END,row)
       
       def DisplayAddress():
              studentlist.delete(0,END)
              for row in pb.ViewAddress():
                  studentlist.insert(END,row)
       
       def DisplayDoB():
              studentlist.delete(0,END)
              for row in pb.ViewDoB():
                  studentlist.insert(END,row)
       
       def DisplayGender():
              studentlist.delete(0,END)
              for row in pb.ViewGender():
                  studentlist.insert(END,row)
               
       def DisplayID():
              studentlist.delete(0,END)
              for row in pb.ViewID():
                  studentlist.insert(END,row)

       def StudentRec(event):
              global sd
              searchstd = studentlist.curselection()[0]
              sd=studentlist.get(searchstd)
              self.txtStdId.delete(0,END)
              self.txtStdId.insert(END,sd[0])
              self.txtFirstname.delete(0,END)
              self.txtFirstname.insert(END,sd[1])
              self.txtSurname.delete(0,END)
              self.txtSurname.insert(END,sd[2])
              self.txtDob.delete(0,END)
              self.txtDob.insert(END,sd[3])
              self.txtAge.delete(0,END)
              self.txtAge.insert(END,sd[4])
              self.txtGender.delete(0,END)
              self.txtGender.insert(END,sd[5])
              self.txtAdress.delete(0,END)
              self.txtAdress.insert(END,sd[6])
              self.txtMobile.delete(0,END)  
              self.txtMobile.insert(END,sd[7])

       def DeleteData():
              
              if(len(StdId.get())!=0):
                     pb.DeleteRec(sd[0])
                     ClearData()
                     DisplayData()

       def SearchDatabase():
              studentlist.delete(0,END)
              for row in pb.SearchData(StdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()):
                     studentlist.insert(END,row,str(""))  
    
       def Update():
              if(len(StdId.get())!=0):
                     pb.DeleteRec(sd[0])
              if(len(StdId.get())!=0):
                     pb.AddStdRec(StdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                     studentlist.delete(0,END)
                     studentlist.insert(END,(StdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))   

       #####################################FRAMES###################################################################
       MainFrame=Frame(self.root,bg="#F5B041")
       MainFrame.grid()  #THIS IS THE MAIN FRAME OF OUR WINDOW
       TitFrame=Frame(MainFrame,bd=1,padx=54,pady=8,bg="#DC7633",relief=RIDGE)
       TitFrame.pack(side=TOP)#THIS IS THE TITLE FRAME
    
       self.lblTit=Label(TitFrame,font=('arial',47,'bold'),text="Students Database Management System",bg="#DC7633",fg="black")
       self.lblTit.grid()

       self.lblTit=Label(TitFrame,font=('arial',25,'bold'),text="DTU",bg="#DC7633",fg="black")
       self.lblTit.grid()

       ButtonFrame=Frame(MainFrame,bd=1,width=1350,height=70,padx=18,pady=10,bg="#E74C3C",relief=RIDGE)
       ButtonFrame.pack(side=BOTTOM)

       DataFrame=Frame(MainFrame,bd=9,width=1300,height=400,padx=20,pady=20,bg="#B9770E",relief=RIDGE)
       DataFrame.pack(side=BOTTOM)
         
       DataFrameLeft=LabelFrame(DataFrame,font=('arial',12,'bold'),bd=1,width=450,height=300,bg="#F4D03F",relief=RIDGE,text="STUDENT INFO\n")
       DataFrameLeft.pack(side=LEFT)

       DataFrameRight=LabelFrame(DataFrame,font=('arial',12,'bold'),bd=1,width=450,height=300,bg="#F4D03F",relief=RIDGE,text="STUDENT DETAILS\n")
       DataFrameRight.pack(side=RIGHT)
#########################################################Lables and Entry widget #######################################################################
       
       self.lblStdId=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Student Id:",bg="#F4D03F")
       self.lblStdId.grid(row=0,column=0,sticky=W)
       
       self.txtStdId=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=StdId,bg="ghost white",width=39)
       self.txtStdId.grid(row=0,column=1)#student id

       self.lblFirstname=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="First Name:",bg="#F4D03F")
       self.lblFirstname.grid(row=1,column=0,sticky=W)
       
       self.txtFirstname=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Firstname,bg="ghost white",width=39)
       self.txtFirstname.grid(row=1,column=1)#firstname


       self.lblSurname=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Surname:",bg="#F4D03F")
       self.lblSurname.grid(row=2,column=0,sticky=W)
       
       self.txtSurname=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Surname,bg="ghost white",width=39)
       self.txtSurname.grid(row=2,column=1)#surname

       self.lblDob=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Date of Birth:",bg="#F4D03F")
       self.lblDob.grid(row=3,column=0,sticky=W)
       
       self.txtDob=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=DoB,bg="ghost white",width=39)
       self.txtDob.grid(row=3,column=1)#dateof birth

       self.lblAge=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Age:",bg="#F4D03F")
       self.lblAge.grid(row=4,column=0,sticky=W)
       
       self.txtAge=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Age,bg="ghost white",width=39)
       self.txtAge.grid(row=4,column=1)#age

       self.lblGender=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Gender:",bg="#F4D03F")
       self.lblGender.grid(row=5,column=0,sticky=W)
       
       self.txtGender=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Gender,bg="ghost white",width=39)
       self.txtGender.grid(row=5,column=1)#gender

       self.lblAdress=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Address:",bg="#F4D03F")
       self.lblAdress.grid(row=6,column=0,sticky=W)
       
       self.txtAdress=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Address,bg="ghost white",width=39)
       self.txtAdress.grid(row=6,column=1)#address

       self.lblMobile=Label(DataFrameLeft,font=('arial',12,'bold'),padx=2,pady=3,text="Mobile:",bg="#F4D03F")
       self.lblMobile.grid(row=7,column=0,sticky=W)
       
       self.txtMobile=Entry(DataFrameLeft,font=('arial',12,'bold'),textvariable=Mobile,bg="ghost white",width=39)
       self.txtMobile.grid(row=7,column=1)#mobile


       ###############################List Box and ScrollBar Widget############################################
       scrollbar=Scrollbar(DataFrameRight)
       scrollbar.grid(row=0 ,column=1,sticky='ns')#scroll bar

       studentlist=Listbox(DataFrameRight,width=68,height=13,font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
       studentlist.bind('<<ListboxSelect>>',StudentRec)
       studentlist.grid(row=0,column=0,padx=10)
       scrollbar.config(command= studentlist.yview)


       #######################################Button Widget####################################################
       self.btnAddData=Button(ButtonFrame,text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=AddData)
       self.btnAddData.grid(row=0,column=0)#ADD NEW

       self.btnDisplay=Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayData)
       self.btnDisplay.grid(row=0,column=1)#DISPLAY

       self.btnClear=Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=ClearData)
       self.btnClear.grid(row=0,column=2)#CLEAR

       self.btnDelete=Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DeleteData)
       self.btnDelete.grid(row=0,column=3)#DELETE

       self.btnSearch=Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=SearchDatabase)
       self.btnSearch.grid(row=0,column=4)#SEARCH

       self.btnUpdate=Button(ButtonFrame,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=Update)
       self.btnUpdate.grid(row=0,column=5)#UPDATE

       self.btnExit=Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=iExit)
       self.btnExit.grid(row=0,column=6)#EXIT

       self.btnNames=Button(ButtonFrame,text="Names",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayNames)
       self.btnNames.grid(row=1,column=0)#NAMES

       self.btnNumber=Button(ButtonFrame,text="Numbers",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayNumbers)
       self.btnNumber.grid(row=1,column=1)#NUMBERS

       self.btnAddress=Button(ButtonFrame,text="Address",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayAddress)
       self.btnAddress.grid(row=1,column=2)#ADDRESS

       self.btnDoB=Button(ButtonFrame,text="DoB",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayDoB)
       self.btnDoB.grid(row=1,column=3)#DOB

       self.btnGender=Button(ButtonFrame,text="Gender",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayGender)
       self.btnGender.grid(row=1,column=4)#GENDER
       
       self.btnID=Button(ButtonFrame,text="ID",font=('arial',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayID)
       self.btnID.grid(row=1,column=5)#ID


if __name__=='__main__':
   root=Tk()#CREATE AN OBJECT
   application=Student(root)#PASS IT TO OUR CLASS WHITH ITS PROPERTIES IN CLASS
   root.mainloop()#RUN UNTIL CLOSING THE WINDOW MANUALLY
