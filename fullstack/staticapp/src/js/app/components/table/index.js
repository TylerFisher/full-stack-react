import React from 'react';
import Row from './Row';

class Table extends React.Component {
  render() {
    const sortedOffices = this.props.offices.sort((a, b) => {
      if (a.division.code > b.division.code) return 1;
      if (b.division.code > a.division.code) return -1;
      return 0;
    });

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
