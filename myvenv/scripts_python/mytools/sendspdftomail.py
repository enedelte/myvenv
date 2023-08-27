import smtplib
import win32com.client as win32
import pandas as pd
import csv
import os

outlook = win32.Dispatch("Outlook.Application")

mail= outlook.CreateItem(0)

mail.To = "daalejoar@gmail.com"
mail.Subject = "Correo prueba"
mail.Body = "Mensaje de prueba"
mail.Send()


print("Correo enviado")