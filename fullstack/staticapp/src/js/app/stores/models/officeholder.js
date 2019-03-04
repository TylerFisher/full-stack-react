import { attr, fk, Model } from 'redux-orm';

class Officeholder extends Model {
  serialize() {
    return this.ref;
  }

  static get fields() {
    return {
      id: attr(),
      term_start: attr(),
      term_end: attr(),
      person: fk('Person'),
      office: fk('Office'),
      party: fk('Party'),
    };
  }
}

Officeholder.modelName = 'Officeholder';

export default Officeholder;
