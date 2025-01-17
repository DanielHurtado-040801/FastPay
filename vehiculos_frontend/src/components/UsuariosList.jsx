import { useEffect, useState } from "react";
import { getAllUsers } from "../api/usuarios.api";
import { UsuariosCard } from "./UsuariosCard";

export function UsuariosList() {
  const [usuarios, setUsuarios] = useState([]);

  useEffect(() => {
    //En esta funcion asincrona realizamos la consulta a nuestro back para obtener todos los usuarios
    async function cargarUsuarios() {
      const respuesta = await getAllUsers();
      setUsuarios(respuesta.data);
    }
    cargarUsuarios();
  }, []);

  return (
    <div className="grid grid-cols-1 gap-3 md:grid-cols-2 lg:grid-cols-3 rounded-lg pb-3 grow">
      {usuarios.map((usuario) => (
        <UsuariosCard key={usuario.id} usuario={usuario}></UsuariosCard>
      ))}
    </div>
  );
}
