from tkinter import *
import tkinter.messagebox
import back


class clientData:
    def __init__(self, root):
        self.root = root
        self.root.title("First A-Laranma Global Ventures")
        self.root.geometry("1350x3700+0+0")
        self.root.config(bg="light blue")
        self.root.iconbitmap(
            "C:/Users/cyberxploit/Desktop/PythonProjects/Tkinter/F A G V/booking 2/logo.ico")

        # Entries variables specified
        CustID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile1 = StringVar()

        # ==================FUNCTIONS====================#
        # Fetch the selected tuple of items. eg Returns a full record in a single line which contains
        # Customer identity, fullname, dob, gender, address and mobile number
        def get_selected_tuple(event):
            global selected_tuple
            index = clientList.curselection()[0]
            selected_tuple = clientList.get(index)

            self.txtCustID.delete(0, END)
            self.txtCustID.insert(END, selected_tuple[1])
            self.txtFirstname.delete(0, END)
            self.txtFirstname.insert(END, selected_tuple[2])
            self.txtSurname.delete(0, END)
            self.txtSurname.insert(END, selected_tuple[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, selected_tuple[4])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, selected_tuple[5])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, selected_tuple[6])
            self.txtMobile1.delete(0, END)
            self.txtMobile1.insert(END, selected_tuple[7])

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "First A-Laranma Global Ventures", "Confirm if you want to exit"
            )
            if iExit > 0:
                self.root.destroy()
                return

        def add():
            if len(CustID.get()) != 0:
                back.addRec(
                    CustID.get(),
                    Firstname.get(),
                    Surname.get(),
                    DoB.get(),
                    Gender.get(),
                    Address.get(),
                    Mobile1.get()
                )
                clientList.delete(0, END)
                clientList.insert(
                    END,
                    (
                        CustID.get(),
                        Firstname.get(),
                        Surname.get(),
                        DoB.get(),
                        Gender.get(),
                        Address.get(),
                        Mobile1.get()
                    )
                )

        def view():
            clientList.delete(0, END)
            for row in back.viewRec():
                clientList.insert(END, row, str(""))

        def clear():
            self.txtCustID.delete(0, END)
            self.txtFirstname.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtMobile1.delete(0, END)

        def update():
            if len(CustID.get()) != 0:
                back.deleteRec(selected_tuple[0])
            if len(CustID.get()) != 0:
                back.addRec(
                    CustID.get(),
                    Firstname.get(),
                    Surname.get(),
                    DoB.get(),
                    Gender.get(),
                    Address.get(),
                    Mobile1.get()
                )
                clientList.delete(0, END)
                clientList.insert(
                    END,
                    CustID.get(),
                    Firstname.get(),
                    Surname.get(),
                    DoB.get(),
                    Gender.get(),
                    Address.get(),
                    Mobile1.get()
                )

        def search():
            clientList.delete(0, END)
            for row in back.searchRec(
                CustID.get(),
                Firstname.get(),
                Surname.get(),
                DoB.get(),
                Gender.get(),
                Address.get(),
                Mobile1.get()
            ):
                clientList.insert(END, row, str(""))

        def delete():
            delete = tkinter.messagebox.askyesno(
                "First A-Laranma Global Ventures", "Confirm if you want to delete"
            )
            if delete > 0:
                if (len(CustID.get())) != 0:
                    back.deleteRec(selected_tuple[0])
                    clear()
                    view()

        def backup():
            

        # =====================FRAMES======================#
        MainFrame = Frame(self.root, bg="Ghost white")
        MainFrame.grid()

        TitFrame = Frame(
            MainFrame, bd=2, padx=68, pady=4, bg="light blue", relief=RIDGE
        )
        TitFrame.pack(side=TOP)

        self.lbtTit = Label(
            TitFrame,
            font=("arial", 47, "bold"),
            text="FIRST A-LARANMA GLOBAL VENTURES",
            bg="Ghost White",
        )
        self.lbtTit.grid()

        DataFrame = Frame(
            MainFrame,
            bd=1,
            width=1300,
            height=200,
            padx=10,
            pady=10,
            bg="red",
            relief=RIDGE,
        )
        DataFrame.pack(side=TOP)

        DataFrameLEFT = LabelFrame(
            DataFrame,
            bd=1,
            width=800,
            height=100,
            padx=10,
            pady=10,
            bg="Ghost White",
            relief=RIDGE,
            font=("arial", 20, "bold"),
            text="CLIENTS MEMBERSHIP INFO \n",
        )
        DataFrameLEFT.pack(side=TOP)

        ButtonFrame = Frame(
            DataFrame,
            bd=1,
            width=60,
            height=70,
            padx=6,
            pady=6,
            bg="Ghost White",
            relief=RIDGE,
        )
        ButtonFrame.pack(side=TOP)

        DataFrameRIGHT = LabelFrame(
            MainFrame,
            bd=1,
            width=1400,
            height=300,
            padx=10,
            pady=20,
            bg="light blue",
            relief=RIDGE,
            font=("arial", 20, "bold"),
            text="Book Details ",
        )
        DataFrameRIGHT.pack(side=BOTTOM)

        # =================LABELS AND WIDGETS==============#
        self.lblCustID = Label(
            DataFrameLEFT,
            font=("arial", 18, "bold"),
            text="Customer ID:",
            padx=2,
            pady=2,
            bg="Ghost White",
        )
        self.lblCustID.grid(row=0, column=0, sticky="W")
        self.txtCustID = Entry(
            DataFrameLEFT, font=("arial", 14), textvariable=CustID, width=12
        )
        self.txtCustID.grid(row=0, column=1)

        self.lblFirstname = Label(
            DataFrameLEFT,
            font=("arial", 18, "bold"),
            text="Firstname:",
            padx=2,
            pady=2,
            bg="Ghost White",
        )
        self.lblFirstname.grid(row=0, column=2, sticky="W")
        self.txtFirstname = Entry(
            DataFrameLEFT, font=("arial", 14), textvariable=Firstname, width=12
        )
        self.txtFirstname.grid(row=0, column=3)

        self.lblSurname = Label(
            DataFrameLEFT,
            font=("arial", 18, "bold"),
            text="Surname:",
            padx=2,
            pady=2,
            bg="Ghost White",
        )
        self.lblSurname.grid(row=0, column=4, sticky="W")
        self.txtSurname = Entry(
            DataFrameLEFT, font=("arial", 14), textvariable=Surname, width=12
        )
        self.txtSurname.grid(row=0, column=5)

        self.lblDoB = Label(
            DataFrameLEFT,
            font=("arial", 18, "bold"),
            text="DoB:",
            padx=2,
            pady=2,
            bg="Ghost White",
        )
        self.lblDoB.grid(row=0, column=6, sticky="W")
        self.txtDoB = Entry(
            DataFrameLEFT, font=("arial", 14), textvariable=DoB, width=12
        )
        self.txtDoB.grid(row=0, column=7)

        self.lblGender = Label(
            DataFrameLEFT,
            font=("arial", 18, "bold"),
            text="Gender:",
            padx=2,
            pady=2,
            bg="Ghost White",
        )
        self.lblGender.grid(row=1, column=0, sticky="W")
        self.txtGender = Entry(
            DataFrameLEFT, font=("arial", 14), textvariable=Gender, width=12
        )
        self.txtGender.grid(row=1, column=1)

        self.lblAddress = Label(
            DataFrameLEFT,
            font=("arial", 18, "bold"),
            text="Address:",
            padx=2,
            pady=2,
            bg="Ghost White",
        )
        self.lblAddress.grid(row=1, column=2, sticky="W")
        self.txtAddress = Entry(
            DataFrameLEFT, font=("arial", 14), textvariable=Address, width=12
        )
        self.txtAddress.grid(row=1, column=3)

        self.lblMobile1 = Label(
            DataFrameLEFT,
            font=("arial", 18, "bold"),
            text="Mobile1:",
            padx=2,
            pady=2,
            bg="Ghost White",
        )
        self.lblMobile1.grid(row=1, column=4, sticky="W")
        self.txtMobile1 = Entry(
            DataFrameLEFT, font=("arial", 14), textvariable=Mobile1, width=12
        )
        self.txtMobile1.grid(row=1, column=5)

        # ================LISTBOX AND SCROLLBAR============#

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky="ns")

        clientList = Listbox(
            DataFrameRIGHT,
            width=100,
            height=12,
            font=("arial", 12, "bold"),
            yscrollcommand=scrollbar.set,
        )
        clientList.grid(row=0, column=0, padx=8)

        scrollbar.config(command=clientList.yview)
        clientList.bind("<<ListboxSelect>>", get_selected_tuple)

        # ======================BUTTONS=====================#
        self.btnAddData = Button(
            ButtonFrame,
            text="Add New",
            font=("arial", 12, "bold"),
            command=add,
            height=1,
            width=10,
            bd=6,
        )
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(
            ButtonFrame,
            text="View All",
            font=("arial", 11, "bold"),
            command=view,
            height=1,
            width=10,
            bd=6,
        )
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(
            ButtonFrame,
            text="Clear",
            font=("arial", 12, "bold"),
            command=clear,
            height=1,
            width=8,
            bd=6,
        )
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(
            ButtonFrame,
            text="Delete",
            font=("arial", 11, "bold"),
            command=delete,
            height=1,
            width=8,
            bd=6,
            fg="red",
        )
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(
            ButtonFrame,
            text="Search",
            font=("arial", 12, "bold"),
            command=search,
            height=1,
            width=8,
            bd=6,
        )
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(
            ButtonFrame,
            text="Update",
            font=("arial", 11, "bold"),
            command=update,
            height=1,
            width=10,
            bd=6,
        )
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExitData = Button(
            ButtonFrame,
            text="Exit",
            font=("arial", 12, "bold"),
            command=iExit,
            height=1,
            width=10,
            bd=6,
            fg="red",
        )
        self.btnExitData.grid(row=0, column=6)


