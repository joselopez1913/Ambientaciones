# -*- coding: utf-8 -*-
import win32com.client as win32
"""
Created on Mon Aug 22 10:52:59 2022

@author: jalleyne
"""

users=['jalleyne','jamunera','jhcastan','jolrodri','adlatorr']
# users=['jalleyne','alroldan','jzuluaga','dacely']
# users=['jalleyne']

def getUserList(users):
    '''

    Parameters
    ----------
    users : List
        Lista de usuarios para recibir notificación.
        
    Returns
    -------
    userList : String
        Cadena con usuarios para utilizar en el mail.To

    '''
    userList=''
    for user in users:
        userList='{0}{1}@bancolombia.com.co;'.format(userList,user)
    return userList[:-1]


def sendFinishedStatus(proceso,status):
    """Función para envar notificación de finalización de ejecución de proceso

    Args:
        proceso (list): proceso del cual se va a notificar la ejecución.
        status (string): estado en el cual terminó el proceso
    """
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.Subject='Notificación de proceso {0} terminó en {1}'.format(proceso[2],status)
    style='''
        <html lang="es"><head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<!-- <title>Fluid Grid Master</title> -->
	<style type="text/css">
		/* Outlines the grid, remove when sending */
		
		body,
		table,
		td,
		a {
			-webkit-text-size-adjust: 100%;
			-ms-text-size-adjust: 100%;
		}
		
		table,
		
		img {
			-ms-interpolation-mode: bicubic;
		}
		/* RESET STYLES */
		
		img {
			border: 0;
			outline: none;
			text-decoration: none;
		}
		
		body {
			margin: 0 !important;
			padding: 0 !important;
			width: 100% !important;
		}
		/* iOS BLUE images */
		
		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: none !important;
			font-size: inherit !important;
			font-family: inherit !important;
			font-weight: inherit !important;
			line-height: inherit !important;
		}
		/* ANDROID CENTER FIX */
		
		div[style*="margin: 16px 0;"] {
			margin: 0 !important;
		}
		
		@media screen and (max-width: 600px) {
			.banner {
				width: 100% !important;
				height: auto !important;
			}
			.simple-content--image {
				display: inline-block;
				width: auto !important;
				
			}
			.table-container {
				width: 100% !important;
			}
			.mobile-space {
				width: 15px !important;
			}
			.mobile-space-2 {
				width: 0px !important;
			}
			.content-row {
				display: inline-block;
			}
			.table_100 {
				width: 100% !important;
			}
			.table_85 {
				width: 85% !important;
			}
			.hide_mobile {
				display: none !important;
			}
			.text-yellow {
				font-size: 25px !important;
				line-height: 28px !important;
			}
			.text-white {
				font-size: 20px !important;
				line-height: 23px !important;
			}
			.table_100.cutom-tbl {
				width: 100% !important;
				max-width: 100% !important;
			}
			/*.td-width {
	 width: 65px !important;
	 }
	 .td-width-space {
	 width: 15px !important;
	 }*/
			.mobile_height {
				height: 10px !important;
			}
			.align_center {
				text-align: center !important;
			}
			.cta_mobile {
				width: 200px !important;
			}
			.blue_text {
				font-size: 13px !important;
				padding: 10px 5px !important;
			}
			.mobile-small-text {
				font-size: 9px !important;
				line-height: 12px !important;
			}
			.mobile-big-text {
				font-size: 20px !important;
				line-height: 12px !important;
			}
			.w-262 {
				width: 262px !important;
				max-width: 100% !important;
			}
		}
		
		@media screen and (max-width: 480px) {
			.banner {
				width: 100% !important;
				height: auto !important;
			}
			.table-container {
				width: 100% !important;
			}
			.mobile-space {
				width: 15px !important;
			}
			.mobile-space-2 {
				width: 0px !important;
			}
			.content-row {
				display: inline-block;
			}
			.table_100 {
				width: 100% !important;
			}
			.table_85 {
				width: 85% !important;
			}
			.hide_mobile {
				display: none !important;
			}
			.text-yellow {
				font-size: 26px !important;
				line-height: 29px !important;
			}
			.text-white {
				font-size: 20px !important;
				line-height: 23px !important;
			}
			.td-width {
				width: 65px !important;
			}
			.td-width-space {
				width: 15px !important;
			}
			.mobile_height {
				height: 10px !important;
			}
			.align_center {
				text-align: center !important;
			}
			.cta_mobile {
				width: 200px !important;
			}
			.blue_text {
				font-size: 13px !important;
				padding: 10px 5px !important;
			}
			.txt-left-mob {
				text-align: left !important;
			}
			.pb-27 {
				padding-bottom: 27px !important;
			}
			.space-mobile {
				height: 5px !important;
			}
		}

	</style>
</head>'''
    body=f'''
<body style="margin:0; padding:0; background-color:#ffffff;">
	<div style="background-color:#ffffff; max-width: 600px; margin: auto;">
		<!--[if mso]>
		<table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" align="center">
		   <tr>
			  <td>
				 <![endif]-->

		<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="600">
			<tbody>
				<tr>
					<td align="center" valign="top">

						<table align="center" bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" class="table_100" style="max-width:600px; width:100%;background-color: #ffffff;" width="600">
							<tbody>
								<tr>
									<td align="left" valign="top">

										<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
											<tbody>
												<tr>
													<td height="3" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>

						<table align="center" bgcolor="#2C2A29" border="0" cellpadding="0" cellspacing="0" class="table_100" style="max-width:600px; width:100%;background-color: #2C2A29;" width="600">
							<tbody>
								<tr>
									<td align="left" style="width: 100%;" valign="top">

										<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
											<tbody>
												<tr>
													<td height="17" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="padding-left: 15px;" valign="top" width="175"><img src="http://bancolombia-email-wsuite.s3.amazonaws.com/templates/605ce7f68622a5425353ea51/img/header-logo.png" width="175" height="auto" border="0" alt="header-logo" class="fr-fic fr-dii"></td>
													<td class="table_100" width="420">&nbsp;</td>
												</tr>
												<tr>
													<td height="17" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
								<tr>
									<td bgcolor="#FDDA24" height="4" style="font-size:1px;line-height:1px;">&nbsp;</td>
								</tr>
							</tbody>
						</table>

						<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="100%">
							<tbody>
								<tr>
									<td align="center" valign="top">

										<table align="center" border="0" cellpadding="0" cellspacing="0" class="table_95" width="90%">
											<tbody>
												<tr>
													<td height="35" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="font-family:Arial, sans-serif;font-size:13px;line-height:16px;color:#000000;font-weight: normal;text-align: left;" valign="top">CV10 Prod Nube</td>
												</tr>
												<tr>
													<td align="left" class="text-yellow" style="font-family:Arial, sans-serif;font-size:28px;line-height:31px;color:#000000;font-weight: bold;text-align: left;" valign="top">Notificación Finalización de Ejecución</td>
												</tr>
												<tr>
													<td class="space-mobile" height="15" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="font-family:Arial, sans-serif;font-size:18px;line-height:21px;color:#000000;font-weight: normal;text-align: left;" valign="top">{proceso[2]}</td>
												</tr>
												<tr>
													<td height="35" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="font-family:Arial, sans-serif;font-size:13px;line-height:16px;color:#000000;font-weight: normal;text-align: left;" valign="top">
														
														<!--
															Aqui es el cuerpo del correo 
														-->

														Se notifica que el proceso <span style="font-weight:bold">{proceso[2]}</span> terminó su ejecución en estado {status}. <br>
														<br>
														<span style="font-weight:bold">Para mayor información:</span><br>
														<br>
														WorkFlow: {proceso[2]}<br>
														<br>													

													</td>
												</tr>
												<tr>
													<td height="35" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="center" valign="middle">

														<table align="center" bgcolor="#FDDA24" border="0" cellpadding="0" cellspacing="0" class="cta" height="36" style="border-radius: 18px;" width="240">
															<tbody>
																<tr>
																	<td align="center" height="36" valign="middle">
																		
																		<a href="https://controllerview.apps.bancolombia.corp:8443/cv/ui/global/index" name="qLink7" overwrite="true" style="background-color:#FDDA24;color:#000000;display:inline-block;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;line-height:36px;text-align:center;text-decoration:none;width:240px;-webkit-text-size-adjust:none;height: 36px;border-radius: 18px;text-transform: uppercase" target="_blank">INGRESAR A CV10 Prod NUBE</a>
																		
																	</td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
												<tr>
													<td height="35" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td style="padding-top:0px;">

														<table border="0" cellpadding="0" cellspacing="0" width="100%">
															<tbody>
																<tr>
																	<td align="center" valign="top"><img src="http://bancolombia-email-wsuite.s3.amazonaws.com/templates/607745a657ad717760ad7605/img/line1.png" alt="footer-logo" width="100%" height="2" style="max-width: 540px;" border="0" class="fr-fic fr-dii"></td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
												<tr>
													<td height="20" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="font-family:Arial, sans-serif;font-size:13px;line-height:16px;color:#000000;font-weight: normal;text-align: left;" valign="top">Powered by: Equipo de migración RL♡</td>
												</tr>
											</tbody>
										</table>
										<!-- Footer -->

										<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="600">
											<tbody>
												<tr>
													<td align="center" valign="top">

														<table align="center" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="600">
															<tbody>
																<tr>
																	<td align="center" valign="top">

																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tbody>
																				<tr>
																					<td align="center" valign="top">

																						<table border="0" cellpadding="0" cellspacing="0" width="100%">
																							<tbody>
																								<tr>
																									
																									<td align="center" valign="top">

																										<table border="0" cellpadding="0" cellspacing="0" style="padding:10px 0px;" width="100%">
																											<tbody>
																												<tr>
																													<td height="30" style="font-size: 1px;line-height: 1px;">&nbsp;</td>
																												</tr>
																												<tr>
																													<td align="center" valign="top"><img src="http://bancolombia-email-wsuite.s3.amazonaws.com/templates/607745a657ad717760ad7605/img/footer-logo.png" alt="footer-logo" class="banner fr-fic fr-dii" width="175" height="auto" style="max-width: 175px;" border="0"></td>
																												</tr>
																												<tr>
																													<td height="41" style="font-size:1px;line-height:1px;">&nbsp;</td>
																												</tr>
																												
																												
																												
																												
																											</tbody>
																										</table>
																									</td>
																									<td width="5%">&nbsp;</td>
																								</tr>
																							</tbody>
																						</table>
																					</td>
																				</tr>
																			</tbody>
																		</table>
																	</td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
											</tbody>
										</table>

										<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="100%">
											<tbody>
												<tr>
													<td align="center" valign="top">

														<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%">
															<tbody>
																<tr>
																	<td height="32" style="font-size:1px;line-height:1px;">&nbsp;</td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
											</tbody>
										</table>
										<!--[if mso]>
					   </td>
					</tr>
				 </table>
				 <![endif]-->
									</td>
								</tr>
							</tbody>
						</table>
					</td>
				</tr>
			</tbody>
		</table></div>


</body></html>'''
    mail.HTMLBody=style+body
    mail.To=getUserList(users)
    try:
        mail.Send()
    except:
        print('Error con módulo de correo')
    return None
    

