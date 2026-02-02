public class CDMA1b {

    // Klasse zur Darstellung eines Chip-Codes mit 4 Werten
    static class Chip {
        private int[] S = new int[4];

        // Initialisiert den Chip mit vier Werten
        public Chip(int s1, int s2, int s3, int s4) {
            S[0] = s1; S[1] = s2; S[2] = s3; S[3] = s4;
        }

        // Gibt einen einzelnen Wert zurück
        public int get(int index) {
            return S[index];
        }
    }

    // Klasse für codierte Bit-Nachrichten
    static class BitMessage {
        private int[] message = new int[4]; // Nachricht als Zahlenvektor

        // Gibt die Nachricht als String zurück
        @Override
        public String toString() {
            return "(" + message[0] + "," + message[1] + "," + message[2] + "," + message[3] + ")";
        }

        // Kodiert ein einzelnes Bit mit dem Chip: true = +Chip, false = -Chip
        public BitMessage encode(Chip c, boolean bit) {
            for (int i = 0; i < 4; i++) {
                message[i] += bit ? c.get(i) : -c.get(i);
            }
            return this;
        }

        // Decodiert ein Bit mithilfe eines Chip-Vergleichs
        public boolean decode(Chip c) {
            int sum = 0;
            for (int i = 0; i < 4; i++) {
                sum += message[i] * c.get(i); // Skalarprodukt
            }
            return sum > 0; // positiv = true, negativ = false
        }
    }

    public static void main(String[] args) {
        // Definition von vier orthogonalen Chips
        var A = new Chip(1, 1, 1, 1);
        var B = new Chip(1, -1, 1, -1);
        var C = new Chip(1, 1, -1, -1);
        var D = new Chip(1, -1, -1, 1);

        // Nachricht: A=true, B=false, C=true, D=false
        var message = new BitMessage()
                .encode(A, true)
                .encode(B, false)
                .encode(C, true)
                .encode(D, false);

        // Ausgabe: Nachricht und dekodierte Bits
        System.out.println(message);
        System.out.println(message.decode(A) + " " +
                           message.decode(B) + " " +
                           message.decode(C) + " " +
                           message.decode(D));
    }
}