import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import App from './app/components/App';
import store from './app/stores/';

import '../scss/main.scss';

const MasterApp = () => (
  <Provider store={store}>
    <App />
  </Provider>
);

console.log('hey');

render(
  <MasterApp />,
  document.getElementById('app')
);
