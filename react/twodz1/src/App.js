import Header from './Header';
import './App.css';
import Nav from './Nav';
import Footer from './Footer';

function App(props) {

  let {navigation, title, slogan, copy} = props;

  return (
    <div className="App">
      <Header title = {title} slogan = {slogan} />
      <Nav navigation = {navigation} />
      <Footer text = {copy} />
    </div>
  );
}

export default App;
