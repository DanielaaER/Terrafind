import React, { useState } from 'react';

import { FaMapMarkerAlt } from 'react-icons/fa';

const EstadosSelector = ({ label, estadoSeleccionado, setEstadoSeleccionado }) => {
  const estados = [
      "Aguascalientes",
      "Baja California",
      "Baja California Sur",
      "Campeche",
      "Coahuila de Zaragoza",
      "Colima",
      "Chiapas",
      "Chihuahua",
      "Ciudad de México",
      "Durango",
      "Guanajuato",
      "Guerrero",
      "Hidalgo",
      "Jalisco",
      "México",
      "Michoacán de Ocampo",
      "Morelos",
      "Nayarit",
      "Nuevo León",
      "Oaxaca",
      "Puebla",
      "Querétaro",
      "Quintana Roo",
      "San Luis Potosí",
      "Sinaloa",
      "Sonora",
      "Tabasco",
      "Tamaulipas",
      "Tlaxcala",
      "Veracruz",
      "Yucatán",
      "Zacatecas"
    ];


    const [inputValue, setInputValue] = useState('');
    const [showAutocomplete, setShowAutocomplete] = useState(false);
    const [autocompletedValue, setAutocompletedValue] = useState('');
  
    const handleChange = (event) => {
      const inputValue = event.target.value;
      setInputValue(inputValue);
      setAutocompletedValue('');
      setShowAutocomplete(true);
    };
  
    const handleOptionClick = (estado) => {
      setInputValue(estado);
      setEstadoSeleccionado(estados.indexOf(estado) + 1); // Devolver el número del estado
      setAutocompletedValue('');
      setShowAutocomplete(false);
    };
  
    return (
      <div>
        <label>
          <FaMapMarkerAlt />{' '}
        </label>
  
        <input
          type="text"
          value={inputValue}
          onChange={handleChange}
          placeholder={label}
        />
  
        {showAutocomplete && (
          <ul className="autocomplete-list">
            {estados
              .filter((estado) =>
                estado.toLowerCase().startsWith(inputValue.toLowerCase())
              )
              .map((estado) => (
                <li
                  key={estado}
                  onClick={() => handleOptionClick(estado)}
                  className={estado === autocompletedValue ? 'autocompleted' : ''}
                >
                  {estado}
                </li>
              ))}
          </ul>
        )}
      </div>
    );
  };
  
  export default EstadosSelector;