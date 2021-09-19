import axios from "axios";


const api = axios.create({
    headers: {
        'Content-Type': 'application/json;charset=UTF-8'
    }
})

export {api}