import { useState, useEffect } from 'react'
import { useAuth } from '@clerk/clerk-react'

export function ReservationsPage() {
  const { userId } = useAuth()
  const [reservations, setReservations] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // TODO: Fetch user reservations from API
    setLoading(false)
  }, [userId])

  if (loading) {
    return <div>Loading reservations...</div>
  }

  return (
    <div className="reservations-container">
      <h1>My Reservations</h1>
      
      <button className="btn btn-primary">Make New Reservation</button>
      
      {reservations.length === 0 ? (
        <p>You don't have any reservations.</p>
      ) : (
        <div className="reservations-list">
          {/* TODO: Display reservations */}
        </div>
      )}
    </div>
  )
}