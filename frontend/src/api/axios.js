import axios from 'axios'
import { API_URL } from '../utils/utils'

export const HTTP = axios.create({
    baseURL:API_URL
})

export const REQUIRE_AUTH_HTTP = (token) => { return axios.create({
    baseURL:API_URL,
    headers:{
        Authorization: `TOKEN ${token}`
    }
})}