package Clase_3;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el nombre de tu libro preferido: ");
        String nombreLibro = sc.nextLine();

        System.out.println("Ingrese el nombre del autor de tu libro preferido: ");
        String nombreAutor = sc.nextLine();

        System.out.println("El nombre de tu libro es " + nombreLibro + " y fue escrito por " + nombreAutor);
    }
}
