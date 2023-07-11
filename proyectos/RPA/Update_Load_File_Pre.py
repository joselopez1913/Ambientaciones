# -*- coding: utf-8 -*-

from cgitb import text
from fileinput import filename
from unittest import skip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import rsa


"""
Created on Wed Aug 24 10:46:15 2022

@author: jalleyne
"""
fileName='Ambientacion.xlsx'
ocNumber='Objeto modificado para ambientación'
driver=webdriver.Chrome('C:\Proyectos\chromedriver.exe')
wait=WebDriverWait(driver,10)
waitScenario=WebDriverWait(driver,3)
waitSaved=WebDriverWait(driver,2)

driver.get('https://precontrollerview.bancolombia.corp:8443/cv/ui/global/index')

def getPassword():
    """Función para decodificar la contraseña del usuario de red

    Returns:
        password (string): contraseña desencriptada
    """
    try:
        with open('\Pass\privKey.txt') as f:
            privateKeyReloaded = rsa.PrivateKey.load_pkcs1(f.read().encode('utf8'))
        with open('\Pass\pass.txt','rb') as f:
            password=rsa.decrypt(f.read(),privateKeyReloaded).decode('utf8')
    except:
        print('Por favor primero corra el Setup')
        password=''
    return password

def doLogin():
    '''

    Returns
    -------
    status : Int
        Retorna 1 si se logea correctamente y -1 si no.

    '''
    status=-1
    try:
        userNameInput=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/form[1]/div[1]/input[2]')))
        passwordInput=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/form[1]/div[2]/input')))    
        userNameInput.send_keys('jolocast')    
        password= getPassword()      
        passwordInput.send_keys(password)    
        loginBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/form[1]/div[4]/input')))    
        loginBtn.click()
        status=1
    except:
        status=-1
    return status

def editErrorFile(dsName):
    """Función para generar TXT con reporte de errores

    Args:
        dsName (String): Nombre del DS que generó error

    Returns:
        None: none
    """
    with open('DS_ERROR.txt') as f:
        text=f.read()
    with open('DS_ERROR.txt', 'w') as f:
        f.write(text)
        f.write('\n')
        f.write(dsName)
    return None

def openDataSource(dataSourceName,branchName,projectName):
    status=-1
    type='CARGA DE ARCHIVO'
    url='https://precontrollerview.bancolombia.corp:8443/cv/ui/branch/{0}/{1}/configure?oType=DataSource&oName={2}'.format(
        projectName,branchName,dataSourceName) 
    try:
        # dsNameLbl=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[2]')))
        # dsNameLbl.click()
        # anotherDsBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[1]/div/div/div/div[2]/div/div/span/div')))
        # anotherDsBtn.click()
        # searchDataSourceInput=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[2]/div/input')))
        # searchDataSourceInput.send_keys(name)
        # time.sleep(1)
        # dataSourceBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[1]/div/div/div/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[2]')))
        # dataSourceBtn.click()
        # time.sleep(1)
        driver.get(url)
        loadersBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[3]/div/div')))
        loadersBtn.click()
        status=1
        conexionDirecta=waitScenario.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='ConexionDirectaMigracion']")))
        type='CONEXION DIRECTA'
    except:
        print('Carga de archivo')
    return status,type
    
def populateDefault(dataSource,tipoCarga):
    status=-1
    try:
        if(tipoCarga=='CONEXION DIRECTA'):
            loadersBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[3]/div/div')))
            loadersBtn.click()
            #scenarioBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div[1]/span/div')))
            scenarioBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/span/div')))
            scenarioBtn.click()
        elif(tipoCarga=='CARGA DE ARCHIVO'):
            dbSourceList=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[2]')))
            dbSourceList.click()
            cv9Lbl=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[text()='CV9_PROD_CNXREPLP']")))
            cv9Lbl.click()
        time.sleep(2)
        selectAllCheck=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[1]/div')))
        selectAllCheck.click()
        populateDefaultLbl=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div[3]/span')))
        populateDefaultLbl.click()
        saveBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div[2]/div')))
        saveBtn.click()
        commentInput=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/textarea')))
        commentInput.send_keys(f'Modificación del escenario de carga para migración OC {ocNumber}.')
        confirmSaveBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[1]/div/div[3]/div[1]/span/div/span')))
        time.sleep(1)
        confirmSaveBtn.click()
        time.sleep(1)
        status=isDSSaved()
    except:
        status=-1
        print('error en DS',dataSource)
        # editErrorFile(dataSource)
    return status

