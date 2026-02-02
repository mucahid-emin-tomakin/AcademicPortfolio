import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GlatteKurve1c extends JFrame {

    // Konstruktor der Hauptklasse
    public GlatteKurve1c() {
        setTitle("Kurve");  // Setzt den Titel des Fensters
        setSize(600, 600);  // Setzt die Fenstergröße auf 600x600 Pixel
        setDefaultCloseOperation(EXIT_ON_CLOSE);  // Schließt das Programm, wenn das Fenster geschlossen wird
        add(new DrawPanel());  // Fügt das Panel (Zeichenfläche) hinzu
        setVisible(true);  // Macht das Fenster sichtbar
    }

    // Main-Methode zum Starten des Programms
    public static void main(String[] args) {
        SwingUtilities.invokeLater(GlatteKurve1c::new);  // Startet die GUI im Event-Dispatch-Thread
    }

    // Zeichenfläche mit Polygon und Corner-Cutting
    static class DrawPanel extends JPanel implements MouseListener {

        private Polygon polygon = new Polygon();  // Instanzvariable für das Polygon

        // Konstruktor für das Panel
        public DrawPanel() {
            addMouseListener(this);  // Registriert das Panel als MouseListener für Mausereignisse
        }

        // Methode zum Zeichnen des Panels
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);  // Ruft die Basismethode auf, um den Hintergrund zu löschen
            Graphics2D g2 = (Graphics2D) g;  // Erstellen eines Graphics2D Objekts für feinere Kontrolle beim Zeichnen

            // Zeichne das Kontrollpolygon (schwarz)
            g2.setColor(Color.BLACK);  // Setzt die Farbe auf Schwarz
            g2.setStroke(new BasicStroke(1));  // Setzt die Strichstärke auf 1 Pixel
            if (polygon.npoints >= 2)
                g2.drawPolygon(polygon);  // Zeichnet das Polygon, wenn mindestens 2 Punkte existieren

            // Unterteilung und Zeichnen der Kurve, wenn mindestens 3 Punkte
            if (polygon.npoints >= 3) {
                Polygon smooth = polygon;
                for (int i = 0; i < 5; i++) {
                    smooth = subdivide(smooth);  // 5 Unterteilungen mit der Corner-Cutting-Methode
                }
                g2.setColor(Color.RED);  // Setzt die Farbe auf Rot für die Kurve
                g2.setStroke(new BasicStroke(2));  // Setzt eine dickere Linie für die Kurve
                g2.drawPolyline(smooth.xpoints, smooth.ypoints, smooth.npoints);  // Zeichnet die geglättete Kurve
            }

            // Zeichne die Eckpunkte des Polygons
            g2.setColor(Color.BLUE);  // Setzt die Farbe auf Blau
            for (int i = 0; i < polygon.npoints; i++) {
                g2.fillOval(polygon.xpoints[i] - 3, polygon.ypoints[i] - 3, 6, 6);  // Zeichnet einen blauen Kreis an jedem Eckpunkt
            }
        }

        // Methode zur Corner-Cutting Unterteilung des Polygons
        private Polygon subdivide(Polygon input) {
            Polygon result = new Polygon();  // Ergebnis-Polygon für die Unterteilung
            int n = input.npoints;  // Anzahl der Punkte im Eingangspolygon

            // Durchlaufe alle Punkte des Polygons
            for (int i = 0; i < n; i++) {
                // Aktueller Punkt und der nächste (zyklisch, der letzte Punkt geht zum ersten zurück)
                int x0 = input.xpoints[i];
                int y0 = input.ypoints[i];
                int x1 = input.xpoints[(i + 1) % n];
                int y1 = input.ypoints[(i + 1) % n];

                // Berechne neue Punkte durch Corner Cutting (Mittelpunkt zwischen den Punkten)
                double px0 = 0.75 * x0 + 0.25 * x1;  // Punkt 0
                double py0 = 0.75 * y0 + 0.25 * y1;
                double px1 = 0.25 * x0 + 0.75 * x1;  // Punkt 1
                double py1 = 0.25 * y0 + 0.75 * y1;

                // Füge die neuen Punkte zum Ergebnis-Polygon hinzu
                result.addPoint((int) px0, (int) py0);
                result.addPoint((int) px1, (int) py1);
            }
            return result;  // Gibt das unterteilte Polygon zurück
        }

        // Diese Methode wird aufgerufen, wenn auf das Panel geklickt wird
        @Override
        public void mouseClicked(MouseEvent e) {
            polygon.addPoint(e.getX(), e.getY());  // Fügt den geklickten Punkt zum Polygon hinzu
            repaint();  // Aktualisiert die Anzeige (Panel wird neu gezeichnet)
        }

        // Leere Implementierungen für die anderen MouseListener-Methoden
        @Override public void mousePressed(MouseEvent e) {}
        @Override public void mouseReleased(MouseEvent e) {}
        @Override public void mouseEntered(MouseEvent e) {}
        @Override public void mouseExited(MouseEvent e) {}
    }
}