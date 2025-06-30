import { useState, useEffect } from 'react'
import { useAuth } from '@clerk/clerk-react'
import { useApi } from '../../utils/api'
import { Link } from 'react-router-dom'

interface Order {
  id: string
  user_id: string
  items: Array<{
    menu_item_id: string
    quantity: number
    notes?: string
  }>
  total: number
  status: string
  created_at: string
  updated_at: string
  is_takeaway: boolean
  notes?: string
}

export function OrdersPage() {
  const { userId } = useAuth()
  const [orders, setOrders] = useState<Order[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const api = useApi()

  useEffect(() => {
    async function fetchOrders() {
      try {
        const userOrders = await api.getOrders()
        setOrders(userOrders)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load orders')
      } finally {
        setLoading(false)
      }
    }

    if (userId) {
      fetchOrders()
    }
  }, [userId])

  if (loading) {
    return <div>Loading orders...</div>
  }

  if (error) {
    return <div>Error: {error}</div>
  }

  return (
    <div className="orders-container">
      <h1>My Orders</h1>
      
      {orders.length === 0 ? (
        <div>
          <p>You haven't placed any orders yet.</p>
          <Link to="/menu" className="btn btn-primary">Browse Menu</Link>
        </div>
      ) : (
        <div className="orders-list">
          {orders.map(order => (
            <div key={order.id} className="order-item">
              <div className="order-header">
                <h3>Order #{order.id}</h3>
                <span className={`status status-${order.status}`}>{order.status}</span>
              </div>
              <p>Total: ${order.total.toFixed(2)}</p>
              <p>{order.items.length} items</p>
              <p>Placed on: {new Date(order.created_at).toLocaleDateString()}</p>
              {order.is_takeaway && <span className="takeaway">Takeaway</span>}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}