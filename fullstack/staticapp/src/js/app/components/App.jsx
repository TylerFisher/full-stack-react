import React from 'react';
import { connect } from 'react-redux';
import { officeSelector } from '../stores/orm/reducers';
import Table from './table';

const App = (props) => {
  if (props.offices.length === 0) return null;
  if (props.offices.length > 0 && !props.offices[0]) return null;
  return (
    <Table offices={props.offices} />
  );
};

const mapStateToProps = state => ({
  offices: officeSelector(state),
});

export default connect(mapStateToProps)(App);
