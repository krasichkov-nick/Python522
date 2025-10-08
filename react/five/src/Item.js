import { useState } from "react";



function Item (){

    let [item, setItem] = useState([]);

    function addItem(){
        setItem([...item,
            Math.floor(Math.random() * 10) + 1
        ])
            
            
    }

    return(
        <div>
            <button onClick={addItem}>Add a number</button>
            <div>
                {
                item.map((i, index)=>(
                    <div 
                        key={index}
                        style={{
                           background: index % 2 ? "grey" : "yellow"
                        }}
                    >{i}</div>
                ))
                }
            </div>
            
        </div>
    )
}

export default Item;