import {useStore} from 'vuex'

export const API_URL = "http://127.0.0.1:8000"

export const isAuthenticated = () => {
    if (useStore().state.user.token){
        return true
    }
    else{
        return false
    }
}

export const handleInput = (data,e) => {
    data[e.target.name] = e.target.value
}
