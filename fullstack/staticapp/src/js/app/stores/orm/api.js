import assign from 'lodash/assign';
import * as actions from './actions';

const headers = {
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json',
  },
};

const GET = assign({}, headers, { method: 'GET' });

function addDivisions(divisions, dispatch) {
  dispatch(actions.createDivisions(divisions));
}

function addDivisionLevels(divisionLevels, dispatch) {
  dispatch(actions.createDivisionLevels(divisionLevels));
}

function addOffices(offices, dispatch) {
  dispatch(actions.createOffices(offices));
}

function addOfficeholders(officeholders, dispatch) {
  dispatch(actions.createOfficeholders(officeholders));
}

function addParties(parties, dispatch) {
  dispatch(actions.createParties(parties));
}

function addPeople(people, dispatch) {
  dispatch(actions.createPeople(people));
}

const fetchDivisions = () =>
  dispatch => fetch('/api/divisions/', GET)
    .then(response => response.json())
    .then(data => Promise.all([
      addDivisions(data, dispatch),
    ])).catch((error) => {
      console.log('API Error fetchDivisions', error, error.code);
    });

const fetchDivisionLevels = () =>
  dispatch => fetch('../api/division-levels/', GET)
    .then(response => response.json())
    .then(data => Promise.all([
      addDivisionLevels(data, dispatch),
    ])).catch((error) => {
      console.log('API Error fetchDivisionLevels', error, error.code);
    });

const fetchOffices = () =>
  dispatch => fetch('../api/offices/', GET)
    .then(response => response.json())
    .then(data => Promise.all([
      addOffices(data, dispatch),
    ])).catch((error) => {
      console.log('API Error fetchOffices', error, error.code);
    });

const fetchOfficeholders = () =>
  dispatch => fetch('../api/officeholders/', GET)
    .then(response => response.json())
    .then(data => Promise.all([
      addOfficeholders(data, dispatch),
    ])).catch((error) => {
      console.log('API Error fetchOfficeholders', error, error.code);
    });

const fetchParties = () =>
  dispatch => fetch('../api/parties/', GET)
    .then(response => response.json())
    .then(data => Promise.all([
      addParties(data, dispatch),
    ])).catch((error) => {
      console.log('API Error fetchParties', error, error.code);
    });

const fetchPeople = () =>
  dispatch => fetch('../api/people/', GET)
    .then(response => response.json())
    .then(data => Promise.all([
      addPeople(data, dispatch),
    ])).catch((error) => {
      console.log('API Error fetchPeople', error, error.code);
    });

export const fetchData = () =>
  dispatch => Promise.all([
    dispatch(fetchDivisions()),
    dispatch(fetchDivisionLevels()),
    dispatch(fetchOffices()),
    dispatch(fetchOfficeholders()),
    dispatch(fetchParties()),
    dispatch(fetchPeople()),
  ]);
