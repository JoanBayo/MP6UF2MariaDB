Haz un CSS para java, para la siguiente tabla de jugadores de un equipo de futbol
                <h2>Madrid</h2>
                <p>1932<p>
                <p>Madrid<p>
                <p>Santiago bernabe<p>
            </div>
            <div>
                <table id="customers">
                    <tr>
                        <th>Número</th>
                        <th>Nombre</th>
                        <th>Poscicion</th>
                        <th>Nacimiento</th>
                        <th>Altura</th>
                        <th>Valor de Mercado</th>
                    </tr>
                    <tr>
                       <td>12</td>
                       <td>Manolo</td>
                       <td>Mediocentro</td>
                       <td>13/12/2002</td>
                       <td>1.67</td>
                       <td>300</td>
                    </tr>
                </table>
            </div>ipos.nombre,equipos.ciudad, equipos.estadio, equipos.fundacion FROM jugadores INNER JOIN equipos ON jugadores.equipos_id = equipos.idequipo WHERE equipos.idequipo = 1