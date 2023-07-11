# -*- coding: utf-8 -*-

import requests
from requests.adapters import HTTPAdapter, Retry
import json
import pandas as pd
import time
from datetime import datetime
import email_module
import rsa
import urllib3


"""
Created on Thu Aug 18 08:50:44 2022

@author: jalleyne
"""
#dia=input('Ingrese el día en el que desea que se ejecute el Script ')
#url='https://precontrollerview.bancolombia.corp:8443/cv'
url='https://precontrollerview.bancolombia.corp:8443/cv'
file=r'C:\Users\jolocast\Downloads\Ambientaciones\Ambientacion.xlsx'


def getPassword():
    """Función para decodificar la contraseña del usuario de red

    Returns:
        password (string): contraseña desencriptada
    """
    try:
        with open('C:\Pass\privKey.txt') as f:
            privateKeyReloaded = rsa.PrivateKey.load_pkcs1(f.read().encode('utf8'))
        with open('C:\Pass\pass.txt','rb') as f:
            password=rsa.decrypt(f.read(),privateKeyReloaded).decode('utf8')
    except:
        print('Por favor primero corra el Setup')
        password=''
    return password

def getUser():
    """Función para obtener el usuario de red

    Returns:
        user (String): Nombre de usuario
    """
    with open(r'C:\Pass\user.txt') as f:
        user=f.read()
    return user


def getHdrs():
   '''

    Returns
    -------
    hdrs : Dictionary
        Headers con la autenticación para la petición.

    '''
   hdrs={'content-type':'text/xml',
            'directoryname':'LDAP',
            'username':getUser(),
            'password':getPassword(),
            'Accept':'application/json'}
   return hdrs

def createRequestBody(project, branch, asof_date,name,processId,table,partition):
    """Función para generar el Body de la petición

    Args:
        project (String): Proyecto que contiene el WF ejecutar
        branch (String): Branch que contiene el WF a ejecutar
        asof_date (String): As Of Date de la ejecución
        name (String): Nombre del WF a ejecutar
        processId (String): ID del proceso en el AXSL
        variables (String): Variables de ejecución del WF

    Returns:
        Body(String): Body para ser usado en la petición
    """
    
    if(True):
        body='''
        <object type="TaskSpec" version="1.0">
            <property name="projectName" value="{0}" valueType="string" />
            <property name="branchName" value="{1}" valueType="string" />
            <property name="taskType" value="WorkFlow" valueType="string" />
            <property name="asOfDate" value="{2}" valueType="date"/>
            <property name="underlyingObject" valueType="url">WorkFlow["{3}"]</property>
            <property name="nonKeyParameters" valueType="object">
                <object type="Task:nonKeyParameters" version="1.0">
                    <property name="id" value="{4}" valueType="string"/>
                    <property name="archivalFrequency" value="AMBIENTACIONES" valueType="string"/>
                    <property name="specificDelegate" valueType="object">
                        <object type="WorkFlow:taskNonKeyParameters" version="1.0">
                            <property name="restartAllModules" value="false" valueType="boolean"/>
                            <property name="variables" valueType="table"/>
                        </object>
                    </property>
                </object>
        </property>
        <property name="instanceKeyValues" valueType="table">
            <object type="InstanceKeyValue" version="1.0">
                <property name="name" value="version" valueType="string"/>
                <property name="keyValueType" value="INTEGER" valueType="string"/>
                <property name="keyValue" value="0" valueType="string"/>
            </object>
            <object type="InstanceKeyValue" version="1.0">
                <property name="name" value="filing_version" valueType="string"/>
                <property name="keyValueType" value="INTEGER" valueType="string"/>
                <property name="keyValue" value="0" valueType="string"/>
            </object>
            </property>
            <property name="keyParameters" valueType="object">
                <object type="WorkFlow:taskKeyParameters" version="1.0">
                    <property name="streams" valueType="table" />
                    <property name="variables" valueType="table">
                        <object type="Variable:value" version="[1.0]">
                            <property name="name" value="table" valueType="string"/>
                            <property name="stringValue" value="{5}" valueType="string"/>
                        </object>
                        <object type="Variable:value" version="[1.0]">
                            <property name="name" value="partition" valueType="string"/>
                            <property name="stringValue" value="{6}" valueType="string"/>
                        </object>
                    </property>
			        <property name="inMemoryExecution" value="false" valueType="boolean" />
		        </object>
	        </property> 

</object>
            '''.format(project,branch,asof_date,name,processId,table,partition)
    else: 
        #nombreVariable,valor=variables.split('=')
        body='''
        <object type="TaskSpec" version="1.0">
            <property name="projectName" value="{0}" valueType="string" />
            <property name="branchName" value="{1}" valueType="string" />
            <property name="taskType" value="WorkFlow" valueType="string" />
            <property name="asOfDate" value="{2}" valueType="date"/>
            <property name="underlyingObject" valueType="url">WorkFlow["{3}"]</property>
            <property name="nonKeyParameters" valueType="object">
                <object type="Task:nonKeyParameters" version="1.0">
                    <property name="id" value="{4}" valueType="string"/>
                    <property name="archivalFrequency" value="" valueType="string"/>
                    <property name="specificDelegate" valueType="object">
                        <object type="WorkFlow:taskNonKeyParameters" version="1.0">
                            <property name="restartAllModules" value="false" valueType="boolean"/>
                            <property name="variables" valueType="table"/>
                        </object>
                    </property>
                </object>
        </property>
        <property name="instanceKeyValues" valueType="table">
            <object type="InstanceKeyValue" version="1.0">
                <property name="name" value="version" valueType="string"/>
                <property name="keyValueType" value="INTEGER" valueType="string"/>
                <property name="keyValue" value="0" valueType="string"/>
            </object>
            <object type="InstanceKeyValue" version="1.0">
                <property name="name" value="filing_version" valueType="string"/>
                <property name="keyValueType" value="INTEGER" valueType="string"/>
                <property name="keyValue" value="0" valueType="string"/>
            </object>
            </property>
            <property name="keyParameters" valueType="object">
                <object type="WorkFlow:taskKeyParameters" version="1.0">
                    <property name="streams" valueType="table" />
                    <property name="variables" valueType="table">
                        <object type="Variable:value" version="[1.0]">
                            <property name="name" value="{5}" valueType="string"/>
                            <property name="stringValue" value="{6}" valueType="string"/>
                        </object>
                    </property>
                    <property name="inMemoryExecution" value="false" valueType="boolean" />
                </object>
            </property> 

        </object>
            '''.format(project,branch,asof_date,name,processId,nombreVariable,valor)
    return body

