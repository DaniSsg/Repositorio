INSTRUCCIONES DE USO 

En dicha practica se hizo uso de un solo script llamado main.py, en el podemos observar el codigo correspondiente a cada una de las solicitudes haciendo uso de la api de Meraki. En primer lugar se listo todas las organizaciones a las que se tenia acceso una vez asignada nuestra API_key a traves de la operacion  getOrganizations a traves de esta se pudo obtener el id de la organizacion asignada, para nuestro caso DeLab. Posteriormente se ejecutaron operaciones como getOrganizationDevices para determinar los datos correspondientes a las redes con equipos de tipo "wireless" y "appliance" y constuir nuestro inventario, tambien vale la pena destacar que se hizo una comprobacion de errores con la operacion raise_for_status() y asi comprobar que las solicitudes estaban obteniendo una respuesta correcta. 

Finalmente para constuir nuestro archivo datos.csv que contiene nuestro inventario se tuvo que hacer de forma manual, como se observa en nuestro codigo (considerando que no ha sido lo mas eficiente, se intento algun metodo para hacerlo de manera automatica pero no se obtuvo un resultado satisfactorio) 

Nota: Los archivos utilizados para la practica son main.py, datos.csv,requirements.txt y README.TXT