if __name__ == "__main__":
    root = Tk()
    application = clientData(root)
    root.mainloop()


'''

        self.lblCustID = Label(DataFrameLEFT, font=("arial", 18, "bold"), text="Customer ID :", padx=2, pady=2, bg="Ghost White")
        self.lblCustID.grid(row=0, column=0, sticky='W')
        self.txtCustID = Entry(DataFrameLEFT, font=("arial", 14), textvariable=CustID, width=12)
        self.txtCustID.grid(row=0, column=1)

        self.lblFirstname = Label(DataFrameLEFT, font=("arial", 18, "bold"), text="Firstname :", padx=2, pady=2, bg="Ghost White")
        self.lblFirstname.grid(row=0, column=2, sticky='W')
        self.txtFirstname = Entry(DataFrameLEFT, font=("arial", 14), textvariable=Firstname, width=12)
        self.txtFirstname.grid(row=0, column=3)
        
        self.lblSurname = Label(DataFrameLEFT, font=("arial", 18, "bold"), text="Surname :", padx=2, pady=2, bg="Ghost White")
        self.lblSurname.grid(row=0, column=4, sticky='W')
        self.txtSurname = Entry(DataFrameLEFT, font=("arial", 14), textvariable=Surname, width=12)
        self.txtSurname.grid(row=0, column=5)
        
        self.lblDoB = Label(DataFrameLEFT, font=("arial", 18, "bold"), text="DoB :", padx=2, pady=2, bg="Ghost White")
        self.lblDoB.grid(row=0, column=6, sticky='W')
        self.txtDoB = Entry(DataFrameLEFT, font=("arial", 14), textvariable=DoB, width=12)
        self.txtDoB.grid(row=0, column=7)
        
        self.lblGender = Label(DataFrameLEFT, font=("arial", 18, "bold"), text="Gender :", padx=2, pady=2, bg="Ghost White")
        self.lblGender.grid(row=1, column=0, sticky='W')
        self.txtGender = Entry(DataFrameLEFT, font=("arial", 14), textvariable=Gender, width=12)
        self.txtGender.grid(row=1, column=1)
        
        self.lblAddress = Label(DataFrameLEFT, font=("arial", 18, "bold"), text="Address :", padx=2, pady=2, bg="Ghost White")
        self.lblAddress.grid(row=1, column=2, sticky='W')
        self.txtAddress = Entry(DataFrameLEFT, font=("arial", 14), textvariable=Address, width=12)
        self.txtFirstname.grid(row=1, column=3)
        
        self.lblMobile1 = Label(DataFrameLEFT, font=("arial", 18, "bold"), text="Mobile1 :", padx=2, pady=2, bg="Ghost White")
        self.lblMobile1.grid(row=1, column=4, sticky='W')
        self.txtMobile1 = Entry(DataFrameLEFT, font=("arial", 14), textvariable=Mobile1, width=12)
        self.txtMobile1.grid(row=1, column=5)

        self.lblMobile2 = Label(DataFrameLEFT, font=("arial", 18, "bold"), text="Mobile2 :", padx=2, pady=2, bg="Ghost White")
        self.lblMobile2.grid(row=1, column=6, sticky='W')
        self.txtMobile2 = Entry(DataFrameLEFT, font=("arial", 14), textvariable=Mobile2, width=12)
        self.txtMobile2.grid(row=1, column=7)

    '''
