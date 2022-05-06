import React, { Component } from 'react';
import { get } from 'axios';

class CardSelect extends Component {
    constructor(props) {
        super(props);
        this.state = {cards: []};
    }
    
    componentDidMount() {
        get('/cards/').then(res => this.setState({cards: res.data.cards}))
    }

    render() {
        const {cards} = this.state;
        return <div><select>
            {cards.map(card => 
                <option value={card.uuid} label={card.name} key={card.uuid}/>)}
        </select></div>;
    }
}

export default CardSelect;