import React from 'react';
import Row from './Row';

class Table extends React.Component {
  render() {
    return (
      <table>
        <thead>
          <tr>
            <th>Officeholder</th>
            <th>Party</th>
            <th>Division</th>
          </tr>
        </thead>
        <tbody>
          {this.props.offices.map(office => (
            <Row office={office} key={office.id} />
          ))}
        </tbody>
      </table>
    );
  }
}

export default Table;
