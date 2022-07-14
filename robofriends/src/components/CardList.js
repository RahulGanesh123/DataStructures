import React from 'react'
import Card from './Card'

function CardList({robots}) {
	//essentially, we pass each robot object to the card component and make a card for each robot. We save this new array in card component
	const cardsArray = robots.map((user, i) => {
		return <Card key={i} 
					 id={robots[i].id} 
					 name={robots[i].name} 
					 email={robots[i].email}
					/> 


	})
	return (
		<div>
	    	{cardsArray}  {/* We display all the cards we created */}
	    </div>
		)
}

export default CardList