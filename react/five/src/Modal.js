import { useState } from "react";
import './Modal.css';

function Modal() {

    let [open, setOpen] = useState(false);

    let image ="https://avatars.mds.yandex.net/i?id=8cec839a5e4da25a9e16a26c3271994bdd34aacc-5657257-images-thumbs&n=13"

    return (
        <div>
            <img src={image} className="small" alt="" onClick={() => setOpen(true)} style={{display: open ? "none" : "block"}} />

            {open && (<div>
                <div>
                    <img src={image} className="big" alt="" onClick={() => setOpen(false)} />
                </div>
            </div>)}
            
        </div>
    )
}

export default Modal;