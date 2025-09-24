import logo from './i.jpeg'
import alb1 from './alb1.jpg'
import alb2 from './alb2.jpeg'
import alb3 from './alb3.jpeg'
import alb4 from './alb4.jpg'
import './Header.css'

function Header(props) {
    let { title, slogan } = props;

    return (
        <header className="App-header">
            <img src={logo} className="logo" alt="logo" />
            <h1>{title}</h1>
            <p>
                {slogan}
            </p>
            <p>
                <a href="https://ok.ru/music/album/122946300621619"><img src={alb1} alt="" className="albom" /></a>
                <img src={alb2} alt="" className="albom" />
                <img src={alb3} alt="" className="albom" />
                <img src={alb4} alt="" className="albom" />
            </p>
        </header>
    )
}

export default Header;