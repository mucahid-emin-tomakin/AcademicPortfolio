public class CDMA1a {

    // Innere Klasse zur Repräsentation eines Chip-Codes
    static class Chip {
        private int[] S = new int[4]; // 4 Werte des Chips

        // Konstruktor: Initialisiert das Chip-Muster mit 4 Werten
        public Chip(int s1, int s2, int s3, int s4) {
            S[0] = s1;
            S[1] = s2;
            S[2] = s3;
            S[3] = s4;
        }

        // Gibt das Element an gegebener Position zurück
        public int get(int index) {
            return S[index];
        }

        // Gibt das gesamte Chip-Muster als Array zurück
        public int[] getSequence() {
            return S;
        }
    }

    public static void main(String[] args) {
        // Erstellen von vier verschiedenen Chip-Mustern
        var A = new Chip(1, 1, 1, 1);
        var B = new Chip(1, -1, 1, -1);
        var C = new Chip(1, 1, -1, -1);
        var D = new Chip(1, -1, -1, 1);

        // Ausgabe der Chip-Werte von Chip A
        System.out.println("Chip A:");
        for (int i = 0; i < 4; i++) {
            System.out.print(A.get(i) + " ");
        }
    }
}