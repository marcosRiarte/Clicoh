Exponemos los siguientes endpoints en las siguientes direcciones
Producto:

Registrar:Crea un producto nuevo
Hacer un POST a https:/heroku algo/


Json de ejemplo:
{
"id":"1234",
"name": "Pizza de cebolla",
"price": "799.99",
"stock": 34
}


Editar un producto
Hacer un UPDATE/PUT a https://product/{product_id}/
simpre debe tener el mismo id y se envia el Json completo(o sea valores en todos sus campos).
Json de ejemplo:
{
"id": "1234",
"name": "Pizza de cebollas,morron y papas",
"price": "899.99",
"stock": 60
}

Eliminar un producto: Borrara el producto de la id proporcionada
Hacer un DELETE a https://{product_id}/

Consultar un producto
Hacer un GET a https:// product/{prodcut_id}/

Listar todos los productos
Hacer un GET a https://product

*Modificar stock de un producto
Hacer un PATCH a https:// product/{IdProducto}/
simpre debe tener el mismo id { "id": "1234","stock": 21 }



Tokens: Para obtener el token debemos ingresar nuestro usuario y contraseña. Por defectos vamos a crear un user administrador que sera
user: admin
password: admin

Nuestro servicio ya cuenta con este usuarios, sino hay que bajarse el proyecto crearse un super usuario con la siguiente instruccion ejecutada dentro de la
carpta del proyecto:
./manage.py createsuperuser

Luego vamos a hacer un POST a herokupath/api/token/
y en el cuerpo del json enviamos nuestro usuario y contraseña creados

{
"username": "admin",
"password": "admin"
}
y nos devolvera el token de "refresh" y el token de "access"; para autenticarnos usaremos el token de access
{
"refresh":
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzM5MzgzMywianRpIjoiMzZiNzEzY2IyZjFiNDNkNzhjMTk4MmUxM2U0NjA0NTEiLCJ1c2VyX2lkIjoxfQ.y-NqGNEyV4bbDg-ZLuCrPXFiA37KgCM_G7v_kX65Hyk",
"access":
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MzA3NzMzLCJqdGkiOiIxMDE1OGZjNDcwZTQ0MjZkOGM4MGFiZjFkZjc2OTBkOCIsInVzZXJfaWQiOjF9.p4mxK71L2jbWG2vA1-W3nzbwnlD0GehcTqynca33Q9Q"
}

para mas intrucciones podemos ver este link https://coffeebytes.dev/django-rest-framework-y-jwt-para-autenticar-usuarios/
Este token dbemos enviarlo en toda nuestra peticiones para las ordenes de compra en formtao Bearer Token.Los tokens tienen distintas duracion
Ordenes:


Registrar: Creamos una nueva orden de compra ; debemos enviar el token access junto con cada solicitud para autenticarnos
JSON de ejemplo:
{
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MzA3NzMzLCJqdGkiOiIxMDE1OGZjNDcwZTQ0MjZkOGM4MGFiZjFkZjc2OTBkOCIsInVzZXJfaWQiOjF9.p4mxK71L2jbWG2vA1-W3nzbwnlD0GehcTqynca33Q9

{
"id": "70", "details": [ { "cuantity": 3, "product": "1234" }, { "cuantity": 1, "product": "45" } ] } y la enviamos a POST http://127.0.0.1:8000/order/ ; el sistema guardar la fecha de crecion y/actulizacion en la base de datos automaticamente. Nos devolvera como resultado el json con el monto total de la factura junto con su precio en dolares actualizado.

Editar una orden (inclusive sus detalles). Debe actualizar el stock del producto
Enviamos una solicitud
Eliminar una orden. Restaura stock del producto
Consultar una orden y sus detalles
Enviar el token en un GET http://127.0.0.1:8000/order/{Id_order}/
Listar todas las ordenes
Enviamos un GET http://127.0.0.1:8000/order y nos devolveran todas las ordenes disponibles ya creadas, con su total en presos y dolares.

