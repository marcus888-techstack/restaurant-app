import { Link } from 'react-router-dom'
import { SignedIn, SignedOut } from '@clerk/clerk-react'

export function HomePage() {
  return (
    <div className="home-container">
      <h1>Welcome to Our Restaurant</h1>
      <p>Experience the finest dining with our carefully crafted menu.</p>
      
      <div className="cta-buttons">
        <Link to="/menu" className="btn btn-primary">View Menu</Link>
        
        <SignedIn>
          <Link to="/reservations" className="btn btn-secondary">Make a Reservation</Link>
        </SignedIn>
        
        <SignedOut>
          <Link to="/sign-up" className="btn btn-secondary">Join Us</Link>
        </SignedOut>
      </div>
    </div>
  )
}