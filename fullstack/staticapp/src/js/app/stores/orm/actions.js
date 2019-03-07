import * as types from './constants';

export const createDivisions = divisions => ({
  type: types.CREATE_DIVISIONS,
  divisions,
});

export const createDivisionLevels = divisionLevels => ({
  type: types.CREATE_DIVISION_LEVELS,
  divisionLevels,
});

export const createOffices = offices => ({
  type: types.CREATE_OFFICES,
  offices,
});

export const createOfficeholders = officeholders => ({
  type: types.CREATE_OFFICEHOLDERS,
  officeholders,
});

export const createParties = parties => ({
  type: types.CREATE_PARTIES,
  parties,
});

export const createPeople = people => ({
  type: types.CREATE_PEOPLE,
  people,
});
