import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 5000,
})

export default {
  getInternships() {
    return apiClient.get('/internships/')
  },
  getInternship(id) {
    return apiClient.get(`/internships/${id}/`)
  },
}
