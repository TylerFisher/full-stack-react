import { ORM } from 'redux-orm';

import Body from './body';
import Division from './division';
import DivisionLevel from './divisionLevel';
import Office from './office';
import Officeholder from './officeholder';
import Party from './party';
import Person from './person';

const orm = new ORM();

orm.register(
  Body,
  Division,
  DivisionLevel,
  Office,
  Officeholder,
  Party,
  Person
);

export default orm;
