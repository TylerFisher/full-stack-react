import { attr, Model } from 'redux-orm';

class Party extends Model {
  serialize() {
    return this.ref;
  }

  static get fields() {
    return {
      id: attr(),
      slug: attr(),
      label: attr(),
      short_label: attr(),
    };
  }
}

Party.modelName = 'Party';

export default Party;
