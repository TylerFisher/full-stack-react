import { applyMiddleware, combineReducers, compose, createStore } from 'redux';
import thunkMiddleware from 'redux-thunk';
import ormReducers from './orm/reducers';
import { fetchData } from './orm/api';

const reducers = combineReducers({
  orm: ormReducers,
});

const store = createStore(reducers, compose(
  applyMiddleware(thunkMiddleware),
  window.__REDUX_DEVTOOLS_EXTENSION__ ? window.__REDUX_DEVTOOLS_EXTENSION__() : f => f
));

store.dispatch(fetchData());

export default store;
