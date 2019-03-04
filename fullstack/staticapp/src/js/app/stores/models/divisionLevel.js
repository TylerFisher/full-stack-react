import { attr, fk, Model } from 'redux-orm';

class DivisionLevel extends Model {
  serialize() {
    return this.ref;
  }

  static get fields() {
    return {
      id: attr(),
      slug: attr(),
      name: attr(),
      parent: fk('DivisionLevel'),
    };
  }
}

DivisionLevel.modelName = 'DivisionLevel';

export default DivisionLevel;
