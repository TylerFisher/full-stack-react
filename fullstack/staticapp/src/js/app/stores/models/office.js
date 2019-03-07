import { attr, fk, Model } from 'redux-orm';

class Office extends Model {
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
      senate_class: attr(),
      division: fk('Division'),
    };
  }
}

Office.modelName = 'Office';

export default Office;