def isDSSaved():
    status=-1
    try:
        savedButton=waitSaved.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div[2]/div')))
        print('Encontrado el botón de guardado')
    except:
        status=1
    return status

def changeLoaderType(dataSource):
    status=-1
    try:
        loadersBtn=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[3]/div/div')))
        loadersBtn.click()
        addScenarioBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/div[2]/span')))
        addScenarioBtn.click()
        addTableScenarioBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[1]/div/div[1]/div[1]/div[2]/span[1]')))
        addTableScenarioBtn.click()
        tableScenarioNameInput=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/input')))
        tableScenarioNameInput.clear()
        time.sleep(1)
        tableScenarioNameInput.send_keys('ConexionDirectaMigracion')
        time.sleep(1)
        tableScenarioCreateBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[3]/div[1]/div[1]/div/div[2]/div[1]')))
        tableScenarioCreateBtn.click()
        newScenarioBtn=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/div[1]/div[1]/span/div/span[1]')))
        newScenarioBtn.click()
        status=1 if populateDefault(dataSource,'CARGA DE ARCHIVO')==1 else print('error')
    except:
        status=-1
        print('error en DS',dataSource)
    return status

def readDataSourceList():
    # df=pd.read_excel('LOAD_INFO_TYPE_LOAD_DS_DM_prueba.xlsx')
    df=pd.read_excel(fileName)
    dataSources=df.values.tolist()
    print('DataSources leídos')
    return dataSources

def updateDataSourceList(dsList):
    '''

    Parameters
    ----------
    procesos : List
        Lista de DataSources.

    Returns
    -------
    None.

    '''
    columnas=['projectName','branchName','objectName','status']
    df=pd.DataFrame(dsList,columns=columnas)
    df.to_excel(fileName, index=False,header=True)
    return None
    
def main():
    dataSources=readDataSourceList()
    contador=0
    for dataSource in dataSources:
        contador+=1
        globalStatus=0
        if not('Aggregation' in dataSource[2] or 'FreeForm' in dataSource[2] or 'Calendar-' in dataSource[2] or 'Portfolio-' in dataSource[2]):
            print(f'iteración: {dataSource[2]}')
            if not(dataSource[3]==1):
                status,type=openDataSource(dataSource[2],dataSource[1],dataSource[0])
                if (status==1):
                    if (type=='CARGA DE ARCHIVO'):
                        globalStatus=changeLoaderType(dataSource[2])
                    elif (type=='CONEXION DIRECTA'):
                        globalStatus=populateDefault(dataSource[2],'CONEXION DIRECTA')
                else:
                    print('error abriendo el DataSource')
                dataSources[contador-1][3]=globalStatus
                print(dataSource[2],dataSource[3])
                # if (dataSource[4]=='CARGA DE ARCHIVO'):
                #     status=changeLoaderType() if openDataSource(dataSource[3],dataSource[2],dataSource[1])==1 else print('error abriendo DS')
                #     print('carga de archivo')
                # elif(dataSource[4]=='CONEXION DIRECTA'):
                #     print('conexion directa')
                #     status=populateDefault(dataSource[4]) if openDataSource(dataSource[3],dataSource[2],dataSource[1])==1 else print('error abriendo DS')
    updateDataSourceList(dataSources)
    return globalStatus
            
main() if doLogin()==1 else print('error')
    
# changeLoaderType() if (openFirstDataSource('AAS_DIA_CDT') if doLogin()==1 else print('error haciendo login'))==1 else print('error editando el DS')
# changeLoaderType()