def startTask(body):
    '''
    Parameters
    ----------
    body : String
        Body en XML de la petición para iniciar ejecución de WF.

    Returns
    -------
    taskId : String
        ID de la tarea y la Branch resultante de la ejecución.

    '''
    link=f'{url}/rest/global/task/startTask'
    
    #try:
    session = requests.Session()
    retry = Retry(connect=10, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    r=session.post(link,body,headers=getHdrs(),verify=False)
    print(r.text)
    response=json.loads(r.text)
    if(response['PROPERTIES']['responseStatus']['value']!=-1):
        taskId=response['PROPERTIES']['responseMessage']['value'].split('[')[1][:-2]
        print('id de la tarea resultante: '+taskId)
    else:
        taskId=''
    # except:
    #     print('ha ocurrido un error intentando ejecutar la petición')
    #     taskId=''

    return taskId

def getTaskStatus(taskId):
    '''
    Parameters
    ----------
    taskId : String
        ID de la tarea y la Branch resultante de la ejecución.

    Returns
    -------
    status : String
        Estado de ejecución de la tarea.

    '''
    if(taskId!=''):
        task,branch=taskId.split('@')
        parameters={'branchId':branch,
                'taskId':task}
        link=f'{url}/rest/global/task/taskStatus'
       
        try:
            urllib3.disable_warnings()
            session = requests.Session()
            retry = Retry(connect=10, backoff_factor=1)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            r=session.get(link,params=parameters,headers=getHdrs(), verify=False)
            #print('código de respuesta: '+r.text)
            response=json.loads(r.text)
            status=response['PROPERTIES']['status']['value']
            print('estado de la tarea: '+status)
        except:
            print('Ha ocurrido un error para obtener el estado de la tarea')
            status='START'

    else:
        status='NONE'
    return status

def readAXSL():
    '''

    Returns
    -------
    procesos : List
        Lista de procesos a ejecutar en el día.

    '''

    df=pd.read_excel(file)
    procesos=df.values.tolist()
    print('AXSL leído')
    return procesos

def updateAXSL(procesos):
    '''

    Parameters
    ----------
    procesos : List
        Lista de procesos diarios del AXSL.

    Returns
    -------
    None.

    '''
    columnas=['PROJECT_NAME','BRANCH_NAME','OBJECT_NAME','OBJECT_AS_OF_DATE','TABLE_NAME','PARTITION_NAME','INSTANCE_KEYS','STATUS','TASK_ID','START_TIME','FINISH_TIME','EXEC_TIME']
    df=pd.DataFrame(procesos,columns=columnas)
    try:
        df.to_excel(r'C:\Users\jolocast\Downloads\Ambientaciones\Ambientacion_resultado.xlsx', index=False,header=True)
        print('aqui guarda')
    except:
        print('Por favor cierre el archivo de Excel')
    return None

def updateTaskStatus(procesos,fila,newStatus):
    print('updateTaskStatus')
    '''


    Parameters
    ----------
    procesos : List
        Lista con los procesos diarios del AXSL.
    fila : Int
        Número de la fila que se va a actualizar.
    newStatus : String
        Nuevo estado de ejecución (ACTIVE,ERROR,NONE,KILLED).

    Returns
    -------
    procesos : List
        Lista actualizada con los procesos diarios del AXSL.

    '''
    procesos[fila][7]=newStatus
    print('Se actualizó el estátus de la tarea {0} a {1}'.format(procesos[fila][2],
                                                                 newStatus))
    if(newStatus=='START'):
        procesos[fila][9]=time.strftime("%H:%M:%S")
    elif(newStatus=='ACTIVE' or newStatus=='WARNING' or newStatus=='KILLED' or newStatus=='ERROR'):
        procesos[fila][10]=time.strftime("%H:%M:%S")
        FMT = '%H:%M:%S'
        procesos[fila][9]=time.strftime("%H:%M:%S") if pd.isna(procesos[fila][9]) else procesos[fila][9]
        tdelta = datetime.strptime(procesos[fila][10], FMT) - datetime.strptime(procesos[fila][9], FMT)
        procesos[fila][11]=str(tdelta)
    
    print(procesos)

    return procesos

def updateTaskId(procesos,fila,newId):
    print('updateTaskId')
    '''

    Parameters
    ----------
    procesos : List
        Lista con los procesos diarios del AXSL.
    fila : Int
        Número de la fila que se va a actualizar.
    newId : TYPE
        Nuevo Id de ejecución.

    Returns
    -------
    procesos : List
        Lista actualizada con los procesos diarios del AXSL.

    '''
    procesos[fila][8]=newId
    print('Se actualizó el Id de ejecución de la tarea {0} a {1}'.format(procesos[fila][0],
                                                                         newId))
    return procesos

def validateTaskStatus(procesos):
    print('validateTaskStatus')
    '''

    Parameters
    ----------
    procesos : List
        Lista con los procesos diarios del AXSL.

    Returns
    -------
    procesos : List
        Lista actualizada con los procesos diarios del AXSL.

    '''
    fila=0
    for proceso in procesos:
        fila+=1
        processStatus=proceso[7]
        taskId=proceso[8]
        if(processStatus=='START' or processStatus=='WAITING'):
            if(not pd.isna(taskId)):
                status=getTaskStatus(taskId)
                if(status!='START' and status!='WAITING'):
                    updateTaskStatus(procesos, fila-1, status)
                    if(status=='ERROR'):
                        #email_module.sendFinishedStatus(proceso, status)
                        print('Status=ERROR')
    print(procesos)
    return procesos

def checkPredecesor(nombrePredecesor,procesos):
    print('checkPredecesor')
    '''

    Parameters
    ----------
    nombrePredecesor : String
        Nombre del proceso predecesor.
    procesos : List
        Lista con los procesos diarios del AXSL.

    Returns
    -------
    active : Boolean
        Booleano que determina si el predecesor ya terminó o no.

    '''
    active=False
    for proceso in procesos:
        processName=proceso[2]
        if(processName.strip()==nombrePredecesor):
            processStatus=proceso[6]
            if(processStatus=='ACTIVE' or processStatus=='WARNING'):
                active=True
    return active

def runProcess(proceso,fila,procesos):
    print('runProcess')
    '''

    Parameters
    ----------
    proceso : List
        Proceso que se va a ejecutar.
    fila : Integer
        Número de la fila del proceso a ejecutar.
    procesos : List
        Lista con los procesos diarios del AXSL.

    Returns
    -------
    procesos : List
        Lista actualizada con los procesos diarios del AXSL.

    '''
    projectName=proceso[0]
    branchName=proceso[1]
    processName=proceso[2]
    wfName='WF_MG_'+processName
    print('Ejecutando',wfName)
    print(procesos)
    #asof_date='2023-03-31 00:00:00' 
    asof_date=proceso[3]
    #day=time.localtime().tm_mday
    #print(day)
    #asof_date=time.strftime('%Y-%m-{0} 00:00:00.0'.format(day))
    print(asof_date)
    table=proceso[4]
    partition=proceso[5]
    body=createRequestBody(projectName,branchName,asof_date,wfName,processName,table,partition)
    taskId=startTask(body)
    if (taskId!=''):
        procesos=updateTaskStatus(procesos,fila-1,'START')
        procesos=updateTaskId(procesos,fila-1,taskId)

        #email_module.sendStartTaskMail(proceso)
    else:
        procesos=updateTaskStatus(procesos,fila-1,'ERROR')
        #email_module.sendFinishedStatus(proceso,'ERROR')
    return procesos

def restartProcess(procesos):
    """función para reiniciar el estatus de todos los procesos a None

    Args:
        procesos (list): Lista de procesos diarios del AXSL

    Returns:
        procesos: Lista actualizada con los procesos diarios del AXSL
    """
    contador=0
    for proceso in procesos:
        procesos[contador][7]='NONE'
        contador+=1
    return procesos

def runAXSL():
    print('runAXSL')
    '''

    Returns
    -------
    procesos : List
        Lista de procesos diarios del AXSL.

    '''
    procesos=readAXSL()
    #while(True):
    print('iteracion '+time.strftime("%H:%M"))
    fila=0
    for proceso in procesos:
        fila+=1
        processStatus=proceso[7]
        if(processStatus=='NONE'):
            procesos=runProcess(proceso,fila,procesos)
        procesos=validateTaskStatus(procesos)
        updateAXSL(procesos)
        
        """
        if(time.strftime('%#d')== dia):
            if(time.strftime("%H:%M")=='00:00' or time.strftime("%H:%M")=='00:01'):
                procesos = restartProcess(procesos)
            else:
                fila=0
                for proceso in procesos:
                    fila+=1
                    hour=time.localtime().tm_hour
                    minute=time.localtime().tm_min
                    scheduleTime=proceso[4]
                    processStatus=proceso[6]
                    if('Predecesor' in scheduleTime):
                        if('-' in scheduleTime):
                            predecesores=scheduleTime.split('-')[0].split(' ')[1].split(',')
                            hour_ex,min_ex=map(int,scheduleTime.split('-')[1].split(':'))
                            predecesoresTerminaron=True
                            for procesoPredecesor in predecesores:
                                if(not checkPredecesor(procesoPredecesor,procesos)):
                                    predecesoresTerminaron=False
                            if(((hour>=hour_ex and minute>=min_ex) or hour>hour_ex) and processStatus=='NONE' and
                            predecesoresTerminaron):
                                procesos=runProcess(proceso,fila,procesos)
                        else:
                            predecesores=scheduleTime.split('-')[0].split(' ')[1].split(',')
                            predecesoresTerminaron=True
                            for procesoPredecesor in predecesores:
                                if(not checkPredecesor(procesoPredecesor,procesos)):
                                    predecesoresTerminaron=False
                            if(predecesoresTerminaron and processStatus=='NONE'):
                                procesos=runProcess(proceso,fila,procesos)
                    else:
                        hour_ex,min_ex=map(int,scheduleTime.split(':'))
                        #print('hora ex:'+ str(hour_ex))
                        if(((hour>=hour_ex and minute>=min_ex) or hour>hour_ex) and processStatus=='NONE'):
                            procesos=runProcess(proceso,fila,procesos)
                procesos=validateTaskStatus(procesos)
            updateAXSL(procesos)
        else:
            print('aún no es día de ejecución')
        time.sleep(60)
        """

    return None


#while(True):
# try:
runAXSL()
# except:
#     print('Ha ocurrido un error inesperado, volver a correr')




