import React from "react";
import './Footer.css'

class Footer extends React.Component {
    render() {
        let { text } = this.props;
        return (
            <footer>
                <p>{text}</p>
            </footer>
        )
    }
}

export default Footer;