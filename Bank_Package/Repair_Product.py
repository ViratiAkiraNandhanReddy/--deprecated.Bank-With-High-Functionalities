# import tkinter as tk
# from time import sleep


# class Loading_Data_Finding:
    
#     def clr_1():
#         Grey.grid(row=0,column=0,padx=60,pady=60)
        
#     def clr_2():
#         Dark_Red.grid(row=0,column=0,padx=60,pady=60)
#         Grey.destroy()

#     def clr_3():
#         Orange.grid(row=0,column=0,padx=60,pady=60)
#         Dark_Red.destroy()

#     def clr_4():
#         Yellow.grid(row=0,column=0,padx=60,pady=60)
#         Orange.destroy()

#     def clr_5():
#         Green.grid(row=0,column=0,padx=60,pady=60)
#         Yellow.destroy()

#     def clr_6():
#         Indigo.grid(row=0,column=0,padx=60,pady=60)
#         Green.destroy()

#     def clr_7():
#         Brown.grid(row=0,column=0,padx=60,pady=60)
#         Indigo.destroy()

#     def clr_8():
#         Gold.grid(row=0,column=0,padx=60,pady=60)
#         Brown.destroy()

#     def clr_9():
#         Lime.grid(row=0,column=0,padx=60,pady=60)
#         Gold.destroy()

#     def clr_10():
#         Lavender.grid(row=0,column=0,padx=60,pady=60)
#         sleep(0.2)
#         Loading.destroy()
        

#     global Loading
#     Loading = tk.Tk()
#     Loading.resizable(False,False)
#     Loading.geometry('240x185')
#     Loading.config(bg='Black')

#     global Grey,Dark_Red,Orange,Yellow,Green,Indigo,Brown,Gold,Lime,Lavender
#     White = tk.Label(Loading,text='Loading.',font=('Roboto 18 bold'),fg='White',bg='Black')
#     White.grid(row=0,column=0,padx=60,pady=60)
#     Grey = tk.Label(Loading,text='Loading..',font=('Roboto 18 bold'),fg='Grey',bg='Black')
#     Grey.after(100,clr_1)
#     Dark_Red = tk.Label(Loading,text='Loading...',font=('Roboto 18 bold'),fg='Dark Red',bg='Black')
#     Dark_Red.after(600,clr_2)
#     Orange = tk.Label(Loading,text='Loading.',font=('Roboto 18 bold'),fg='Orange',bg='Black')
#     Orange.after(1200,clr_3)
#     Yellow = tk.Label(Loading,text='Loading..',font=('Roboto 18 bold'),fg='Yellow',bg='Black')
#     Yellow.after(1800,clr_4)
#     Green = tk.Label(Loading,text='Loading...',font=('Roboto 18 bold'),fg='Green',bg='Black')
#     Green.after(2400,clr_5)
#     Indigo = tk.Label(Loading,text='Loading.',font=('Roboto 18 bold'),fg='Indigo',bg='Black')
#     Indigo.after(3000,clr_6)
#     Brown = tk.Label(Loading,text='Loading..',font=('Roboto 18 bold'),fg='Brown',bg='Black')
#     Brown.after(3600,clr_7)
#     Gold = tk.Label(Loading,text='Loading...',font=('Roboto 18 bold'),fg='Gold',bg='Black')
#     Gold.after(4200,clr_8)
#     Lime = tk.Label(Loading,text='Loading.',font=('Roboto 18 bold'),fg='Lime',bg='Black')
#     Lime.after(4800,clr_9)
#     Lavender = tk.Label(Loading,text='Loading..',font=('Roboto 18 bold'),fg='Lavender',bg='Black')
#     Lavender.after(5400,clr_10)
    
#     Loading.mainloop()

# class User_Data_Lost:
#     pass

# def User_Data_Not_Found():
#     try:
#         with open(r'Bank_Package\Data_Of_User.txt','r') as Data:
#             Recovered_Data = Data.read()
        
#     except:
#         Not_Found = tk.Tk()
#         Not_Found.title('Data Corrupted')
#         Not_Found.geometry('500x300')
#         Not_Found.resizable(False,False)
#         Not_Found.config(bg='#EDB1B1')
#         tk.Label(Not_Found,text='Backup Data Corrupted!',bg='#EDB1B1',font=('Roboto 16 bold')).pack()
#         Not_Found.mainloop()
#     finally:
#         pass
#     print(Recovered_Data)



# #Satisfied Code Completion:8%     
# '''                                                            End Of Program                                                                 '''
# # Loading_Data_Finding()