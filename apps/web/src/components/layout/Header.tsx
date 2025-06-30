import { SignedIn, SignedOut, UserButton, SignInButton } from '@clerk/clerk-react'
import { Link } from 'react-router-dom'

export function Header() {
  return (
    <header className="header">
      <nav className="nav-container">
        <Link to="/" className="logo">
          Restaurant App
        </Link>
        
        <div className="nav-links">
          <Link to="/menu">Menu</Link>
          
          <SignedIn>
            <Link to="/orders">My Orders</Link>
            <Link to="/reservations">Reservations</Link>
            <UserButton afterSignOutUrl="/" />
          </SignedIn>
          
          <SignedOut>
            <SignInButton mode="modal">
              <button className="sign-in-btn">Sign In</button>
            </SignInButton>
          </SignedOut>
        </div>
      </nav>
    </header>
  )
}