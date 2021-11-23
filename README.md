***Clicoh ecommerce*</br>
-Django 3.2.0</br>
-gunicorn</br>
.Python 3.6 o superior</br>
-Heroku</br>
</br>
Exponemos los siguientes endpoints en las siguientes direcciones </br>
Producto:</br>

Registrar:Crea un producto nuevo</br>
Hacer un POST a https://clicoh-ecomerce.herokuapp.com/product/</br>

Json de ejemplo:</br>
{</br>
"id":"1234",</br>
"name": "Pizza de cebolla",</br>
"price": "799.99",</br>
"stock": 34</br>
}</br>

</br></br>
Editar un producto</br>
Hacer un PUT a https://clicoh-ecomerce.herokuapp.com/product/{product_id}/</br>
simpre debe tener el mismo id y se envia el Json completo(o sea valores en todos sus campos).</br>
Json de ejemplo:</br>
{</br>
"id": "1234",</br>
"name": "Pizza de cebollas,morron y papas",</br>
"price": "899.99",</br>
"stock": 60</br>
}</br>

-Eliminar un producto: Borrara el producto de la id proporcionada</br>
Hacer un DELETE a https://clicoh-ecomerce.herokuapp.com/product/{product_id}/</br>
</br></br>
-Consultar un producto</br>
Hacer un GET a https://clicoh-ecomerce.herokuapp.com/product/{prodcut_id}/</br>
</br></br>
-Listar todos los productos</br>
Hacer un GET a  https://clicoh-ecomerce.herokuapp.com/product/</br>
</br></br>
-Modificar stock de un producto</br>
Hacer un PATCH a https://clicoh-ecomerce.herokuapp.com/product/{product_id}/</br>
simpre debe tener el mismo id { "id": "1234","stock": 21 }</br>
</br></br>

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
Este token debemos enviarlo en todas nuestras peticiones para las ordenes de compra en formtao Bearer Token.Los tokens tienen distintas duracion 5 minutos o 24 hs
Ordenes:


Registrar: Creamos una nueva orden de compra ; debemos enviar el token access junto con cada solicitud para autenticarnos
JSON de ejemplo:
{
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MzA3NzMzLCJqdGkiOiIxMDE1OGZjNDcwZTQ0MjZkOGM4MGFiZjFkZjc2OTBkOCIsInVzZXJfaWQiOjF9.p4mxK71L2jbWG2vA1-W3nzbwnlD0GehcTqynca33Q9

{
"id": "70", "details": [ { "cuantity": 3, "product": "1234" }, { "cuantity": 1, "product": "45" } ] } y la enviamos a POST https://clicoh-ecomerce.herokuapp.com/order/ ; el sistema guardar la fecha de crecion y/actulizacion en la base de datos automaticamente. Nos devolvera como resultado el json con el monto total de la factura junto con su precio en dolares actualizado.

Editar una orden (inclusive sus detalles). Debe actualizar el stock del producto
PUT https://clicoh-ecomerce.herokuapp.com/order/
Enviamos una solicitud
Eliminar una orden. Restaura stock del producto
DELETE POST https://clicoh-ecomerce.herokuapp.com/order/{order_id}
Consultar una orden y sus detalles
Enviar el token en un GET POST https://clicoh-ecomerce.herokuapp.com/order
Listar todas las ordenes
Enviamos un GET https://clicoh-ecomerce.herokuapp.com/order//order y nos devolveran todas las ordenes disponibles ya creadas, con su total en presos y dolares.

