![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# full-stack-react-example

### Quickstart

First, install requirements and load data

```
$ cd example
$ pipenv install
$ pipenv run python manage.py migrate
$ pipenv run python manage.py loaddata fixtures.json
$ cd ../fullstack/staticapp
$ npm install
```

##### Running a development server

Developing python files? Move into example directory and run the development server with pipenv.

  ```
  $ cd example
  $ pipenv run python manage.py runserver
  ```

Developing static assets? Move into the pluggable app's staticapp directory and start the node development server. Note that you need the Python server running in a separate tab.

  ```
  $ cd fullstack/staticapp
  $ npm start
  ```


## The class!

##### What are we doing

We're going to add a button to the top of the table that switches between senators and representatives.

##### What we need to do

We need to:

- Add a Body model to Redux ORM
- Fetch the Body data from the Body API and add it to our redux store
- Add it to our selector to pass to React
- Create the button and use the Body data to toggle

##### Step one: add a Body model to Redux ORM

To add the Body model to our ORM, we'll need to touch three files. First, we need to create our body model file. Create a file at `fullstack/staticapp/src/js/app/stores/models/body.js`. Add this code to the file:

```
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
```

Next, we need to attach this model to our Office model, since all Offices belong to a Body. Open `fullstack/staticapp/src/js/app/stores/models/office.js`. In the `fields()` function, add a foreign key to the Body model:

```
static get fields() {
  return {
    id: attr(),
    slug: attr(),
    name: attr(),
    label: attr(),
    short_label: attr(),
    senate_class: attr(),
    division: fk('Division'),
    body: fk('Body'), // <-- this line right here
  };
}
```

Finally, we need to register the model to our ORM. Open `fullstack/staticapp/src/js/app/stores/models/index.js`. First, above line 3, import the body file:

```
import Body from './body';
```

Then, in the ORM register function, add `Body` as a parameter to the function call:

```
orm.register(
  Body,
  Division,
  DivisionLevel,
  Office,
  Officeholder,
  Party,
  Person
);
```

Now we have a Body model!

##### Step two: Fetch the Body data from the Body API and add it to our redux store

We already have a body API working on our backend. We just need to fetch it and add it to the redux store. We're going to have to write a lot of boilerplate code to get there.

First, open `fullstack/staticapp/src/js/app/stores/orm/constants.js` and add the following line to the file:

```
export const CREATE_BODIES = 'CREATE_BODIES';
```

Then, open `fullstack/staticapp/src/js/app/stores/orm/actions.js` and add the following lines to the file:

```
export const createBodies = bodies => ({
  type: types.CREATE_BODIES,
  bodies,
});
```

Next, open `fullstack/staticapp/src/js/app/stores/orm/reducers.js` and find where we create an ORM session and pull out the models. Change the statement beginning on line 11 to this:

```
const {
  Body,
  Division,
  DivisionLevel,
  Office,
  Officeholder,
  Party,
  Person,
} = session;
```


Next, find the big switch statement starting on line 21. Add a new case that looks like this:

```
case types.CREATE_BODIES:
  action.bodies.map(body => Body.upsert(body));
  break;
```

Finally, open `fullstack/staticapp/src/js/app/stores/orm/api.js`. We're going to add two functions to this file:

```
function addBodies(bodies, dispatch) {
  dispatch(actions.createBodies(bodies));
}
```

```
const fetchBodies = () =>
  dispatch => fetch('/api/bodies/', GET)
    .then(response => response.json())
    .then(data => Promise.all([
      addBodies(data, dispatch),
    ])).catch((error) => {
      console.log('API Error fetchBodies', error, error.code);
    });
```

At the bottom of the file, there's a function called `fetchData()`. In that function is a promise that calls all of our individual fetch functions. Add `fetchBodies` to that array.

```
export const fetchData = () =>
  dispatch => Promise.all([
    dispatch(fetchBodies()),
    dispatch(fetchDivisions()),
    dispatch(fetchDivisionLevels()),
    dispatch(fetchOffices()),
    dispatch(fetchOfficeholders()),
    dispatch(fetchParties()),
    dispatch(fetchPeople()),
  ]);
```

Now we have data in our redux store!

##### Step three: add body data to our selector

To get the data to React, we need to add the body of an office to the office selector. Open `fullstack/staticapp/src/js/app/stores/orm/reducers.js`. Go to the `officeSelector` function and find the return statement on line 59. Change it to look like this:

```
return Object.assign({}, obj, {
  division: office.division.serialize(),
  body: office.body.serialize(), // <-- we're adding this!
  officeholder: {
    person: officeholder.person.serialize(),
    party: officeholder.party.serialize(),
  },
});
```

##### Step four: create the button

Now, finally, our data has made it to React and we can use it to create a button. Open `fullstack/staticapp/src/js/app/components/table/index.js`. We need to do a few things here. First, let's create our button.

```
render() {
  return (
    <div className='wrapper'>
        <button>Change body</button>
        ...
```

It doesn't do anything yet. We need to know what body we're filtered to currently. That means the component needs its own internal state. To do that, we're going to add a constructor to our class, above the render function, that looks like this:

```
constructor(props) {
  super(props);

  this.state = {
    currentBody: 'senate',
  };
}
```

Next, we're going to use this state to filter the offices that we are showing. Add the following to the top of the render function:

```
const filteredOffices = this.props.offices.filter(office => office.body.slug === this.state.currentBody);
```

Then, change lines 34-36 to read:

```
{filteredOffices.map(office => (
  <Row office={office} key={office.id} />
))}
```

Our button still doesn't do anything. It needs an event listener for clicks, so that it can change the state. First, let's write the function. Add this below the constructor:

```
changeBody() {
  this.setState({
    currentBody: this.state.currentBody === 'senate' ? 'house' : 'senate',
  });
}
```

Then, add an `onClick` handler to our button:

```
<button onClick={this.changeBody}>Change body</button>
```

Oops, this actually errors out. We need to add one more thing to our constructor so that our change function has the ability to change the component's state:

```
this.changeBody = this.changeBody.bind(this);
```

Now try your button. It works! We're done!
