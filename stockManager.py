import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as Msg
import mysql.connector as mysql


main=tk.Tk()
main.geometry("1200x700")
main.title("ECO AGRO (Stock Recorder)")

def add_in():
    in_window = Toplevel(main)
    in_window.title("Add In Records")
    in_window.geometry("1200x700")
    
    def savecmd():
        dates = date_e.get()
        supp_codes = supp_code_e.get()
        stock_codes = stock_code_e.get()
        type_materials = type_m_e.get()
        ec_vals = ec_e.get()
        moistures = moist_e.get()
        fibers = fiber_e.get()
        amounts = amount_e.get()
        qc_checks = qc_e.get()
        storage_areas = store_e.get()
    
        if (dates=="" or supp_codes=="" or stock_codes=="" or type_materials=="" or amounts=="" or qc_checks==""):
            Msg.showinfo("Insert Data","Required Fields are not yet filled")
        
        else:
            con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
            cursor = con.cursor()
            cursor.execute("INSERT INTO supplier (date,supp_code,stock_code,type_material,ec_val,moisture,fiber,amount,qc_check,storage_area) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(dates,supp_codes,stock_codes,type_materials,ec_vals,moistures,fibers,amounts,qc_checks,storage_areas))
            cursor.execute("commit");
            date_e.delete(0,'end')
            supp_code_e.delete(0,'end')
            stock_code_e.delete(0,'end')
            type_m_e.delete(0,'end')
            ec_e.delete(0,'end')
            moist_e.delete(0,'end')
            fiber_e.delete(0,'end')
            amount_e.delete(0,'end')
            qc_e.delete(0,'end')
            store_e.delete(0,'end')
            
            cursor.execute("TRUNCATE TABLE stock_onhand")
            #cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
            doquerry = """
            INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat)
            SELECT supplier.stock_code, supplier.type_material, supplier.amount, IFNULL(out_unique.tot_use, 0), (supplier.amount - IFNULL(out_unique.tot_use, 0))
            FROM supplier
            LEFT JOIN out_unique ON supplier.stock_code = out_unique.stock_code;
            """
            cursor.execute(doquerry)
            con.commit()
            cursor.close()
            
            Msg.showinfo("Status","Record Added Succesfully")
            con.close();
        show()
        
    def show():
        con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
        cursor = con.cursor()
        cursor.execute("select count(*) from supplier")
        s = cursor.fetchall()
        z=int(s[0][0])
        cursor.execute(f"SELECT * FROM supplier LIMIT {z-3}, 1")
        rows = cursor.fetchall()
        id_show1.config(text=rows[0][0])
        date_show1.config(text=rows[0][1])
        supp_code_show1.config(text=rows[0][2])
        stock_code_show1.config(text=rows[0][3])
        type_m_show1.config(text=rows[0][4])
        ec_show1.config(text=rows[0][5])
        moist_show1.config(text=rows[0][6])
        fiber_show1.config(text=rows[0][7])
        amount_show1.config(text=rows[0][8])
        qc_show1.config(text=rows[0][9])
        store_show1.config(text=rows[0][10])
    
    
        cursor.execute(f"SELECT * FROM supplier LIMIT {z-2}, 1")
        rows = cursor.fetchall()
        id_show2.config(text=rows[0][0])
        date_show2.config(text=rows[0][1])
        supp_code_show2.config(text=rows[0][2])
        stock_code_show2.config(text=rows[0][3])
        type_m_show2.config(text=rows[0][4])
        ec_show2.config(text=rows[0][5])
        moist_show2.config(text=rows[0][6])
        fiber_show2.config(text=rows[0][7])
        amount_show2.config(text=rows[0][8])
        qc_show2.config(text=rows[0][9])
        store_show2.config(text=rows[0][10])
    
        cursor.execute(f"SELECT * FROM supplier LIMIT {z-1}, 1")
        rows = cursor.fetchall()
        id_show3.config(text=rows[0][0])
        date_show3.config(text=rows[0][1])
        supp_code_show3.config(text=rows[0][2])
        stock_code_show3.config(text=rows[0][3])
        type_m_show3.config(text=rows[0][4])
        ec_show3.config(text=rows[0][5])
        moist_show3.config(text=rows[0][6])
        fiber_show3.config(text=rows[0][7])
        amount_show3.config(text=rows[0][8])
        qc_show3.config(text=rows[0][9])
        store_show3.config(text=rows[0][10])
    
        con.close();
    

    def label_clicked1(event):
        id_user = id_show1.cget("text")
        date_e.delete(0,'end')
        supp_code_e.delete(0,'end')
        stock_code_e.delete(0,'end')
        type_m_e.delete(0,'end')
        ec_e.delete(0,'end')
        moist_e.delete(0,'end')
        fiber_e.delete(0,'end')
        amount_e.delete(0,'end')
        qc_e.delete(0,'end')
        store_e.delete(0,'end')
        date_e.insert(0,date_show1.cget("text"))
        supp_code_e.insert(0,supp_code_show1.cget("text"))
        stock_code_e.insert(0,stock_code_show1.cget("text"))
        type_m_e.insert(0,type_m_show1.cget("text"))
        ec_e.insert(0,ec_show1.cget("text"))
        moist_e.insert(0,moist_show1.cget("text"))
        fiber_e.insert(0,fiber_show1.cget("text"))
        amount_e.insert(0,amount_show1.cget("text"))
        qc_e.insert(0,qc_show1.cget("text"))
        store_e.insert(0,store_show1.cget("text"))
    
        def delete():
            if date_e.get()=="":
                Msg.showinfo("Status","Select a ID to Delete")
            else:
                con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
                cursor = con.cursor()
                cursor.execute("delete from supplier where id='"+str(id_user)+"'")
                cursor.execute("TRUNCATE TABLE stock_onhand")
                #cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                doquerry = """
                INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat)
                SELECT supplier.stock_code, supplier.type_material, supplier.amount, IFNULL(out_unique.tot_use, 0), (supplier.amount - IFNULL(out_unique.tot_use, 0))
                FROM supplier
                LEFT JOIN out_unique ON supplier.stock_code = out_unique.stock_code;
                """
                cursor.execute(doquerry)
                cursor.execute("commit");
                date_e.delete(0,'end')
                supp_code_e.delete(0,'end')
                stock_code_e.delete(0,'end')
                type_m_e.delete(0,'end')
                ec_e.delete(0,'end')
                moist_e.delete(0,'end')
                fiber_e.delete(0,'end')
                amount_e.delete(0,'end')
                qc_e.delete(0,'end')
                store_e.delete(0,'end')
                
                
                
                Msg.showinfo("Status","Record Deleted Succesfully")
                show()
                cursor.execute("TRUNCATE TABLE stock_onhand")
                cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                con.commit()
                cursor.close()
                con.close();
                
        del_butt = Button(in_window,text='Delete',font=('Arial',12),command =delete)
        del_butt.place(x =320,y = 430)
        
        
    
    
    def label_clicked2(event):
        id_user = id_show2.cget("text")
        date_e.delete(0,'end')
        supp_code_e.delete(0,'end')
        stock_code_e.delete(0,'end')
        type_m_e.delete(0,'end')
        ec_e.delete(0,'end')
        moist_e.delete(0,'end')
        fiber_e.delete(0,'end')
        amount_e.delete(0,'end')
        qc_e.delete(0,'end')
        store_e.delete(0,'end')
        date_e.insert(0,date_show2.cget("text"))
        supp_code_e.insert(0,supp_code_show2.cget("text"))
        stock_code_e.insert(0,stock_code_show2.cget("text"))
        type_m_e.insert(0,type_m_show2.cget("text"))
        ec_e.insert(0,ec_show2.cget("text"))
        moist_e.insert(0,moist_show2.cget("text"))
        fiber_e.insert(0,fiber_show2.cget("text"))
        amount_e.insert(0,amount_show2.cget("text"))
        qc_e.insert(0,qc_show2.cget("text"))
        store_e.insert(0,store_show2.cget("text"))
        def delete():
            if date_e.get()=="":
                Msg.showinfo("Status","Select a ID to Delete")
            else:
                con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
                cursor = con.cursor()
                cursor.execute("delete from supplier where id='"+str(id_user)+"'")
                cursor.execute("TRUNCATE TABLE stock_onhand")
                cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                cursor.execute("commit");
                date_e.delete(0,'end')
                supp_code_e.delete(0,'end')
                stock_code_e.delete(0,'end')
                type_m_e.delete(0,'end')
                ec_e.delete(0,'end')
                moist_e.delete(0,'end')
                fiber_e.delete(0,'end')
                amount_e.delete(0,'end')
                qc_e.delete(0,'end')
                store_e.delete(0,'end')
        
                Msg.showinfo("Status","Record Deleted Succesfully")
                show()
                cursor.execute("TRUNCATE TABLE stock_onhand")
                #cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                doquerry = """
                INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat)
                SELECT supplier.stock_code, supplier.type_material, supplier.amount, IFNULL(out_unique.tot_use, 0), (supplier.amount - IFNULL(out_unique.tot_use, 0))
                FROM supplier
                LEFT JOIN out_unique ON supplier.stock_code = out_unique.stock_code;
                """
                cursor.execute(doquerry)
                con.commit()
                cursor.close()
                con.close();
        del_butt = Button(in_window,text='Delete',font=('Arial',12),command =delete)
        del_butt.place(x =320,y = 430)
    
    def label_clicked3(event):
        id_user = id_show3.cget("text")
        date_e.delete(0,'end')
        supp_code_e.delete(0,'end')
        stock_code_e.delete(0,'end')
        type_m_e.delete(0,'end')
        ec_e.delete(0,'end')
        moist_e.delete(0,'end')
        fiber_e.delete(0,'end')
        amount_e.delete(0,'end')
        qc_e.delete(0,'end')
        store_e.delete(0,'end')
        date_e.insert(0,date_show3.cget("text"))
        supp_code_e.insert(0,supp_code_show3.cget("text"))
        stock_code_e.insert(0,stock_code_show3.cget("text"))
        type_m_e.insert(0,type_m_show3.cget("text"))
        ec_e.insert(0,ec_show3.cget("text"))
        moist_e.insert(0,moist_show3.cget("text"))
        fiber_e.insert(0,fiber_show3.cget("text"))
        amount_e.insert(0,amount_show3.cget("text"))
        qc_e.insert(0,qc_show3.cget("text"))
        store_e.insert(0,store_show3.cget("text"))
        def delete():
            if date_e.get()=="":
                Msg.showinfo("Status","Select a ID to Delete")
            else:
                con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
                cursor = con.cursor()
                cursor.execute("delete from supplier where id='"+str(id_user)+"'")
                cursor.execute("commit");
                date_e.delete(0,'end')
                supp_code_e.delete(0,'end')
                stock_code_e.delete(0,'end')
                type_m_e.delete(0,'end')
                ec_e.delete(0,'end')
                moist_e.delete(0,'end')
                fiber_e.delete(0,'end')
                amount_e.delete(0,'end')
                qc_e.delete(0,'end')
                store_e.delete(0,'end')
                
                cursor.execute("TRUNCATE TABLE stock_onhand")
                cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                Msg.showinfo("Status","Record Deleted Succesfully")
                show()
                cursor.execute("TRUNCATE TABLE stock_onhand")
                #cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                doquerry = """
                INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat)
                SELECT supplier.stock_code, supplier.type_material, supplier.amount, IFNULL(out_unique.tot_use, 0), (supplier.amount - IFNULL(out_unique.tot_use, 0))
                FROM supplier
                LEFT JOIN out_unique ON supplier.stock_code = out_unique.stock_code;
                """
                cursor.execute(doquerry)
                con.commit()
                cursor.close()
                con.close();
        del_butt = Button(in_window,text='Delete',font=('Arial',12),command =delete)
        del_butt.place(x =320,y = 430)
    
    
    
    def reset():
        date_e.delete(0,'end')
        supp_code_e.delete(0,'end')
        stock_code_e.delete(0,'end')
        type_m_e.delete(0,'end')
        ec_e.delete(0,'end')
        moist_e.delete(0,'end')
        fiber_e.delete(0,'end')
        amount_e.delete(0,'end')
        qc_e.delete(0,'end')
        store_e.delete(0,'end')
    
    

    topic=Label(in_window,text='Add a IN record',font=('Arial',15))
    topic.place(x=420,y=50)

    date =Label(in_window,text='Date',font=('Arial',11))
    date.place(x=100,y=150)

    date_e =Entry(in_window,font=('Arial',11))
    date_e.place(x=280,y=150,width = 100)

    supp_code =Label(in_window,text='Supplier Code',font=('Arial',11))
    supp_code.place(x=100,y=200)

    supp_code_e =Entry(in_window,font=('Arial',11))
    supp_code_e.place(x=280,y=200,width = 100)

    stock_code =Label(in_window,text='Stock Code',font=('Arial',11))
    stock_code.place(x=100,y=250)

    stock_code_e =Entry(in_window,font=('Arial',11))
    stock_code_e.place(x=280,y=250,width = 100)

    type_m =Label(in_window,text='Type',font=('Arial',11))
    type_m.place(x=100,y=300)

    #type_m_e =Entry(in_window,font=('Arial',11))
    #type_m_e.place(x=280,y=300,width = 100)

    type_m_e =ttk.Combobox(in_window,font=('Arial',11),width=33)
    type_m_e["values"]=("Washed CP","Unwashed CP","Treated CP","LEC CP","HEC CP","Black CP","Washed Chips", "Unwashed Chips","Treated Chips","HEC Chips","Washed Crushed","Unwashed Crushed","Crushed CP", "8mm Crush","Fine Dust","Other")
    type_m_e.place(x=280,y=300,width =155)

    ec =Label(in_window,text='EC Value',font=('Arial',11))
    ec.place(x=100,y=350)

    ec_e =Entry(in_window,font=('Arial',11))
    ec_e.place(x=280,y=350,width = 100)

    moist =Label(in_window,text='Moisture',font=('Arial',11))
    moist.place(x=550,y=150)

    moist_e =Entry(in_window,font=('Arial',11))
    moist_e.place(x=730,y=150,width = 100)

    fiber =Label(in_window,text='Fiber',font=('Arial',11))
    fiber.place(x=550,y=200)

    fiber_e =Entry(in_window,font=('Arial',11))
    fiber_e.place(x=730,y=200,width = 100)

    amount =Label(in_window,text='Amount',font=('Arial',11))
    amount.place(x=550,y=250)


    amount_e =Entry(in_window,font=('Arial',11))
    amount_e.place(x=730,y=250,width = 100)

    qc =Label(in_window,text='QC By',font=('Arial',11))
    qc.place(x=550,y=300)

    qc_e =Entry(in_window,font=('Arial',11))
    qc_e.place(x=730,y=300,width = 100)

    store =Label(in_window,text='Storage Area',font=('Arial',11))
    store.place(x=550,y=350)

    store_e =Entry(in_window,font=('Arial',11))
    store_e.place(x=730,y=350,width = 100)

    save_butt = Button(in_window,text='Save',font=('Arial',12),command =savecmd)
    save_butt.place(x =250,y = 430)

    reset_butt = Button(in_window,text='Reset',font=('Arial',12),command =reset)
    reset_butt.place(x =400,y = 430)






    id_t=Label(in_window,text='ID',font=('Arial',9),fg='red')
    id_t.place(x=20,y=500)

    date_t=Label(in_window,text='Date',font=('Arial',9),fg='red')
    date_t.place(x=120,y=500)

    supp_code_t=Label(in_window,text='Supplier Code',font=('Arial',9),fg='red')
    supp_code_t.place(x=227,y=500)

    stock_code_t=Label(in_window,text='Stock Code',font=('Arial',9),fg='red')
    stock_code_t.place(x=380,y=500)

    type_m_t=Label(in_window,text='Type',font=('Arial',9),fg='red')
    type_m_t.place(x=500,y=500)

    ec_t=Label(in_window,text='EC Value',font=('Arial',9),fg='red')
    ec_t.place(x=620,y=500)

    moist_t=Label(in_window,text='Moisture',font=('Arial',9),fg='red')
    moist_t.place(x=705,y=500)

    fiber_t=Label(in_window,text='Fiber',font=('Arial',9),fg='red')
    fiber_t.place(x=795,y=500)

    amount_t=Label(in_window,text='Amount',font=('Arial',9),fg='red')
    amount_t.place(x=860,y=500)

    qc_t=Label(in_window,text='QC By',font=('Arial',9),fg='red')
    qc_t.place(x=975,y=500)

    store_t=Label(in_window,text='Stored Area',font=('Arial',9),fg='red')
    store_t.place(x=1070,y=500)
    








    id_show1=Label(in_window,text='',font=('Arial',10))
    id_show1.bind("<Button-1>", label_clicked1)
    id_show1.place(x=20,y=550)

    date_show1=Label(in_window,text='',font=('Arial',10))
    date_show1.place(x=110,y=550)

    supp_code_show1=Label(in_window,text='',font=('Arial',10))
    supp_code_show1.place(x=255,y=550)

    stock_code_show1=Label(in_window,text='',font=('Arial',10))
    stock_code_show1.place(x=380,y=550)

    type_m_show1=Label(in_window,text='',font=('Arial',10))
    type_m_show1.place(x=500,y=550)

    ec_show1=Label(in_window,text='',font=('Arial',10))
    ec_show1.place(x=630,y=550)

    moist_show1=Label(in_window,text='',font=('Arial',10))
    moist_show1.place(x=725,y=550)

    fiber_show1=Label(in_window,text='',font=('Arial',10))
    fiber_show1.place(x=798,y=550)

    amount_show1=Label(in_window,text='',font=('Arial',10))
    amount_show1.place(x=862,y=550)

    qc_show1=Label(in_window,text='',font=('Arial',10))
    qc_show1.place(x=975,y=550)

    store_show1=Label(in_window,text='',font=('Arial',10))
    store_show1.place(x=1100,y=550)





    id_show2=Label(in_window,text='',font=('Arial',10))
    id_show2.bind("<Button-1>", label_clicked2)
    id_show2.place(x=20,y=590)

    date_show2=Label(in_window,text='',font=('Arial',10))
    date_show2.place(x=110,y=590)

    supp_code_show2=Label(in_window,text='',font=('Arial',10))
    supp_code_show2.place(x=255,y=590)

    stock_code_show2=Label(in_window,text='',font=('Arial',10))
    stock_code_show2.place(x=380,y=590)

    type_m_show2=Label(in_window,text='',font=('Arial',10))
    type_m_show2.place(x=500,y=590)

    ec_show2=Label(in_window,text='',font=('Arial',10))
    ec_show2.place(x=630,y=590)

    moist_show2=Label(in_window,text='',font=('Arial',10))
    moist_show2.place(x=725,y=590)

    fiber_show2=Label(in_window,text='',font=('Arial',10))
    fiber_show2.place(x=798,y=590)

    amount_show2=Label(in_window,text='',font=('Arial',10))
    amount_show2.place(x=862,y=590)

    qc_show2=Label(in_window,text='',font=('Arial',10))
    qc_show2.place(x=975,y=590)

    store_show2=Label(in_window,text='',font=('Arial',10))
    store_show2.place(x=1100,y=590)




    id_show3=Label(in_window,text='',font=('Arial',10))
    id_show3.bind("<Button-1>", label_clicked3)
    id_show3.place(x=20,y=630)

    date_show3=Label(in_window,text='',font=('Arial',10))
    date_show3.place(x=110,y=630)

    supp_code_show3=Label(in_window,text='',font=('Arial',10))
    supp_code_show3.place(x=255,y=630)

    stock_code_show3=Label(in_window,text='',font=('Arial',10))
    stock_code_show3.place(x=380,y=630)

    type_m_show3=Label(in_window,text='',font=('Arial',10))
    type_m_show3.place(x=500,y=630)

    ec_show3=Label(in_window,text='',font=('Arial',10))
    ec_show3.place(x=630,y=630)

    moist_show3=Label(in_window,text='',font=('Arial',10))
    moist_show3.place(x=725,y=630)

    fiber_show3=Label(in_window,text='',font=('Arial',10))
    fiber_show3.place(x=798,y=630)

    amount_show3=Label(in_window,text='',font=('Arial',10))
    amount_show3.place(x=862,y=630)

    qc_show3=Label(in_window,text='',font=('Arial',10))
    qc_show3.place(x=975,y=630)

    store_show3=Label(in_window,text='',font=('Arial',10))
    store_show3.place(x=1100,y=630)

    show()
    
    
    in_window.mainloop()
    
def add_out():
    out_window = Toplevel(main)
    out_window.title("Add Out Records")
    out_window.geometry("1000x600")
    
    def savecmd():
        dates = date_e.get()
        stock_codes = stock_code_e.get()
        usages = usage_e.get()
    
        if (dates=="" or stock_codes=="" or usages==""):
            Msg.showinfo("Insert Data","Required Fields are not yet filled")
        
        else:
            con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
            cursor = con.cursor()
            cursor.execute("insert into out_data (date,stock_code,usage_kg) values(%s,%s,%s)",(dates,stock_codes,usages))
            cursor.execute("commit")
            cursor.execute("TRUNCATE TABLE out_unique")
            
            aggregate_query = """
            INSERT INTO out_unique (stock_code, tot_use)
            SELECT stock_code, SUM(usage_kg) as tot_use
            FROM out_data
            GROUP BY stock_code;
            """
            cursor.execute(aggregate_query)
            con.commit()
            
            cursor.execute("TRUNCATE TABLE stock_onhand")
            #cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
            doquerry = """
            INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat)
            SELECT supplier.stock_code, supplier.type_material, supplier.amount, IFNULL(out_unique.tot_use, 0), (supplier.amount - IFNULL(out_unique.tot_use, 0))
            FROM supplier
            LEFT JOIN out_unique ON supplier.stock_code = out_unique.stock_code;
            """
            cursor.execute(doquerry)
            con.commit()
            cursor.close()
            
            date_e.delete(0,'end')
            stock_code_e.delete(0,'end')
            usage_e.delete(0,'end')
        
            Msg.showinfo("Status","Record Added Succesfully")
            
            

            
            show()
            con.close();
            
    
    def show():
        con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
        cursor = con.cursor()
        cursor.execute("select count(*) from out_data")
        s = cursor.fetchall()
        z=int(s[0][0])
        cursor.execute(f"SELECT * FROM out_data LIMIT {z-3}, 1")
        rows = cursor.fetchall()
        id_show1.config(text=rows[0][0])
        date_show1.config(text=rows[0][1])
        stock_code_show1.config(text=rows[0][2])
        usage_show1.config(text=rows[0][3])
    
    
        cursor.execute(f"SELECT * FROM out_data LIMIT {z-2}, 1")
        rows = cursor.fetchall()
        id_show2.config(text=rows[0][0])
        date_show2.config(text=rows[0][1])
        stock_code_show2.config(text=rows[0][2])
        usage_show2.config(text=rows[0][3])
    
        cursor.execute(f"SELECT * FROM out_data LIMIT {z-1}, 1")
        rows = cursor.fetchall()
        id_show3.config(text=rows[0][0])
        date_show3.config(text=rows[0][1])
        stock_code_show3.config(text=rows[0][2])
        usage_show3.config(text=rows[0][3])
    
        con.close();
        
        
    def label_clicked1(event):
        id_user = id_show1.cget("text")
        date_e.delete(0,'end')
        stock_code_e.delete(0,'end')
        usage_e.delete(0,'end')
        date_e.insert(0,date_show1.cget("text"))
        stock_code_e.insert(0,stock_code_show1.cget("text"))
        usage_e.insert(0,usage_show1.cget("text"))
        
    
        def delete():
            if date_e.get()=="":
                Msg.showinfo("Status","Select a ID to Delete")
            else:
                con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
                cursor = con.cursor()
                cursor.execute("delete from out_data where id='"+str(id_user)+"'")
                cursor.execute("commit");
                
                cursor.execute("TRUNCATE TABLE out_unique")
            
                aggregate_query = """
                INSERT INTO out_unique (stock_code, tot_use)
                SELECT stock_code, SUM(usage_kg) as tot_use
                FROM out_data
                GROUP BY stock_code;
                """
                cursor.execute(aggregate_query)
                con.commit()
                cursor.close()
                
                date_e.delete(0,'end')
                stock_code_e.delete(0,'end')
                usage_e.delete(0,'end')
        
                Msg.showinfo("Status","Record Deleted Succesfully")
                show()
                cursor.execute("TRUNCATE TABLE stock_onhand")
                #cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                doquerry = """
                INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat)
                SELECT supplier.stock_code, supplier.type_material, supplier.amount, IFNULL(out_unique.tot_use, 0), (supplier.amount - IFNULL(out_unique.tot_use, 0))
                FROM supplier
                LEFT JOIN out_unique ON supplier.stock_code = out_unique.stock_code;
                """
                cursor.execute(doquerry)
                con.commit()
                cursor.close()
                con.close();
                
        del_butt = Button(out_window,text='Delete',font=('Arial',13),command =delete)
        del_butt.place(x =265,y = 280)
        
        
    def label_clicked2(event):
        id_user = id_show2.cget("text")
        date_e.delete(0,'end')
        stock_code_e.delete(0,'end')
        usage_e.delete(0,'end')
        date_e.insert(0,date_show2.cget("text"))
        stock_code_e.insert(0,stock_code_show2.cget("text"))
        usage_e.insert(0,usage_show2.cget("text"))
        
    
        def delete():
            if date_e.get()=="":
                Msg.showinfo("Status","Select a ID to Delete")
            else:
                con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
                cursor = con.cursor()
                cursor.execute("delete from out_data where id='"+str(id_user)+"'")
                cursor.execute("commit");
                
                cursor.execute("TRUNCATE TABLE out_unique")
            
                aggregate_query = """
                INSERT INTO out_unique (stock_code, tot_use)
                SELECT stock_code, SUM(usage_kg) as tot_use
                FROM out_data
                GROUP BY stock_code;
                """
                cursor.execute(aggregate_query)
                con.commit()
                cursor.close()
                
                date_e.delete(0,'end')
                stock_code_e.delete(0,'end')
                usage_e.delete(0,'end')
        
                Msg.showinfo("Status","Record Deleted Succesfully")
                show()
                cursor.execute("TRUNCATE TABLE stock_onhand")
                #cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                doquerry = """
                INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat)
                SELECT supplier.stock_code, supplier.type_material, supplier.amount, IFNULL(out_unique.tot_use, 0), (supplier.amount - IFNULL(out_unique.tot_use, 0))
                FROM supplier
                LEFT JOIN out_unique ON supplier.stock_code = out_unique.stock_code;
                """
                cursor.execute(doquerry)
                con.commit()
                cursor.close()
                con.close();
                
        del_butt = Button(out_window,text='Delete',font=('Arial',13),command =delete)
        del_butt.place(x =265,y = 280)
        
    
    def label_clicked3(event):
        id_user = id_show3.cget("text")
        date_e.delete(0,'end')
        stock_code_e.delete(0,'end')
        usage_e.delete(0,'end')
        date_e.insert(0,date_show3.cget("text"))
        stock_code_e.insert(0,stock_code_show3.cget("text"))
        usage_e.insert(0,usage_show3.cget("text"))
        
    
        def delete():
            if date_e.get()=="":
                Msg.showinfo("Status","Select a ID to Delete")
            else:
                con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
                cursor = con.cursor()
                cursor.execute("delete from out_data where id='"+str(id_user)+"'")
                cursor.execute("commit");
                cursor.execute("TRUNCATE TABLE out_unique")
            
                aggregate_query = """
                INSERT INTO out_unique (stock_code, tot_use)
                SELECT stock_code, SUM(usage_kg) as tot_use
                FROM out_data
                GROUP BY stock_code;
                """
                cursor.execute(aggregate_query)
                con.commit()
                cursor.close()
                
                
                date_e.delete(0,'end')
                stock_code_e.delete(0,'end')
                usage_e.delete(0,'end')
        
                Msg.showinfo("Status","Record Deleted Succesfully")
                show()
                cursor.execute("TRUNCATE TABLE stock_onhand")
                #cursor.execute('INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat) SELECT supplier.stock_code, supplier.type_material, supplier.amount, out_unique.tot_use, (supplier.amount - out_unique.tot_use) FROM supplier INNER JOIN out_unique ON supplier.stock_code = out_unique.stock_code')
                doquerry = """
                INSERT INTO stock_onhand (stock_code, type_mat, in_mat, out_mat, on_handmat)
                SELECT supplier.stock_code, supplier.type_material, supplier.amount, IFNULL(out_unique.tot_use, 0), (supplier.amount - IFNULL(out_unique.tot_use, 0))
                FROM supplier
                LEFT JOIN out_unique ON supplier.stock_code = out_unique.stock_code;
                """
                cursor.execute(doquerry)
                con.commit()
                cursor.close()
                con.close();
                
        del_butt = Button(out_window,text='Delete',font=('Arial',13),command =delete)
        del_butt.place(x =265,y = 280)
    
    
    def reset():
        date_e.delete(0,'end')
        stock_code_e.delete(0,'end')
        usage_e.delete(0,'end')
        
        
    
    id_t=Label(out_window,text='ID',font=('Arial',11),fg='red')
    id_t.place(x=100,y=350)

    date_t=Label(out_window,text='Date',font=('Arial',11),fg='red')
    date_t.place(x=180,y=350)

    stock_code_t=Label(out_window,text='Stock Code',font=('Arial',11),fg='red')
    stock_code_t.place(x=300,y=350)
    
    usage_t=Label(out_window,text='Usage (kg)',font=('Arial',11),fg='red')
    usage_t.place(x=420,y=350)
    
    id_show1=Label(out_window,text='ID',font=('Arial',10))
    id_show1.bind("<Button-1>", label_clicked1)
    id_show1.place(x=100,y=400)

    date_show1=Label(out_window,text='Date',font=('Arial',10))
    date_show1.place(x=180,y=400)

    stock_code_show1=Label(out_window,text='Stock Code',font=('Arial',10))
    stock_code_show1.place(x=300,y=400)
    
    usage_show1=Label(out_window,text='Usage (kg)',font=('Arial',10))
    usage_show1.place(x=420,y=400)
    
    id_show2=Label(out_window,text='ID',font=('Arial',10))
    id_show2.bind("<Button-1>", label_clicked2)
    id_show2.place(x=100,y=450)

    date_show2=Label(out_window,text='Date',font=('Arial',10))
    date_show2.place(x=180,y=450)

    stock_code_show2=Label(out_window,text='Stock Code',font=('Arial',10))
    stock_code_show2.place(x=300,y=450)
    
    usage_show2=Label(out_window,text='Usage (kg)',font=('Arial',10))
    usage_show2.place(x=420,y=450)
    
    id_show3=Label(out_window,text='ID',font=('Arial',10))
    id_show3.bind("<Button-1>", label_clicked3)
    id_show3.place(x=100,y=500)

    date_show3=Label(out_window,text='Date',font=('Arial',10))
    date_show3.place(x=180,y=500)

    stock_code_show3=Label(out_window,text='Stock Code',font=('Arial',10))
    stock_code_show3.place(x=300,y=500)
    
    usage_show3=Label(out_window,text='Usage (kg)',font=('Arial',10))
    usage_show3.place(x=420,y=500)
    
    
    
    
    
    topic=Label(out_window,text='Add a OUT record',font=('Arial',15))
    topic.place(x=420,y=20)
    
    date =Label(out_window,text='Date',font=('Arial',11))
    date.place(x=100,y=120)

    date_e =Entry(out_window,font=('Arial',11))
    date_e.place(x=280,y=120,width = 100)
    
    stock_code =Label(out_window,text='Stock Code',font=('Arial',11))
    stock_code.place(x=100,y=170)

    stock_code_e =Entry(out_window,font=('Arial',11))
    stock_code_e.place(x=280,y=170,width = 100)
    
    usage =Label(out_window,text='Usage (kg)',font=('Arial',11))
    usage.place(x=100,y=220)

    usage_e =Entry(out_window,font=('Arial',11))
    usage_e.place(x=280,y=220,width = 100)
    
    save2_butt = Button(out_window,text='Save',font=('Arial',13),command =savecmd)
    save2_butt.place(x =200,y = 280)
    
    reset2_butt = Button(out_window,text='Reset',font=('Arial',13),command =reset)
    reset2_butt.place(x =340,y = 280)
    show()
    out_window.mainloop()
    
addin_butt = Button(main,text='Add In Record',font=('Arial',10),command =add_in)
addin_butt.place(x =500,y = 7)


addout_butt = Button(main,text='ADD Out Record',font=('Arial',10),command =add_out)
addout_butt.place(x =600,y = 7)

matt_sum=Label(main,text='Material Summery',font=('Arial',15))
matt_sum.place(x=180,y=7)

"Washed CP","Unwashed CP","Treated CP","LEC CP","HEC CP","Black CP","Washed Chips", "Unwashed Chips","Treated Chips","HEC Chips","Washed Crushed","Unwashed Crushed","Crushed CP", "8mm Crush","Fine Dust","Other"

washedcp_lb = Label(main,text="Washed CP",font=('Arial',11))
washedcp_lb.place(x=100,y=50)

washedcp_ans = Label(main,text="",font=('Arial',11))
washedcp_ans.place(x=300,y=50)

unwashedcp_lb = Label(main,text="Unwashed CP",font=('Arial',11))
unwashedcp_lb.place(x=100,y=90)

unwashedcp_ans = Label(main,text="",font=('Arial',11))
unwashedcp_ans.place(x=300,y=90)

treatedcp_lb = Label(main,text="Treated CP",font=('Arial',11))
treatedcp_lb.place(x=100,y=130)

treatedcp_ans = Label(main,text="",font=('Arial',11))
treatedcp_ans.place(x=300,y=130)

leccp_lb = Label(main,text="LEC CP",font=('Arial',11))
leccp_lb.place(x=100,y=170)

leccp_ans = Label(main,text="",font=('Arial',11))
leccp_ans.place(x=300,y=170)

heccp_lb = Label(main,text="HEC CP",font=('Arial',11))
heccp_lb.place(x=100,y=210)

heccp_ans = Label(main,text="",font=('Arial',11))
heccp_ans.place(x=300,y=210)

blackcp_lb = Label(main,text="Black CP",font=('Arial',11))
blackcp_lb.place(x=100,y=250)

blackcp_ans = Label(main,text="",font=('Arial',11))
blackcp_ans.place(x=300,y=250)

washedchips_lb = Label(main,text="Washed Chips",font=('Arial',11))
washedchips_lb.place(x=100,y=290)

washedchips_ans = Label(main,text="",font=('Arial',11))
washedchips_ans.place(x=300,y=290)

unwashedchips_lb = Label(main,text="Unwashed Chips",font=('Arial',11))
unwashedchips_lb.place(x=100,y=330)

unwashedchips_ans = Label(main,text="",font=('Arial',11))
unwashedchips_ans.place(x=300,y=330)

treatedchips_lb = Label(main,text="Treated Chips",font=('Arial',11))
treatedchips_lb.place(x=100,y=370)

treatedchips_ans = Label(main,text="",font=('Arial',11))
treatedchips_ans.place(x=300,y=370)

hecchips_lb = Label(main,text="HEC Chips",font=('Arial',11))
hecchips_lb.place(x=100,y=410)

hecchips_ans = Label(main,text="",font=('Arial',11))
hecchips_ans.place(x=300,y=410)

washed_crushed_lb = Label(main,text="Washed Crushed",font=('Arial',11))
washed_crushed_lb.place(x=100,y=450)

washed_crushed_ans = Label(main,text="",font=('Arial',11))
washed_crushed_ans.place(x=300,y=450)

unwashedcrushed_lb = Label(main,text="Unwashed Crushed",font=('Arial',11))
unwashedcrushed_lb.place(x=100,y=490)

unwashedcrushed_ans = Label(main,text="",font=('Arial',11))
unwashedcrushed_ans.place(x=300,y=490)

crushed_cp_lb = Label(main,text="Crushed CP",font=('Arial',11))
crushed_cp_lb.place(x=100,y=530)

crushed_cp_ans = Label(main,text="",font=('Arial',11))
crushed_cp_ans.place(x=300,y=530)

mmcrush_lb = Label(main,text="8mm Crush",font=('Arial',11))
mmcrush_lb.place(x=100,y=570)

mmcrush_ans = Label(main,text="",font=('Arial',11))
mmcrush_ans.place(x=300,y=570)

finedust_lb = Label(main,text="Fine Dust",font=('Arial',11))
finedust_lb.place(x=100,y=610)

finedust_ans = Label(main,text="",font=('Arial',11))
finedust_ans.place(x=300,y=610)

other_lb = Label(main,text="Other",font=('Arial',11))
other_lb.place(x=100,y=650)

other_ans = Label(main,text="",font=('Arial',11))
other_ans.place(x=300,y=650)


def refresh():
    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Treated CP';")
    rows = cursor.fetchall()
    treated_tot= 0
    for row in rows:
        treated_tot = row[4]+treated_tot
    treatedcp_ans.config(text=treated_tot)
    cursor.close()


    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Washed CP';")
    rows = cursor.fetchall()
    washedcp_tot= 0
    for row in rows:
        washedcp_tot = row[4]+washedcp_tot
    washedcp_ans.config(text=washedcp_tot)
    cursor.close()

    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Unwashed CP';")
    rows = cursor.fetchall()
    unwashedcp_tot= 0
    for row in rows:
        unwashedcp_tot = row[4]+unwashedcp_tot
    unwashedcp_ans.config(text=unwashedcp_tot)
    cursor.close()


    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'LEC CP';")
    rows = cursor.fetchall()
    leccp_tot= 0
    for row in rows:
        leccp_tot = row[4]+leccp_tot
    leccp_ans.config(text=leccp_tot)
    cursor.close()

    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'HEC CP';")
    rows = cursor.fetchall()
    heccp_tot= 0
    for row in rows:
        heccp_tot = row[4]+heccp_tot
    heccp_ans.config(text=heccp_tot)
    cursor.close()

    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Black CP';")
    rows = cursor.fetchall()
    blackcp_tot= 0
    for row in rows:
        blackcp_tot = row[4]+blackcp_tot
    blackcp_ans.config(text=blackcp_tot)
    cursor.close()


    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Washed Chips';")
    rows = cursor.fetchall()
    washchips_tot= 0
    for row in rows:
        washchips_tot = row[4]+washchips_tot
    washedchips_ans.config(text=washchips_tot)
    cursor.close()


    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Unwashed Chips';")
    rows = cursor.fetchall()
    unwashchips_tot= 0
    for row in rows:
        unwashchips_tot = row[4]+unwashchips_tot
    unwashedchips_ans.config(text=unwashchips_tot)
    cursor.close()


    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Treated Chips';")
    rows = cursor.fetchall()
    treatedchips_tot= 0
    for row in rows:
        treatedchips_tot = row[4]+treatedchips_tot
    treatedchips_ans.config(text=treatedchips_tot)
    cursor.close()


    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'HEC Chips';")
    rows = cursor.fetchall()
    hecchips_tot= 0
    for row in rows:
        hecchips_tot = row[4]+hecchips_tot
    hecchips_ans.config(text=hecchips_tot)
    cursor.close()

    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Washed Crushed';")
    rows = cursor.fetchall()
    washedcrushed_tot= 0
    for row in rows:
        washedcrushed_tot = row[4]+washedcrushed_tot
    washed_crushed_ans.config(text=washedcrushed_tot)
    cursor.close()

    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Unwashed Crushed';")
    rows = cursor.fetchall()
    unwashedcrushed_tot= 0
    for row in rows:
        unwashedcrushed_tot = row[4]+unwashedcrushed_tot
    unwashedcrushed_ans.config(text=unwashedcrushed_tot)
    cursor.close()

    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Crushed CP';")
    rows = cursor.fetchall()
    crushedcp_tot= 0
    for row in rows:
        crushedcp_tot = row[4]+crushedcp_tot
    crushed_cp_ans.config(text=crushedcp_tot)
    cursor.close()

    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = '8mm Crush';")
    rows = cursor.fetchall()
    mmcrush_tot= 0
    for row in rows:
        mmcrush_tot = row[4]+mmcrush_tot
    mmcrush_ans.config(text=mmcrush_tot)
    cursor.close()

    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Fine Dust';")
    rows = cursor.fetchall()
    findust_tot= 0
    for row in rows:
        findust_tot = row[4]+findust_tot
    finedust_ans.config(text=findust_tot)
    cursor.close()


    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM stock_onhand WHERE type_mat = 'Other';")
    rows = cursor.fetchall()
    other_tot= 0
    for row in rows:
        other_tot = row[4]+other_tot
    other_ans.config(text=other_tot)
    cursor.close()
    con.close()

ref_butt = Button(main,text='Refresh',font=('Arial',13),command =refresh)
ref_butt.place(x =400,y = 7)

def searchgo():
    stokk = stock_e.get()
    con = mysql.connect(host="localhost",user ="root",password="thepigtail",database = "supplier_identi")
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM supplier WHERE stock_code ='"+str(stokk)+"';")
    rows = cursor.fetchall()
    
    prodate_ans.config(text=rows[0][1])
    suup_ans.config(text=rows[0][2])
    mate_ans.config(text=rows[0][4])
    ecv_ans.config(text=rows[0][5])
    moistv_ans.config(text=rows[0][6])
    fib_ans.config(text=rows[0][7])
    qcby_ans.config(text=rows[0][9])
    storagea_ans.config(text=rows[0][10])
    
    
    cursor.execute(f"SELECT * FROM stock_onhand WHERE stock_code ='"+str(stokk)+"';")
    cols = cursor.fetchall()
    amo_ans.config(text=cols[0][4])
    cursor.close()
    con.close()
    

stock_e =Entry(main,font=('Arial',11))
stock_e.place(x=850,y=70,width = 100)
search_now = Button(main,text='Search',font=('Arial',13),command =searchgo)
search_now.place(x =960,y = 63)

prodate_lb = Label(main,text="Date :",font=('Arial',11))
prodate_lb.place(x=840,y=150)

prodate_ans = Label(main,text="",font=('Arial',11))
prodate_ans.place(x=980,y=150)

suup_lb = Label(main,text="Supplier Code :",font=('Arial',11))
suup_lb.place(x=840,y=200)

suup_ans = Label(main,text="",font=('Arial',11))
suup_ans.place(x=980,y=200)


mate_lb = Label(main,text="Material Type :",font=('Arial',11))
mate_lb.place(x=840,y=250)

mate_ans = Label(main,text="",font=('Arial',11))
mate_ans.place(x=980,y=250)

ecv_lb = Label(main,text="EC Value :",font=('Arial',11))
ecv_lb.place(x=840,y=300)

ecv_ans = Label(main,text="",font=('Arial',11))
ecv_ans.place(x=980,y=300)

moistv_lb = Label(main,text="Moisture Value :",font=('Arial',11))
moistv_lb.place(x=840,y=350)

moistv_ans = Label(main,text="",font=('Arial',11))
moistv_ans.place(x=980,y=350)

fib_lb = Label(main,text="Fiber Value :",font=('Arial',11))
fib_lb.place(x=840,y=400)

fib_ans = Label(main,text="",font=('Arial',11))
fib_ans.place(x=980,y=400)


amo_lb = Label(main,text="On hand amount :",font=('Arial',11))
amo_lb.place(x=840,y=450)

amo_ans = Label(main,text="",font=('Arial',11))
amo_ans.place(x=980,y=450)

qcby_lb = Label(main,text="QC By :",font=('Arial',11))
qcby_lb.place(x=840,y=500)

qcby_ans = Label(main,text="",font=('Arial',11))
qcby_ans.place(x=980,y=500)

storagea_lb = Label(main,text="Storage Area :",font=('Arial',11))
storagea_lb.place(x=840,y=550)

storagea_ans = Label(main,text="",font=('Arial',11))
storagea_ans.place(x=980,y=550)


main.mainloop()
