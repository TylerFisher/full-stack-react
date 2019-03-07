import React from 'react';
import Row from './Row';

class Table extends React.Component {
  render() {
    return (
      <div className='wrapper'>
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
      </div>
    );
  }
}

export default Table;
