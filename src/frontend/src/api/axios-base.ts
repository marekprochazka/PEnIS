import axios from "axios";
import {getCsrf} from "@/utils/getCsrf";

const api = axios.create({
    headers: {
        'Content-Type': 'application/json;charset=UTF-8',

    }
})

const csrfHeader = () => {
    return {
        headers: {
            'X-CSRFToken': getCsrf()
        }
    }
}

export {api, csrfHeader}