import { attr, fk, Model } from 'redux-orm';

class Body extends Model {
  serialize() {
    return this.ref;
  }

  static get fields() {
    return {
      id: attr(),
      slug: attr(),
      label: attr(),
      short_label: attr(),
      parent: fk('Body'),
    };
  }
}

Body.modelName = 'Body';

export default Body;
