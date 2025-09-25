import React from "react";
import './Range.css';

class Range extends React.Component {
    state = { val: 120 }

    range = (event) => {
        this.setState({val: event.target.value})
    }

    render(){
        return(
            <>
                <br />
                <br />
                <br />
                <h3>Выберите размер квадрата</h3>
                <input type="range" onChange={this.range} min = "50" max = "240" value={this.state.val} />
                <p>{this.state.val}px * {this.state.val}px</p>
                <div 
                    className="square" 
                    style={{
                        width: `${this.state.val}px`,
                        height: `${this.state.val}px`
                    }}
                ></div>
            </>
        )
    }

}

export default Range;