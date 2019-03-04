import { attr, fk, Model } from 'redux-orm';

class Person extends Model {
  serialize() {
    return this.ref;
  }

  static get fields() {
    return {
      id: attr(),
      slug: attr(),
      last_name: attr(),
      first_name: attr(),
      middle_name: attr(),
      suffix: attr(),
      full_name: attr(),
      gender: attr(),
      birth_date: attr(),
    };
  }
}

Person.modelName = 'Person';

export default Person;
