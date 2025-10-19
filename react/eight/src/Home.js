import './Home.css';
import { useState } from 'react';

function Home() {
  const items = ['Мама', 'Папа', 'Я', 'Дружная', 'Семья'];

  // Состояние: массив флагов для каждого элемента
  const [isSelected, setIsSelected] = useState(
    new Array(items.length).fill(false)
  );

  // Новое состояние: счётчик выбранных элементов
  const [selectedCount, setSelectedCount] = useState(0);

  // Обработчик изменения чекбокса
  const handleCheckboxChange = (index) => {
    setIsSelected((prev) => {
      const newState = [...prev];
      newState[index] = !newState[index]; // Инвертируем состояние

      // Обновляем счётчик: считаем количество true в массиве
      const newCount = newState.filter(Boolean).length;
      setSelectedCount(newCount);

      return newState;
    });
  };

  return (
    <div className="home-page">
      <h2>Home Page</h2>
      <div className="shopping-list">
        <h3>Shopping list:</h3>    
        <li>
          {items.map((item, index) => (
            <li key={index}>
              <label>
                <input
                  type="checkbox"
                  checked={isSelected[index]}
                  onChange={() => handleCheckboxChange(index)}
                />
                {item}
              </label>
              <span className="status-symbol">
                {isSelected[index] ? '+' : '-'}
              </span>
            </li>
          ))}
        </li>
        <p className="selected-count">
          Together we are a force: <strong>{selectedCount}</strong> from {items.length}
        </p>
      </div>
    </div>
  );
}

export default Home;
