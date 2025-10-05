package clases;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
/**
 *
 * @author USUARIO
 */
public class Usuario {
    private int id;
    private String Nombre;
    private String Apellido;
    private String Email;
    private String Username;
    private String Clave;
    private String Rol;

    public Usuario(int id, String Nombre, String Apellido, String Email, String Username, String Clave, String Rol) {
        this.id = id;
        this.Nombre = Nombre;
        this.Apellido = Apellido;
        this.Email = Email;
        this.Username = Username;
        this.Clave = Clave;
        this.Rol = Rol;

    }

    public Usuario() {

    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String nombre) {
        Nombre = nombre;
    }

    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String apellido) {
        Apellido = apellido;
    }

    public String getEmail() {
        return Email;
    }

    public void setEmail(String email) {
        Email = email;
    }

    public String getUsername() {
        return Username;
    }

    public void setUsername(String username) {
        Username = username;
    }

    public String getClave() {
        return Clave;
    }

    public void setClave(String clave) {
        Clave = clave;
    }

    public String getRol() {
        return Rol;
    }

    public void setRol(String rol) {
        Rol = rol;
    }


    public static Usuario validarUsuario(String username, String clave) {
        Connection conn = Conector.obtenerconexion();

        //esto lo que hace es verificar si la conexion fallo y si fallo muestra un mensaje y devuelve null.
        if (conn == null) {
            System.out.println("no se pudo conectar a la base de datos");
            return null;
        }
        try {
            // aqui defimimos la consulta sql y los signos de ? se remplazan por el datos reales.
            String sql = "SELECT * FROM usuarios WHERE Username = ? AND Clave = ? ";
            // esto lo hace es hacer una consulta segura y que haiga inyecciones SQL.
            PreparedStatement ps = conn.prepareStatement(sql);

            // aqui replazamos los signos de interogacion por los parametros que le dimos al metodo arriba
            ps.setString(1, username);
            ps.setString(2, clave);
            //  ejecuta la consulta que hicmos arriba y guarda los valores en rs.
            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                // creamos un nuevo objeto clases.Usuario

                Usuario u = new Usuario();
                // aqui lo que estamos haciendo es asignando los valores que vienen de la base de datos.
                u.setId(rs.getInt("id"));
                u.setNombre(rs.getString("Nombre"));
                u.setApellido(rs.getString("Apellido"));
                u.setEmail(rs.getString("Email"));
                u.setUsername(rs.getString("Username"));
                u.setClave(rs.getString("Clave"));
                u.setRol(rs.getString("Rol"));
                rs.close();
                ps.close();
                conn.close();

                return u;
            } else {
                rs.close();
                ps.close();
                conn.close();
                return null;
            }

        } catch (SQLException e) {
            System.out.println("error al validar usuario: " + e.getMessage());
            return null;
        }
    }
}


