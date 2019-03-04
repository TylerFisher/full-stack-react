import React from 'react';
import { connect } from 'react-redux';
import orm from '../stores/models';

const App = (props) => {
  const session = orm.session(props.db.orm);
  return (
    <div />
  );
};

const mapStateToProps = state => ({
  db: state,
});

export default connect(mapStateToProps)(App);
