import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'

// Layout
import { Header } from './components/layout/Header'

// Public pages
import { HomePage } from './pages/public/HomePage'
import { MenuPage } from './pages/public/MenuPage'
import { SignInPage } from './pages/public/SignInPage'
import { SignUpPage } from './pages/public/SignUpPage'

// Protected pages
import { OrdersPage } from './pages/customer/OrdersPage'
import { ReservationsPage } from './pages/customer/ReservationsPage'

// Auth
import { ProtectedRoute } from './components/auth/ProtectedRoute'

function App() {
  return (
    <Router>
      <div className="app">
        <Header />
        <main className="main-content">
          <Routes>
            {/* Public Routes */}
            <Route path="/" element={<HomePage />} />
            <Route path="/menu" element={<MenuPage />} />
            <Route path="/sign-in" element={<SignInPage />} />
            <Route path="/sign-up" element={<SignUpPage />} />
            
            {/* Protected Customer Routes */}
            <Route path="/orders" element={
              <ProtectedRoute>
                <OrdersPage />
              </ProtectedRoute>
            } />
            <Route path="/reservations" element={
              <ProtectedRoute>
                <ReservationsPage />
              </ProtectedRoute>
            } />
            
            {/* TODO: Add admin routes */}
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App
