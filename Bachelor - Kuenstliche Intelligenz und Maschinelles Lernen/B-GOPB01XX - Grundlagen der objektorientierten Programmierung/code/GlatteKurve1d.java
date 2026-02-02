import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GlatteKurve1d extends JFrame {

    // Konstruktor der Hauptklasse
    public GlatteKurve1d() {
        setTitle("Kurve");  // Setzt den Titel des Fensters
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  // Das Programm schließt, wenn das Fenster geschlossen wird
        setSize(600, 600);  // Setzt die Fenstergröße auf 600x600 Pixel
        setLocationRelativeTo(null);  // Fenster wird auf dem Bildschirm zentriert
        add(new KurvePanel());  // Fügt das Panel (Zeichenfläche) hinzu
        setVisible(true);  // Macht das Fenster sichtbar
    }

    // Main-Methode zum Starten des Programms
    public static void main(String[] args) {
        new GlatteKurve1d();  // Erzeugt ein neues Fenster der Hauptklasse
    }

    // Inneres Panel zum Zeichnen der Kurve
    class KurvePanel extends JPanel implements MouseListener {

        private Polygon polygon = new Polygon();  // Instanzvariable für das Polygon

        // Konstruktor für das Panel
        public KurvePanel() {
            addMouseListener(this);  // Registriert das Panel als MouseListener für Mausereignisse
        }

        // Methode zum Zeichnen des Panels
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);  // Ruft die Basismethode auf, um den Hintergrund zu löschen
            Graphics2D g2 = (Graphics2D) g;  // Erstellen eines Graphics2D Objekts für feinere Kontrolle beim Zeichnen

            // Zeichne das ursprüngliche Kontrollpolygon (schwarz und dünn)
            g2.setColor(Color.BLACK);  // Setzt die Farbe auf Schwarz
            g2.setStroke(new BasicStroke(1));  // Setzt die Strichstärke auf 1 Pixel
            g2.drawPolygon(polygon);  // Zeichnet das Polygon

            // Unterteilte glatte Kurve (rot und dicker), wenn mindestens 3 Punkte
            if (polygon.npoints >= 3) {
                Polygon smooth = subdivide(polygon, 5);  // Erzeugt eine geglättete Kurve durch 5 Schritte der Unterteilung
                g2.setColor(Color.RED);  // Setzt die Farbe auf Rot für die Kurve
                g2.setStroke(new BasicStroke(2));  // Setzt eine dickere Linie für die Kurve
                g2.drawPolyline(smooth.xpoints, smooth.ypoints, smooth.npoints);  // Zeichnet die geglättete Kurve
            }
        }

        // Corner-Cutting Algorithmus (ein Schritt)
        private Polygon subdivide(Polygon polygon) {
            Polygon result = new Polygon();  // Ergebnis-Polygon für die Unterteilung
            int n = polygon.npoints;  // Anzahl der Punkte im Polygon

            // Durchlaufe alle Punkte des Polygons und berechne neue Zwischenpunkte
            for (int i = 0; i < n; i++) {
                int x0 = polygon.xpoints[i];
                int y0 = polygon.ypoints[i];
                int x1 = polygon.xpoints[(i + 1) % n];  // Der nächste Punkt, zyklisch (letzter Punkt geht zurück zum ersten)
                int y1 = polygon.ypoints[(i + 1) % n];

                // Berechne neue Punkte durch Corner Cutting (75% und 25% Gewichtung)
                double xA = 0.75 * x0 + 0.25 * x1;
                double yA = 0.75 * y0 + 0.25 * y1;

                double xB = 0.25 * x0 + 0.75 * x1;
                double yB = 0.25 * y0 + 0.75 * y1;

                result.addPoint((int) xA, (int) yA);  // Füge die neuen Punkte zum Ergebnis-Polygon hinzu
                result.addPoint((int) xB, (int) yB);
            }
            return result;  // Gibt das unterteilte Polygon zurück
        }

        // Mehrfaches Subdividing (5 Schritte empfohlen)
        private Polygon subdivide(Polygon polygon, int steps) {
            Polygon result = polygon;  // Initialisiere das Ergebnis mit dem ursprünglichen Polygon
            for (int i = 0; i < steps; i++) {
                result = subdivide(result);  // Wiederhole die Unterteilung für die angegebene Anzahl von Schritten
            }
            return result;  // Gibt das final unterteilte Polygon zurück
        }

        // MouseListener: Nur die Methode mouseClicked interessiert uns
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