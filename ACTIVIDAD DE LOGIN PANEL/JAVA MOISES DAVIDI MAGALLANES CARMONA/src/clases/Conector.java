/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package clases;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
/**
 *
 * @author USUARIO
 */
public class Conector {
    private static final String URL = "jdbc:mysql://localhost:3306/login_db";
    private static final String USURIO = "root";
    private  static final String Clave = "";


    public static Connection obtenerconexion(){
        try {
         return DriverManager.getConnection(URL,USURIO,Clave);
        } catch (SQLException e) {
            System.out.println("error al conectar: " + e.getMessage());
            return null;
        }
    }
}


