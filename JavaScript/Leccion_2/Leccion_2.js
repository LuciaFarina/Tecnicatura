// Tipos de Datos en JAvaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identicar
*/
var nombre = 'Lucia'; //Tipo Str
console.log(typeof nombre);

nombre = 7
console.log(typeof nombre);

nombre = 12.3;
console.log(typeof nombre)

var numero = 3000; //Tipo Númerico
console.log(numero);

var objeto = {
    nombre : "Lucia",
    apellido : "Farina",
    telefono : "2604678965"
}

console.log(objeto);

//Tipo de datos Booleanos
var bandera = true;
console.log(bandera)

// Tipo de dato Funcion
function miFuncion(){}
console.log(typeof miFuncion)

//Tipo de datos Symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

// Tipo de dato clase
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }   
}

console.log(typeof Persona);

var x;
console.log(x);

x = undefined
console.log(typeof x);

var y = null;
console.log(typeof y);

