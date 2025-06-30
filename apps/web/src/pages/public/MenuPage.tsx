import { useState, useEffect } from 'react'
import { SignedIn, SignedOut, SignInButton } from '@clerk/clerk-react'
import { useApi } from '../../utils/api'

interface MenuItem {
  id: string
  name: string
  description: string
  price: number
  category: string
  available: boolean
  image_url?: string
}

export function MenuPage() {
  const [menuItems, setMenuItems] = useState<MenuItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const api = useApi()

  useEffect(() => {
    async function fetchMenu() {
      try {
        const items = await api.getMenuItems()
        setMenuItems(items)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load menu')
      } finally {
        setLoading(false)
      }
    }

    fetchMenu()
  }, [])

  if (loading) {
    return <div>Loading menu...</div>
  }

  if (error) {
    return <div>Error: {error}</div>
  }

  return (
    <div className="menu-container">
      <h1>Our Menu</h1>
      
      <div className="menu-grid">
        {menuItems.length === 0 ? (
          <p>No menu items available</p>
        ) : (
          menuItems.map(item => (
            <div key={item.id} className="menu-item">
              <h3>{item.name}</h3>
              <p>{item.description}</p>
              <p className="price">${item.price.toFixed(2)}</p>
              {!item.available && <span className="unavailable">Currently unavailable</span>}
            </div>
          ))
        )}
      </div>
      
      <SignedIn>
        <div className="order-actions">
          <button className="btn btn-primary">View Cart</button>
        </div>
      </SignedIn>
      
      <SignedOut>
        <div className="sign-in-prompt">
          <p>Sign in to place an order</p>
          <SignInButton mode="modal">
            <button className="btn btn-primary">Sign In</button>
          </SignInButton>
        </div>
      </SignedOut>
    </div>
  )
}