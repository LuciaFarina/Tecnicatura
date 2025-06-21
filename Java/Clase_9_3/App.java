package Clase_9_3;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        final double SALARIO_BASE = 1000.0;

        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el número de carros vendidos: ");
        int carrosVendidos = scanner.nextInt();
        System.out.print("Ingrese el valor total de las ventas: ");
        double valorTotalVentas = scanner.nextDouble();

        double comisionFija = carrosVendidos * 150.0;
        double comisionPorcentaje = valorTotalVentas * 0.05;

        double salarioTotal = SALARIO_BASE + comisionFija + comisionPorcentaje;

        System.out.println("El salario mensual del vendedor es: $" + salarioTotal);

        scanner.close();
    }
}
