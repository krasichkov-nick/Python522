function Task (props){
    let {task, doneTask, index, deleteTask, cancleTask} = props;

    return(
        <div className="task" style={{textDecoration: task.done ? 'line-through' : '', background: task.done ? '#e0f7fa' : ''}}>
            {task.text}
            <div>
                <button onClick={() => doneTask(index)} style={{
                        backgroundColor: task.done ? '#4caf50' : '#f5f5f5'
                    }}>Done</button>
                <button onClick={() => cancleTask(index)}>Cancel</button>
                <button onClick={() => deleteTask(index)} >X</button>
            </div>
        </div>
    )
}

export default Task;