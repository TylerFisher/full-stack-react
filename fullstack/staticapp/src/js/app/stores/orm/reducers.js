import { createSelector } from 'redux-orm';
import * as types from './constants';
import orm from '../models/';

export default(dbState, action) => {
  if (typeof dbState === 'undefined') {
    return orm.getEmptyState();
  }

  const session = orm.session(dbState);
  const {
    Body,
    Division,
    DivisionLevel,
    Office,
    Officeholder,
    Party,
    Person,
  } = session;

  switch (action.type) {
    case types.CREATE_BODIES:
      action.bodies.map(body => Body.upsert(body));
      break;
    case types.CREATE_DIVISIONS:
      action.divisions.map(division => Division.upsert(division));
      break;
    case types.CREATE_DIVISION_LEVELS:
      action.divisionLevels.map(divisionLevel => DivisionLevel.upsert(divisionLevel));
      break;
    case types.CREATE_OFFICES:
      action.offices.map(office => Office.upsert(office));
      break;
    case types.CREATE_OFFICEHOLDERS:
      action.officeholders.map(officeholder => Officeholder.upsert(officeholder));
      break;
    case types.CREATE_PARTIES:
      action.parties.map(party => Party.upsert(party));
      break;
    case types.CREATE_PEOPLE:
      action.people.map(person => Person.upsert(person));
      break;
    default:
      break;
  }
  return session.state;
};

export const officeSelector = createSelector(
  orm,
  state => state.orm,
  session => {
    return session.Office
      .all()
      .toModelArray()
      .map(office => {
        if (!office.division) return null;
        const officeholder = office.officeholderSet.toModelArray()[0];
        if (!officeholder.person) return null;

        const obj = office.serialize();

        return Object.assign({}, obj, {
          division: office.division.serialize(),
          body: office.body.serialize(),
          officeholder: {
            person: officeholder.person.serialize(),
            party: officeholder.party.serialize(),
          },
        });
      })
      .sort((a, b) => {
        if (!a || !b) return 0;
        if (a.division.code > b.division.code) return 1;
        if (b.division.code > a.division.code) return -1;
        return 0;
      });
  }
);
