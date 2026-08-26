Desarrollar en Python un sistema de gestión correspondiente a una de las temáticas propuestas
en esta actividad. El sistema deberá permitir almacenar y administrar un conjunto de registros
utilizando las estructuras y recursos trabajados hasta la UVA 3 inclusive.
Cada grupo deberá seleccionar una sola temática y desarrollar todas las funcionalidades indicadas en la consigna. Las temáticas son las siguientes:

Gestión de gimnasio
El sistema permitirá administrar socios. Cada socio deberá incluir como mínimo: Número de
socio; Nombre; Actividad principal; Valor de la cuota; Estado.
La actividad deberá seleccionarse entre un conjunto de categorías previamente definido por
el estudiante.

Requisitos generales del sistema
Uso de matrices: Los registros del sistema deberán almacenarse y gestionarse utilizando una matriz implementada mediante una lista de listas. Cada fila de la matriz representará un registro completo de la temática seleccionada y sus columnas corresponderán a los diferentes datos definidos para dicho registro. Todas las funcionalidades de alta, consulta, modificación, eliminación, listado y procesamiento deberán operar sobre esta estructura de datos.

Datos iniciales: Al iniciar el programa, la matriz deberá contener como mínimo 5 registros cargados previamente (hardcodeados) en el código fuente. Estos datos permitirán comenzar a utilizar y probar las distintas funcionalidades del sistema sin necesidad de realizar previamente la carga manual de información. Los registros agregados posteriormente mediante la opción de alta deberán incorporarse a la misma matriz.

Menú de opciones y funcionalidades: El programa deberá presentar un menú de opciones que permita ejecutar las distintas funcionalidades y permanecer activo hasta que el usuario seleccione la opción de salida.
    1. Dar de alta un registro: El usuario deberá poder ingresar los datos correspondientes a un nuevo registro y almacenarlo en la estructura utilizada por el sistema.
    2. Consultar un registro: Se deberá poder buscar un registro utilizando su código, número o identificador correspondiente y mostrar todos sus datos.
    3. Modificar un registro: Se deberá localizar previamente el registro y permitir modificar uno o más de sus datos.
    4. Eliminar un registro: Se deberá localizar previamente el registro y eliminarlo de la estructura de datos.
    5. Mostrar todos los registros: Se deberá imprimir un listado completo de la información almacenada utilizando un formato tabular, con encabezados que permitan identificar claramente cada uno de los campos. La información deberá presentarse organizada en filas y columnas, procurando una correcta alineación de los datos para facilitar su lectura.
    6. Consultar registros por categoría: El usuario deberá poder ingresar o seleccionar una categoría y visualizar todos los registros que pertenezcan a ella.
    7. Realizar un procesamiento estadístico: El sistema deberá calcular y mostrar información obtenida a partir de los registros almacenados. Como mínimo deberá incluir: cantidad total de registros; cantidad de registros correspondientes a una categoría determinada; y una estadística adicional relacionada con la temática seleccionada.
