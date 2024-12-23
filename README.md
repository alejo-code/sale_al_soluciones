# Módulo de Ventas VIP para Odoo 14

Este módulo extiende la funcionalidad de la aplicación de ventas en Odoo 14. Añade características adicionales como tarifas VIP, campos personalizados en contactos y un wizard para filtrar pedidos de ventas según criterios específicos.

## Requisitos

- Odoo 14.
- El módulo debe ser instalado en una base de datos de Odoo 14.

## Funcionalidades

### 1. Tarifa VIP

Al instalar el módulo, se crea una tarifa llamada **VIP** que aplica un **40% de descuento** en cualquier producto.

### 2. Campo VIP en Contactos

Se agrega un campo booleano llamado **"VIP"** a los contactos (clientes). Este campo es **editable en el formulario** de contacto y es **visible solo para usuarios del grupo “Ventas/Administrador”**.

### 3. Asignación Automática de Tarifa VIP

Cuando se selecciona un cliente en un pedido de ventas y el cliente tiene marcado el campo **"VIP"**, el módulo asigna automáticamente la tarifa **VIP** al pedido de ventas.

### 4. Filtro en el Listado de Ventas

El módulo crea un filtro en el listado de ventas para mostrar solo los pedidos de clientes **VIP**.

### 5. Wizard para Filtrar Pedidos de Ventas

Se agrega un wizard accesible desde el menú ** Pedidos > Ventas por vendedor**. Solo es visible para los usuarios que pertenecen al grupo **“Ventas/Administrador”**.

El wizard tiene los siguientes campos:

- **Vendedores**: Un campo relacional para seleccionar uno o más vendedores. Si no se selecciona ningún vendedor, se incluirán los pedidos de todos los vendedores.
- **Fecha Desde**: Campo de fecha para filtrar pedidos a partir de esta fecha.
- **Fecha Hasta**: Campo de fecha para filtrar pedidos hasta esta fecha.

### 6. Comportamiento del Wizard

- Si ambos campos de fecha están establecidos, el reporte incluirá solo los pedidos dentro del rango de fechas.
- Si solo se establece la fecha en **Desde**, se incluirán los pedidos a partir de esa fecha.
- Si solo se establece la fecha en **Hasta**, se incluirán los pedidos hasta esa fecha.

### 7. Reporte por Consola

El wizard imprimirá en la consola los pedidos de ventas que cumplen con los filtros establecidos.

## Instalación

1. Descargar el módulo.
2. Copiar el módulo en el directorio `addons` de tu instalación de Odoo.
3. Desde la interfaz de Odoo, ir a **Aplicaciones** y actualizar la lista de aplicaciones.
4. Buscar **"Ventas VIP"** e instalar el módulo.

## Uso

- Después de instalar el módulo, asegúrate de que el grupo **"Ventas/Administrador"** tenga acceso a las funcionalidades del módulo.
- Crea o edita un contacto para marcarlo como **VIP**.
- En un pedido de ventas, selecciona un cliente **VIP** y la tarifa **VIP** se asignará automáticamente al pedido.
- Usa el wizard desde **Pedidos > Ventas por vendedor** para generar reportes filtrados por vendedor y rango de fechas.

## Estructura del Módulo

El módulo contiene las siguientes partes:

- **Models**: Define los modelos y campos relacionados con las tarifas y contactos.
- **Views**: Define las vistas, incluyendo la vista del formulario de contacto y el wizard.
- **Reports**: Genera el reporte basado en los filtros seleccionados en el wizard.
- **Security**: Define los permisos y accesos para el grupo **"Ventas/Administrador"**.

## Contribución

Si deseas contribuir al desarrollo de este módulo, por favor crea un pull request con tus cambios.

## Licencia

Este módulo está licenciado bajo la [Licencia AGPL-3.0](https://www.gnu.org/licenses/agpl-3.0.html).

---

Para cualquier duda o soporte, por favor contacta con el equipo de desarrollo en **[email@empresa.com](mailto:email@empresa.com)**.
