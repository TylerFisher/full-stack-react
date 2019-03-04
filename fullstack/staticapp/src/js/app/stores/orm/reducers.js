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
