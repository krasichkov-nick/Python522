import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

let nav = {"Новости": "/news", "Афиша": "/afisha", "Группа": "/group", "Релизы": "/relise", "Магазин": "/market", "Галерея": "/galery", "Медиа": "/media", "Пресса": "/press", "Контакты": "/contacts"};
let slogan = "Дискография"
let text = "Песни группы Князь"
let copy = "Copyright - 2025. Здесь могла бы быть Ваша реклама :)"

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App navigation = {nav} slogan = {slogan} title = {text} copy = {copy}/>
  </React.StrictMode>
);
