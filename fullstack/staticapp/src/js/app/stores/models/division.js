import { attr, fk, Model } from 'redux-orm';

class Division extends Model {
  serialize() {
    return this.ref;
  }

  static get fields() {
    return {
      id: attr(),
      slug: attr(),
      name: attr(),
      label: attr(),
      short_label: attr(),
      code: attr(),
      parent: fk('Division'),
      level: fk('DivisionLevel'),
    };
  }
}

Division.modelName = 'Division';

export default Division;
