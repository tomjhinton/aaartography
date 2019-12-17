import React from 'react'
import ReactDOM from 'react-dom'
import { HashRouter as Router, Switch, Route } from 'react-router-dom'
import 'bulma'
import './style.scss'

import Map from './components/front/Map'
import Header from './components/front/Header'
import Footer from './components/front/Footer'


class App extends React.Component {
  constructor(){
    super()

    this.state = {
    }
  }

  componentDidMount() {

  }

  render() {
    return (

      <Router>
        <main>
          <Header />
          <Switch>
            <Route path="/" component={Map} />

          </Switch>

        </main>
        <footer>
          <Footer/>
        </footer>
      </Router>


    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
