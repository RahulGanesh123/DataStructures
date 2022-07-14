import React, {Component} from 'react'
import CardList from '../components/CardList'
import SearchBox from '../components/SearchBox'
import './App.css'
import Scroll from '../components/Scroll'
import 'tachyons'
import ErrorBoundary from '../components/ErrorBoundary'


/*We need to extend Component in order to access the render() method.*/
class App extends Component {
	constructor() {
		super() /*We need to call super() because we are extending the Component Super class*/
		this.state = {
			'robots': [],
			'searchField': ''
		}
	}
	componentDidMount() {
		fetch('https://jsonplaceholder.typicode.com/users')
		.then(response => {
			return response.json()
		})
		.then(users=> {
			this.setState({robots : users})
		})
	}
	onSearchChange = (event) => {
		this.setState({searchField : event.target.value})
	}
	render() {
		const {robots, searchField} = this.state
		const filteredRobots = robots.filter(robot => {
			return robot.name.toLowerCase().includes(searchField.toLowerCase())
		})
		if(!robots.length){ 
			return <h1 className='tc'> Loading </h1>
		}
		else{
			return (
				<div className = 'tc'>
					<h1 className = 'f1'>RoboFriends</h1>
					<SearchBox searchChange={this.onSearchChange}/>
					{/* We have to destructure robots because remeber that we didnt use export default. So theoretically, there could be more than on export than robots, thats why we destructure it*/}
					<Scroll>
						<ErrorBoundary>
							<CardList robots = {filteredRobots}/>
						</ErrorBoundary>
					</Scroll>
				</div>
			)
	    }
    }
}

export default App