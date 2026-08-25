import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Auth API calls
export const authAPI = {
  register: (username, email, password, fullName) =>
    api.post('/auth/register', { username, email, password, full_name: fullName }),
  login: (username, password) =>
    api.post('/auth/login', { username, password }),
  logout: () =>
    api.post('/auth/logout'),
};

// Tickets API calls
export const ticketsAPI = {
  getAll: (filters = {}) =>
    api.get('/tickets', { params: filters }),
  getById: (id) =>
    api.get(`/tickets/${id}`),
  create: (title, description, priority = 'medium') =>
    api.post('/tickets', { title, description, priority }),
  update: (id, data) =>
    api.put(`/tickets/${id}`, data),
  delete: (id) =>
    api.delete(`/tickets/${id}`),
};

// Users API calls
export const usersAPI = {
  getAll: () =>
    api.get('/users'),
  getById: (id) =>
    api.get(`/users/${id}`),
  getProfile: () =>
    api.get('/users/profile'),
};

export default api;
