import { useAuth } from '@clerk/clerk-react'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5001'
const API_PREFIX = '/api/v1'

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message)
    this.name = 'ApiError'
  }
}

async function fetchWithAuth(url: string, options: RequestInit = {}, token?: string) {
  const headers = {
    'Content-Type': 'application/json',
    ...options.headers,
  }

  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }

  const response = await fetch(url, {
    ...options,
    headers,
  })

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Unknown error' }))
    throw new ApiError(response.status, error.detail || 'Request failed')
  }

  return response.json()
}

export function useApi() {
  const { getToken } = useAuth()

  const api = {
    // Auth endpoints
    async getCurrentUser() {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/auth/me`, {}, token)
    },

    async verifyToken() {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/auth/verify`, {}, token)
    },

    // Menu endpoints (public)
    async getMenuItems(category?: string) {
      const params = new URLSearchParams()
      if (category) params.append('category', category)
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/menu/items?${params}`)
    },

    async getMenuItem(itemId: string) {
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/menu/items/${itemId}`)
    },

    async getCategories() {
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/menu/categories`)
    },

    // Order endpoints (protected)
    async getOrders() {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/orders`, {}, token)
    },

    async getOrder(orderId: string) {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/orders/${orderId}`, {}, token)
    },

    async createOrder(orderData: any) {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/orders`, {
        method: 'POST',
        body: JSON.stringify(orderData),
      }, token)
    },

    async cancelOrder(orderId: string) {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/orders/${orderId}/cancel`, {
        method: 'POST',
      }, token)
    },

    // Admin endpoints
    async createMenuItem(itemData: any) {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/menu/items`, {
        method: 'POST',
        body: JSON.stringify(itemData),
      }, token)
    },

    async updateMenuItem(itemId: string, itemData: any) {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/menu/items/${itemId}`, {
        method: 'PUT',
        body: JSON.stringify(itemData),
      }, token)
    },

    async deleteMenuItem(itemId: string) {
      const token = await getToken()
      return fetchWithAuth(`${API_BASE_URL}${API_PREFIX}/menu/items/${itemId}`, {
        method: 'DELETE',
      }, token)
    },
  }

  return api
}