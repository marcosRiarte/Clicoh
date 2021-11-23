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
simpre debe tener el mismo id</br>
{ "id": "1234","stock": 21 }</br>
</br></br>

Tokens: Para obtener el token debemos ingresar nuestro usuario y contraseña. Por defectos vamos a crear un user administrador que sera</br>
user: admin</br>
password: admin</br>

Nuestro servicio ya cuenta con este usuarios, sino hay que bajarse el proyecto crearse un super usuario con la siguiente instruccion ejecutada dentro de la
carpta del proyecto:</br>
./manage.py createsuperuser</br>
</br></br>
Luego vamos a hacer un POST a herokupath/api/token/</br>
y en el cuerpo del json enviamos nuestro usuario y contraseña creados</br></br>
</br>
{</br>
"username": "admin",</br>
"password": "admin"</br>
}</br>
y nos devolvera el token de "refresh" y el token de "access"; para autenticarnos usaremos el token de access</br></br>
{</br>
"refresh":</br>
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzM5MzgzMywianRpIjoiMzZiNzEzY2IyZjFiNDNkNzhjMTk4MmUxM2U0NjA0NTEiLCJ1c2VyX2lkIjoxfQ.y-NqGNEyV4bbDg-ZLuCrPXFiA37KgCM_G7v_kX65Hyk",</br>
"access":</br>
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MzA3NzMzLCJqdGkiOiIxMDE1OGZjNDcwZTQ0MjZkOGM4MGFiZjFkZjc2OTBkOCIsInVzZXJfaWQiOjF9.p4mxK71L2jbWG2vA1-W3nzbwnlD0GehcTqynca33Q9Q"</br>
}</br>
</br>
para mas intrucciones podemos ver este link https://coffeebytes.dev/django-rest-framework-y-jwt-para-autenticar-usuarios/</br>
Este token debemos enviarlo en todas nuestras peticiones para las ordenes de compra en formtao Bearer Token. Los tokens tienen distintas duracion 5 minutos o 24 hs
</br></br>
-Ordenes:</br></br>


Registrar: Creamos una nueva orden de compra ; debemos enviar el token access junto con cada solicitud para autenticarnos</br></br>
JSON de ejemplo:</br>
{</br>
Authorization: Bearer</br> eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3MzA3NzMzLCJqdGkiOiIxMDE1OGZjNDcwZTQ0MjZkOGM4MGFiZjFkZjc2OTBkOCIsInVzZXJfaWQiOjF9.p4mxK71L2jbWG2vA1-W3nzbwnlD0GehcTqynca33Q9</br>

{</br>
"id": "70", "details": [ { "cuantity": 3, "product": "1234" }, { "cuantity": 1, "product": "45" } ] }</br> 
y la enviamos a POST https://clicoh-ecomerce.herokuapp.com/order/ ; el sistema guardar la fecha de crecion y/actulizacion en la base de datos automaticamente. Nos devolvera como resultado el json con el monto total de la factura junto con su precio en dolares actualizado.</br>
</br>
Editar una orden (inclusive sus detalles). Debe actualizar el stock del producto</br>
Authorization: Bearer + {Token access}</br>
PUT https://clicoh-ecomerce.herokuapp.com/order/{order_id}/</br></br>
{</br>
"id": "70", "details": [ { "cuantity": 3, "product": "1234" }, { "cuantity": 13, "product": "45" } ] } </br>
 </br> </br>
Eliminar una orden. Restaura stock del producto</br>
Authorization: Bearer + {Token access}</br>
DELETE  https://clicoh-ecomerce.herokuapp.com/order/{order_id}/</br>
</br></br>
Consultar una orden y sus detalles</br>
Authorization: Bearer + {Token access}</br>
Enviar el token en un GET  https://clicoh-ecomerce.herokuapp.com/order/{order_id}/</br>
</br></br>
Listar todas las ordenes</br>
Authorization: Bearer + {Token access}</br>
Enviamos un GET https://clicoh-ecomerce.herokuapp.com/order/ y nos devolveran todas las ordenes disponibles ya creadas, con su total en presos y dolares.</br>

