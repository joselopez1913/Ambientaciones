import rsa
from getpass import getpass
import os

"""
Created on Fri Oct 28 12:00:44 2022

@author: jalleyne
"""

def genKeys():
    """Función para generar las keys pública y privada

    Returns:
        pubKey,privKey (tupla): Llaves públicas y privada
    """
    pubKey, privKey = rsa.newkeys(2048)
    publicKeyPkcs1PEM = pubKey.save_pkcs1().decode('utf8') 
    privateKeyPkcs1PEM = privKey.save_pkcs1().decode('utf8') 

    with open('C:\Pass\pubKey.txt','w') as f:
        f.write(publicKeyPkcs1PEM)

    with open('C:\Pass\privKey.txt','w') as f:
        f.write(privateKeyPkcs1PEM)
    return pubKey,privKey

def genPassword(password):  
    """Función para generar la contraseña encriptada

    Args:
        password (String): Contraseña de red
    """
    pubKey,privKey=genKeys()
    with open('C:\Pass\pass.txt','wb') as f:
        f.write(rsa.encrypt(password.encode('utf8'),pubKey))

def genUser(user):
    """Función para generar el txt con el usuario

    Args:
        user (String): Nombre de usuario banco
    """ 
    with open(r'C:\Pass\user.txt','w') as f:
        f.write(user)

def validateFolder():
    """Función para validar si existe el Path
    """
    if not(os.path.exists(r'C:\Pass')):
        os.makedirs(r'C:\Pass')

validateFolder()
print('Ingrese su usuario y contraseña de red')
print('Usuario: ',end='')
user=input()
password=getpass()

genUser(user)
genPassword(password)

# with open('C:\Pass\pass.txt','rb') as f:
#     password=rsa.decrypt(f.read(),privateKeyReloaded).decode('utf8')

