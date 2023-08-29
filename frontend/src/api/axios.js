import axios from 'axios'
import { API_URL } from '../utils/utils'

export const HTTP = axios.create({
    baseURL:API_URL
})