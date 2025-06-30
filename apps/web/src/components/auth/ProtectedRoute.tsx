import { useAuth } from '@clerk/clerk-react'
import { Navigate } from 'react-router-dom'
import { ReactNode } from 'react'

interface ProtectedRouteProps {
  children: ReactNode
  allowedRoles?: string[]
}

export function ProtectedRoute({ children, allowedRoles }: ProtectedRouteProps) {
  const { isLoaded, isSignedIn, userId } = useAuth()

  if (!isLoaded) {
    return <div>Loading...</div>
  }

  if (!isSignedIn) {
    return <Navigate to="/sign-in" replace />
  }

  // TODO: Add role checking when backend is ready
  // For now, just check if user is signed in
  if (allowedRoles && allowedRoles.length > 0) {
    // Role checking will be implemented after backend setup
  }

  return <>{children}</>
}