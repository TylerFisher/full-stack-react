import React from 'react';
import Row from './Row';

class Table extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentBody: 'senate',
    }

    this.changeBody = this.changeBody.bind(this);
  }

  changeBody() {
    this.setState({
      currentBody: this.state.currentBody === 'senate' ? 'house' : 'senate',
    });
  }

  render() {
    const filteredOffices = this.props.offices.filter(office => office.body.slug === this.state.currentBody);

    filteredOffices.sort((a, b) => {
      if (a.division.code > b.division.code) return 1;
      if (b.division.code > a.division.code) return -1;
      return 0;
    });

    return (
      <div className="wrapper">
        <button className="change-body" onClick={this.changeBody}>Change body</button>
        <table>
          <thead>
            <tr>
              <th>Officeholder</th>
              <th>Party</th>
              <th>Division</th>
            </tr>
          </thead>
          <tbody>
            {filteredOffices.map(office => (
              <Row office={office} key={office.id} />
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default Table;
