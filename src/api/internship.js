import apiClient from './axios'

export const fetchInternships = () => {
  return apiClient.get('/internships')
}

export const createInternship = (data) => {
  return apiClient.post('/internships', data)
}
