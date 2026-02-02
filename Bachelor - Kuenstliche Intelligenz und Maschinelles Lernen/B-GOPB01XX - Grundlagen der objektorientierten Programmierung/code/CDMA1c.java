public class CDMA1c {

    // Repräsentiert eine Chip-Sequenz mit 4 Werten
    static class Chip {
        private int[] S = new int[4];

        public Chip(int s1, int s2, int s3, int s4) {
            S[0] = s1; S[1] = s2; S[2] = s3; S[3] = s4;
        }

        // Gibt den Wert an gegebener Position zurück
        public int get(int index) {
            return S[index];
        }
    }

    // Nachricht, die aus 4 Werten besteht (einem Codewort)
    static class BitMessage {
        private int[] message = new int[4];

        // Gibt die Nachricht als String aus
        @Override
        public String toString() {
            return "(" + message[0] + "," + message[1] + "," + message[2] + "," + message[3] + ")";
        }

        // Kodiert ein einzelnes Bit mithilfe eines Chips
        public BitMessage encode(Chip c, boolean bit) {
            for (int i = 0; i < 4; i++) {
                message[i] += bit ? c.get(i) : -c.get(i); // +Chip wenn true, -Chip wenn false
            }
            return this;
        }

        // Dekodiert ein einzelnes Bit mithilfe eines Chips
        public boolean decode(Chip c) {
            int sum = 0;
            for (int i = 0; i < 4; i++) {
                sum += message[i] * c.get(i); // Skalarprodukt
            }
            return sum > 0; // positiv = true, negativ = false
        }
    }

    // Repräsentiert ein Byte (8 Bits)
    static class ByteMessage {
        private BitMessage[] bits = new BitMessage[8];

        public ByteMessage() {
            // Initialisiert jedes BitMessage-Element
            for (int i = 0; i < 8; i++) {
                bits[i] = new BitMessage();
            }
        }

        // Gibt alle 8 BitMessages als String aus
        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            for (BitMessage bit : bits) {
                sb.append(bit.toString()).append(" ");
            }
            return sb.toString().trim();
        }

        // Kodiert ein Zeichen (8 Bits) mit einem Chip
        public ByteMessage encode(Chip chip, char c) {
            for (int i = 0; i < 8; i++) {
                boolean bit = ((c >> i) & 1) == 1; // prüft Bit i (LSB zuerst)
                bits[i].encode(chip, bit);
            }
            return this;
        }

        // Dekodiert das Zeichen mithilfe eines Chips
        public char decode(Chip chip) {
            int value = 0;
            for (int i = 0; i < 8; i++) {
                if (bits[i].decode(chip)) {
                    value |= (1 << i); // setzt Bit i auf 1
                }
            }
            return (char) value;
        }
    }

    public static void main(String[] args) {
        // Erzeugung von vier orthogonalen Chips
        var A = new Chip(1, 1, 1, 1);
        var B = new Chip(1, -1, 1, -1);
        var C = new Chip(1, 1, -1, -1);
        var D = new Chip(1, -1, -1, 1);

        // Kodiert "test" auf vier Chips
        var message = new ByteMessage()
                .encode(A, 't')
                .encode(B, 'e')
                .encode(C, 's')
                .encode(D, 't');

        // Gibt kodierte Nachricht aus
        System.out.println(message);

        // Dekodiert wieder zurück zu Zeichen
        System.out.println("" + message.decode(A)
                           + message.decode(B)
                           + message.decode(C)
                           + message.decode(D));
    }
}