def sendStartTaskMail(proceso):
    """Función para enviar notificación de inicio de ejecución de proceso

    Args:
        proceso (list): proceso del cual se va a notificar la ejecución.
    """
    outlook=win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.Subject='Notificación de ejecución de proceso {0}.'.format(proceso[2])
    mail.To=getUserList(users)
    style='''
    <html lang="es"><head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<!-- <title>Fluid Grid Master</title> -->
	<style type="text/css">
		/* Outlines the grid, remove when sending */
		
		body,
		table,
		td,
		a {
			-webkit-text-size-adjust: 100%;
			-ms-text-size-adjust: 100%;
		}
		
		table,
		
		img {
			-ms-interpolation-mode: bicubic;
		}
		/* RESET STYLES */
		
		img {
			border: 0;
			outline: none;
			text-decoration: none;
		}
		
		body {
			margin: 0 !important;
			padding: 0 !important;
			width: 100% !important;
		}
		/* iOS BLUE images */
		
		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: none !important;
			font-size: inherit !important;
			font-family: inherit !important;
			font-weight: inherit !important;
			line-height: inherit !important;
		}
		/* ANDROID CENTER FIX */
		
		div[style*="margin: 16px 0;"] {
			margin: 0 !important;
		}
		
		@media screen and (max-width: 600px) {
			.banner {
				width: 100% !important;
				height: auto !important;
			}
			.simple-content--image {
				display: inline-block;
				width: auto !important;
				
			}
			.table-container {
				width: 100% !important;
			}
			.mobile-space {
				width: 15px !important;
			}
			.mobile-space-2 {
				width: 0px !important;
			}
			.content-row {
				display: inline-block;
			}
			.table_100 {
				width: 100% !important;
			}
			.table_85 {
				width: 85% !important;
			}
			.hide_mobile {
				display: none !important;
			}
			.text-yellow {
				font-size: 25px !important;
				line-height: 28px !important;
			}
			.text-white {
				font-size: 20px !important;
				line-height: 23px !important;
			}
			.table_100.cutom-tbl {
				width: 100% !important;
				max-width: 100% !important;
			}
			/*.td-width {
	 width: 65px !important;
	 }
	 .td-width-space {
	 width: 15px !important;
	 }*/
			.mobile_height {
				height: 10px !important;
			}
			.align_center {
				text-align: center !important;
			}
			.cta_mobile {
				width: 200px !important;
			}
			.blue_text {
				font-size: 13px !important;
				padding: 10px 5px !important;
			}
			.mobile-small-text {
				font-size: 9px !important;
				line-height: 12px !important;
			}
			.mobile-big-text {
				font-size: 20px !important;
				line-height: 12px !important;
			}
			.w-262 {
				width: 262px !important;
				max-width: 100% !important;
			}
		}
		
		@media screen and (max-width: 480px) {
			.banner {
				width: 100% !important;
				height: auto !important;
			}
			.table-container {
				width: 100% !important;
			}
			.mobile-space {
				width: 15px !important;
			}
			.mobile-space-2 {
				width: 0px !important;
			}
			.content-row {
				display: inline-block;
			}
			.table_100 {
				width: 100% !important;
			}
			.table_85 {
				width: 85% !important;
			}
			.hide_mobile {
				display: none !important;
			}
			.text-yellow {
				font-size: 26px !important;
				line-height: 29px !important;
			}
			.text-white {
				font-size: 20px !important;
				line-height: 23px !important;
			}
			.td-width {
				width: 65px !important;
			}
			.td-width-space {
				width: 15px !important;
			}
			.mobile_height {
				height: 10px !important;
			}
			.align_center {
				text-align: center !important;
			}
			.cta_mobile {
				width: 200px !important;
			}
			.blue_text {
				font-size: 13px !important;
				padding: 10px 5px !important;
			}
			.txt-left-mob {
				text-align: left !important;
			}
			.pb-27 {
				padding-bottom: 27px !important;
			}
			.space-mobile {
				height: 5px !important;
			}
		}

	</style>
</head>'''
    body=f'''
<body style="margin:0; padding:0; background-color:#ffffff;">
	<div style="background-color:#ffffff; max-width: 600px; margin: auto;">
		<!--[if mso]>
		<table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" align="center">
		   <tr>
			  <td>
				 <![endif]-->

		<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="600">
			<tbody>
				<tr>
					<td align="center" valign="top">

						<table align="center" bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" class="table_100" style="max-width:600px; width:100%;background-color: #ffffff;" width="600">
							<tbody>
								<tr>
									<td align="left" valign="top">

										<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
											<tbody>
												<tr>
													<td height="3" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>

						<table align="center" bgcolor="#2C2A29" border="0" cellpadding="0" cellspacing="0" class="table_100" style="max-width:600px; width:100%;background-color: #2C2A29;" width="600">
							<tbody>
								<tr>
									<td align="left" style="width: 100%;" valign="top">

										<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
											<tbody>
												<tr>
													<td height="17" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="padding-left: 15px;" valign="top" width="175"><img src="http://bancolombia-email-wsuite.s3.amazonaws.com/templates/605ce7f68622a5425353ea51/img/header-logo.png" width="175" height="auto" border="0" alt="header-logo" class="fr-fic fr-dii"></td>
													<td class="table_100" width="420">&nbsp;</td>
												</tr>
												<tr>
													<td height="17" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
								<tr>
									<td bgcolor="#FDDA24" height="4" style="font-size:1px;line-height:1px;">&nbsp;</td>
								</tr>
							</tbody>
						</table>

						<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="100%">
							<tbody>
								<tr>
									<td align="center" valign="top">

										<table align="center" border="0" cellpadding="0" cellspacing="0" class="table_95" width="90%">
											<tbody>
												<tr>
													<td height="35" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="font-family:Arial, sans-serif;font-size:13px;line-height:16px;color:#000000;font-weight: normal;text-align: left;" valign="top">CV10 Prod Nube</td>
												</tr>
												<tr>
													<td align="left" class="text-yellow" style="font-family:Arial, sans-serif;font-size:28px;line-height:31px;color:#000000;font-weight: bold;text-align: left;" valign="top">Notificación Ejecución de Proceso</td>
												</tr>
												<tr>
													<td class="space-mobile" height="15" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="font-family:Arial, sans-serif;font-size:18px;line-height:21px;color:#000000;font-weight: normal;text-align: left;" valign="top">{proceso[2]}</td>
												</tr>
												<tr>
													<td height="35" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="font-family:Arial, sans-serif;font-size:13px;line-height:16px;color:#000000;font-weight: normal;text-align: left;" valign="top">
														
														<!--
															Aqui es el cuerpo del correo 
														-->

														Se notifica inicio de ejecución del proceso. <br>
														<br>

													</td>
												</tr>
												<tr>
													<td height="35" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="center" valign="middle">

														<table align="center" bgcolor="#FDDA24" border="0" cellpadding="0" cellspacing="0" class="cta" height="36" style="border-radius: 18px;" width="240">
															<tbody>
																<tr>
																	<td align="center" height="36" valign="middle">
																		
																		<a href="https://controllerview.apps.bancolombia.corp:8443/cv/ui/global/index" name="qLink7" overwrite="true" style="background-color:#FDDA24;color:#000000;display:inline-block;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;line-height:36px;text-align:center;text-decoration:none;width:240px;-webkit-text-size-adjust:none;height: 36px;border-radius: 18px;text-transform: uppercase" target="_blank">INGRESAR A CV10 Prod NUBE</a>
																		
																	</td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
												<tr>
													<td height="35" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td style="padding-top:0px;">

														<table border="0" cellpadding="0" cellspacing="0" width="100%">
															<tbody>
																<tr>
																	<td align="center" valign="top"><img src="http://bancolombia-email-wsuite.s3.amazonaws.com/templates/607745a657ad717760ad7605/img/line1.png" alt="footer-logo" width="100%" height="2" style="max-width: 540px;" border="0" class="fr-fic fr-dii"></td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
												<tr>
													<td height="20" style="font-size:1px;line-height:1px;">&nbsp;</td>
												</tr>
												<tr>
													<td align="left" style="font-family:Arial, sans-serif;font-size:13px;line-height:16px;color:#000000;font-weight: normal;text-align: left;" valign="top">Powered by: Equipo de migración RL♡</td>
												</tr>
											</tbody>
										</table>
										<!-- Footer -->

										<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="600">
											<tbody>
												<tr>
													<td align="center" valign="top">

														<table align="center" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="600">
															<tbody>
																<tr>
																	<td align="center" valign="top">

																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tbody>
																				<tr>
																					<td align="center" valign="top">

																						<table border="0" cellpadding="0" cellspacing="0" width="100%">
																							<tbody>
																								<tr>
																									
																									<td align="center" valign="top">

																										<table border="0" cellpadding="0" cellspacing="0" style="padding:10px 0px;" width="100%">
																											<tbody>
																												<tr>
																													<td height="30" style="font-size: 1px;line-height: 1px;">&nbsp;</td>
																												</tr>
																												<tr>
																													<td align="center" valign="top"><img src="http://bancolombia-email-wsuite.s3.amazonaws.com/templates/607745a657ad717760ad7605/img/footer-logo.png" alt="footer-logo" class="banner fr-fic fr-dii" width="175" height="auto" style="max-width: 175px;" border="0"></td>
																												</tr>
																												<tr>
																													<td height="41" style="font-size:1px;line-height:1px;">&nbsp;</td>
																												</tr>
																												
																												
																												
																												
																											</tbody>
																										</table>
																									</td>
																									<td width="5%">&nbsp;</td>
																								</tr>
																							</tbody>
																						</table>
																					</td>
																				</tr>
																			</tbody>
																		</table>
																	</td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
											</tbody>
										</table>

										<table align="center" bgcolor="#FFFFFF" border="0" cellpadding="0" cellspacing="0" style="max-width:600px; width:100%;" width="100%">
											<tbody>
												<tr>
													<td align="center" valign="top">

														<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%">
															<tbody>
																<tr>
																	<td height="32" style="font-size:1px;line-height:1px;">&nbsp;</td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
											</tbody>
										</table>
										<!--[if mso]>
					   </td>
					</tr>
				 </table>
				 <![endif]-->
									</td>
								</tr>
							</tbody>
						</table>
					</td>
				</tr>
			</tbody>
		</table></div>


</body></html>
        '''
    mail.HTMLBody=style+body
    mail.Send()
    return None

