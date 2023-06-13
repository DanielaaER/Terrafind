import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

import EstadosSelector from './EstadosSelector';
import { FaMap } from 'react-icons/fa';

const App = () => {
  const [estadoOrigen, setEstadoOrigen] = useState('');
  const [estadoDestino, setEstadoDestino] = useState('');
  const [mapUrl, setMapUrl] = useState(`${process.env.PUBLIC_URL}/search.html`);
  const [resultado, setResultado] = useState(null); // Estado para almacenar los datos recibidos del backend
  const [mapaSeleccionado, setMapaSeleccionado] = useState('buscar'); // Estado para almacenar el mapa seleccionado


  const handleBuscar = async event => {
    event.preventDefault(); // Prevenir el comportamiento predeterminado del botón

    // Realizar la solicitud POST
    const result = await axios.post('http://40.119.51.181:5000/terrafind', { edoOrigen: estadoOrigen, edoDestino: estadoDestino });

    console.log(result.data);
    const resultado = result.data


    // const municipiosMostrar = [estadoDestino, estadoOrigen];
    // Manejar la respuesta del servidor aquí

    // await axios
    //   .post('http://localhost:5000/buscar', { municipios_mostrar: municipiosMostrar })
    // setMapaSeleccionado('buscar'); // Cambiar al mapa de búsqueda después de recibir la respuesta del servidor
    await axios
      .post('http://127.0.0.1:5000/ruta', { municipios_mostrar: resultado })
    
  };

  const handleEnviar = event => {
    event.preventDefault(); // Prevenir el comportamiento predeterminado del botón


    // Cambiar al mapa de búsqueda
    setMapaSeleccionado('enviar');
  };

  return (
    <div className="app-container">
      <div className="lado-izquierdo">
        {mapaSeleccionado === 'buscar' && <iframe src={`${process.env.PUBLIC_URL}/search.html`} title="Search" width="100%" height="100%" frameBorder="0"></iframe>}
        {mapaSeleccionado === 'enviar' && <iframe src={`${process.env.PUBLIC_URL}/route.html`} title="Ruta" width="100%" height="100%" frameBorder="0"></iframe>}
      </div>

      <div className="lado-derecho">
        <div className="terrafind-container">
          <h2>
            <FaMap /> Terrafind
          </h2>
        </div>
        <div className="selector-container">
          <EstadosSelector label="Origen" estadoSeleccionado={estadoOrigen} setEstadoSeleccionado={setEstadoOrigen} />
        </div>
        <div className="selector-container">
          <EstadosSelector label="Destino" estadoSeleccionado={estadoDestino} setEstadoSeleccionado={setEstadoDestino} />
        </div>
        <div className="button-container">
          <button className="button-send" onClick={handleBuscar}>
            Buscar
          </button>
          <button className="button-send" onClick={handleEnviar}>
            Enviar
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
