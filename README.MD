# Proyecto Calculadora de Impuestos

## Descripción del Proyecto

Este proyecto es una Calculadora de Impuestos que calcula el monto del impuesto a pagar basado en diversos parámetros de ingresos y gastos. Valida los valores de entrada para asegurar que sean positivos y cumplan con condiciones específicas antes de realizar el cálculo del impuesto.

## Autores

- Mario Andrade Rojas
-Samuel Villa Carmona

## Documentación

### src/Console

En estas carpetas se encuentra los siguientes dos archivos: 

-Calculadora_Console.py
-Calculadora.py

#### Calculadora_Console.py:
Este archivo trata de la consola o la interfaz de usuario, para que el cliente o la persona pueda calcular sus impuestos. Agregando valores correspondidos y correctos. De lo contrario, saltaran errores, si fue correcto, lanza el valor total.

#### Calculadora.py:

Este archivo contiene toda la logica, conteniendo en el condicionales y formulas para la realizacion de los calculos o condiciones que se presentan a la hora de que el usuario ingrese los valores. 


### test
Esta carpeta contiene los siguientes archicos: 

-Calculadora_tests.py
-Casos_Calculadora.py
-Exceptions.py

#### Calculadora_tests.py
En este archivo encontramos la primera prueba uniaria con un ejemplo de prueba, es basicamente parecido al Calculadora.py, donde en el se encuentran formulas y condicionales, aparte de funciones para que la logica sea algo mas agradable. Al correrlo nos da el resultado de el ejemeplo de prueba. Este archivo es importante ya que en el se hacen todos los calculos, y se llaman las funciones desde los otros archivos. Tambien contiene las excepciones.

#### Casos_Calculadora.py
En este archivo estan las pruebas unitarias con casos de la vida real, donde encontramos: Casos normales, Casos extraordinarios y Casos de error.Desde este archivo se llaman las funciones de Calculadora_tests.py para poder hacer los calculos.

#### Exceptions.py
En este archivo se encuentran todas las excepciones, para que el usuario o la persona logre ver si, tiene algun error en los calculos o a la hora de haber ingresado un valor.


## Como ejectutar?
Para el buen uso de esta aplicacion el usuario debe ingresar al archivo Calculadora_Consoloe.py, que se encuentra en: src/Console/Calculadora_console.py.

Al ejecutar el programa le va desplegar una serie de preguntas para calcular el impuesto, y el usuario debera ingresar los valores correspondidos a su salario y gastos mensuales, usando solamente numeros, sin comas ni espacios, ni caracteres como: (#$%&+-) calculando asi el valor que deberia pagar de impuestos. 