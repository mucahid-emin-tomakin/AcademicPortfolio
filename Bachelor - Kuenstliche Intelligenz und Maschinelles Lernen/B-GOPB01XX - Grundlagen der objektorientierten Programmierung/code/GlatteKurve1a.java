import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GlatteKurve1a extends JFrame {

    // Unser Zeichenbereich (Panel), auf dem die Punkte und das Polygon angezeigt werden
    private DrawPanel panel;

    // Konstruktor der Hauptklasse, die das Fenster erstellt und das Panel hinzufügt
    public GlatteKurve1a() {
        setTitle("Polygon mit Mausklicks");  // Setzt den Titel des Fensters
        setSize(600, 600);  // Setzt die Fenstergröße auf 600x600 Pixel
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  // Schließt das Programm, wenn das Fenster geschlossen wird

        panel = new DrawPanel();  // Erstellt eine Instanz des DrawPanel (das Zeichenpanel)
        add(panel);  // Fügt das Panel zum JFrame hinzu
        setVisible(true);  // Macht das Fenster sichtbar
    }

    // Inneres Panel, auf dem das Polygon gezeichnet wird
    private class DrawPanel extends JPanel implements MouseListener {

        private Polygon polygon = new Polygon(); // Instanzvariable für das Polygon, das gezeichnet wird

        public DrawPanel() {
            addMouseListener(this);  // Registriert das Panel als MouseListener für Mausereignisse
        }

        // Methode zum Zeichnen des Panels
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);  // Ruft die Basismethode auf, um den Hintergrund zu löschen

            // Zeichne alle Punkte, die im Polygon gespeichert sind
            g.setColor(Color.RED);  // Setzt die Farbe für die Punkte auf Rot
            for (int i = 0; i < polygon.npoints; i++) {
                g.fillOval(polygon.xpoints[i] - 3, polygon.ypoints[i] - 3, 6, 6);  // Zeichnet rote Kreise an den Punkten
            }

            // Zeichne das Polygon nur, wenn mindestens 3 Punkte vorhanden sind
            if (polygon.npoints >= 3) {
                g.setColor(Color.BLUE);  // Setzt die Farbe für das Polygon auf Blau
                g.drawPolygon(polygon);  // Zeichnet das Polygon mit den gespeicherten Punkten
            }
        }

        // Diese Methode wird aufgerufen, wenn auf das Panel geklickt wird
        @Override
        public void mouseClicked(MouseEvent e) {
            int x = e.getX();  // Holen der X-Koordinate des Mausklicks
            int y = e.getY();  // Holen der Y-Koordinate des Mausklicks

            // Fügt den Punkt zum Polygon hinzu
            polygon.addPoint(x, y);

            // Aktualisiert die Anzeige (Panel wird neu gezeichnet)
            repaint();
        }

        // Leere Implementierungen für die anderen MouseListener-Methoden
        @Override public void mousePressed(MouseEvent e) {}
        @Override public void mouseReleased(MouseEvent e) {}
        @Override public void mouseEntered(MouseEvent e) {}
        @Override public void mouseExited(MouseEvent e) {}
    }

    // Main-Methode zum Starten des Programms
    public static void main(String[] args) {
        SwingUtilities.invokeLater(GlatteKurve1a::new);  // Startet die GUI im Event-Dispatch-Thread
    }
}