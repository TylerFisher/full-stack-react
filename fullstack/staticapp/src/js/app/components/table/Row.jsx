import React from 'react';

class Row extends React.Component {
  render() {
    const { office } = this.props;
    return (
      <tr>
        <td>{office.officeholder.person.full_name}</td>
        <td>{office.officeholder.party.label}</td>
        <td>{office.division.label}</td>
      </tr>
    );
  }
}

export default Row;
