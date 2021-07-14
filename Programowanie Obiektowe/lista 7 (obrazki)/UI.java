import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.Serializable;
import java.io.*;


public class UI {
    static class Ksiazka implements Serializable{
        static final long serialVersionUID = 1;
        String pole1, pole2, pole3, filename;


        Ksiazka(String filename) {
            this.pole1 = "";
            this.pole2 = "";
            this.pole3 = "";
            this.filename = filename;
        }

        public String toString() {
            return "<" + pole1 + "," + pole2 + "," + pole3 + ">";
        }

        public void edit() {
            new EditUI(this);
        }

        public void save() {
            try{
                FileOutputStream fout = new FileOutputStream(filename);  
                ObjectOutputStream out = new ObjectOutputStream(fout);  
                out.writeObject(this);
                out.close();
    
                System.out.println("Serialised");
            }catch(Exception e){System.out.println(e);}  
        }

        public Ksiazka load() {
            try {
                ObjectInputStream fin = new ObjectInputStream(new FileInputStream(filename));  
                Ksiazka out = (Ksiazka)fin.readObject();  
                fin.close();

                System.out.println("Deserialised");
                return out;
            }catch(Exception e) {
                System.out.println(e);
                return this;
            }
        }
    }

    static class WydawnictwoCiagle extends Ksiazka {
        static final long serialVersionUID = 2;

        WydawnictwoCiagle(String filename) {
            super(filename);
        }
    }

    static class Czasopismo extends Ksiazka {
        static final long serialVersionUID = 3;

        Czasopismo(String filename) {
            super(filename);
        }
    }

    static class EditUI implements ActionListener{
        JTextField tfs[] = new JTextField[3];
        Ksiazka ks;
        int HEIGHT = 30;
        EditUI(Ksiazka ks) {
            this.ks = ks;
            
            JFrame f = new JFrame("EditUI");
            JPanel panel = new JPanel();
            panel.setLayout(null);
            panel.setBounds(0,0,215,250);
            panel.setBackground(Color.lightGray);  

            for(int i = 0; i < 3; i++) {
                tfs[i] = new JTextField();
                tfs[i].setBounds(50, 50 + HEIGHT*i, 100, HEIGHT);
                tfs[i].setForeground(Color.orange);
                tfs[i].setBackground(Color.darkGray);
                tfs[i].setCaretColor(Color.orange);
                tfs[i].setBorder(BorderFactory.createLineBorder(Color.black));
                tfs[i].setToolTipText("Pole" + String.valueOf(i+1));
                panel.add(tfs[i]);
            }
            tfs[0].setText(ks.pole1);
            tfs[0].setCaretPosition(tfs[0].getText().length());
            tfs[1].setText(ks.pole2);
            tfs[1].setCaretPosition(tfs[1].getText().length());
            tfs[2].setText(ks.pole3);
            tfs[2].setCaretPosition(tfs[2].getText().length());

            
            JButton b = new JButton("Save");
            b.setBounds(50,50+3*HEIGHT,100, HEIGHT);
            b.setBackground(Color.orange);
            b.setFocusPainted(false);
            b.addActionListener(this);
            panel.add(b);


            f.add(panel);
            f.setSize(215,250);
            f.setResizable(false);
            f.setLayout(null);
            f.setLocationRelativeTo(null);
            f.setVisible(true);           
        }

        public void actionPerformed(ActionEvent e) { 
            ks.pole1 = tfs[0].getText();
            ks.pole2 = tfs[1].getText();
            ks.pole3 = tfs[2].getText();
            ks.save();
        } 
    }

public static void main(String[] args) {

        

        switch(args[1]) {
            case "Ksiazka":
                Ksiazka k = new Ksiazka(args[0]);
                k.load().edit();
                break;
            case "WydawnictwoCiagle":
                WydawnictwoCiagle w = new WydawnictwoCiagle(args[0]);
                w.load().edit();
                break;
            case "Czasopismo":
                Czasopismo c = new Czasopismo(args[0]);
                c.load().edit();
                break;
            default:
                throw new IllegalArgumentException("Invalid Arguments");
          }
    }
}