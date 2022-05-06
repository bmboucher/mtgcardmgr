import React, { Component } from 'react';

class CardEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            text: 'HELLO'
        };
    }

    onKeyDown = (event) => {
        console.log(event);
        if (/Key[A-Z]/.test(event.code)) {
            this.setState({dfopjktext: this.state.text + event.key})
        }
    };

    render() {
        const {text} = this.state;
        return <div>
        <input onKeyDown={this.onKeyDown} tabIndex={0} readOnly={true} value={text}></input>
        </div>
    }
}

export default CardEntry;