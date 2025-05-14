// Ejercicio: Tienda de libros
// Mostrar: Ingrese los siguientes datos del libro
// Digite el nombre del libro
// Digite el ID del libro
// Digite el precio del libro
// Indicar si el envío es gratuito (True/False)
// Mostrar:
// 	Nombre:
// 	ID: 
// 	Precio:
// 	Envío Gratuito?:

package Clase_6;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese los siguientes datos del libro: ");
        System.out.println("Digite el nombre del libro: ");
        String nombre = sc.nextLine();

        System.out.println("Digite el ID del libro: ");
        String id = sc.nextLine();

        System.out.println("Digite el precio del libro: ");
        String precio = sc.nextLine();

        System.out.println("Indicar si el envío es gratuito (True/False): ");
        String envioGratis = sc.nextLine();

        if (envioGratis.equals("True")) {
            envioGratis = "Sí";
        } else if (envioGratis.equals("False")) {
            envioGratis = "No";
        } else {
            envioGratis = "El formato es inválido, ingrese True/False";
        }

        System.out.println("Nombre: " + nombre);
        System.out.println("ID: " + id);
        System.out.println("Precio: " + precio);
        System.out.println("Envio Gratuito?: " + envioGratis);
    }
}
