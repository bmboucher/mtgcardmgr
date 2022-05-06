import React, { Component } from 'react';
import { get } from 'axios';

class CardEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            setCode: null,
            number: null,
            options: []
        };
    }

    onKeyDown = (event) => {
        console.log(event);
        let {setCode, number} = this.state;
        if (/Key[A-Z]/.test(event.code) && (!setCode || setCode.length < 3)) {
            setCode = setCode || '';
            setCode += event.key.toUpperCase();
            this.setState({setCode});
        } else if (/Digit[0-9]/.test(event.code) && (!number || number.length < 3)) {
            number = number || '';
            number += event.key;
            this.setState({number});
        } else if (event.code == 'Backspace') {
            setCode = null;
            number = null;
            this.setState({setCode, number});
        } else {
            return;
        }
        let queryParams = {};
        if (setCode) {
            queryParams.set = setCode.length < 3 ? setCode + '*' : setCode;
        }
        if (number) {
            queryParams.number = number.length < 3 ? number + '*' : number;
        }
        const queryStr=Object.entries(queryParams).map(([key, value]) => `${key}=${value}`).join('&');
        get(`/cards/?${queryStr}`).then(res => this.setState({options: res.data.cards}));
    };

    render() {
        const {setCode, number, options} = this.state;
        const text = `${setCode}/${number}`
        let img = undefined;
        if (options.length > 0) {
            const scryfallId = options[0].scryfallId;
            const img_url = `https://c1.scryfall.com/file/scryfall-cards/large/front/${scryfallId[0]}/${scryfallId[1]}/${scryfallId}.jpg`
            img = <img src={img_url} alt={options[0].name} style={{height: '500px'}}/>
        }

        return <div>
        <input onKeyDown={this.onKeyDown} tabIndex={0} readOnly={true} value={text}></input>
        <ul>
            {options.map(opt => <li key={opt.uuid}>{opt.name}</li>)}
        </ul>
        {img}
        </div>
    }
}

export default CardEntry;