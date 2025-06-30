package Clase_10;

public class Ej_5 {
    public static void main(String[] args) {
        boolean condicion = false;

        if (condicion) {
            System.out.println("Condición verdadera");
        } else {
            System.out.println("Condición falsa");
        }

        int num = 4;
        String numTxt;

        if (num == 1) {
            numTxt = "uno";
        } else if (num == 2) {
            numTxt = "dos";
        } else if (num == 3) {
            numTxt = "tres";
        } else if (num == 4) {
            numTxt = "cuatro";
        } else {
            numTxt = "inválido";
        }

        System.out.println("El número es " + numTxt);
    }
}