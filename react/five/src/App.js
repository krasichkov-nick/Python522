
import './App.css';
import { useState } from 'react';
// import Counter from './Counter';
// import Person from './Person';
// import Modal from './Modal';
// import Item from './Item';
import Task from './Task';
import Form from './Form';

function App() {

  let [tasks, setTasks] = useState([
    {
      text: "Выучить JavaScript",
      done: false
    },
    {
      text: "Познакомиться с Реактом",
      done: false
    },
    {
      text: "Устоиться на работу",
      done: false
    }
  ])

  let addTask = text => {
    let newTask = [...tasks, {text}];
    setTasks(newTask);
  }

  let doneTask = index => {
    let newTask = [...tasks];
    newTask[index].done = true;
    setTasks(newTask);
  }

  let cancleTask = index => {
    let newTask = [...tasks];
    newTask[index].done = false;
    setTasks(newTask);
  }

  let deleteTask = index => {
    let newTask = [...tasks];
    newTask.splice(index, 1);
    setTasks(newTask);
  }

  let clearTasks = () => {
    let filteredTasks = tasks.filter(task => !task.done);
    setTasks(filteredTasks);
  }

  return (
    <div className="App">
      <div className="task-list">
        {/* <Counter />
      <Person /> */}
        {/* <Modal /> */}
        {/* <Item /> */}
        {
          tasks.map((task, index) =>
            <Task
              key={index}
              task={task}
              doneTask={doneTask}
              index={index}
              deleteTask={deleteTask}
              cancleTask={cancleTask}
            />
          )
        }
        <Form addTask={addTask}/></div>
        <button onClick={clearTasks}>Удалить все выполненные задачи</button>
    </div>
  );
}

export default App;
