import { SignUp } from '@clerk/clerk-react'

export function SignUpPage() {
  return (
    <div className="auth-container">
      <SignUp 
        path="/sign-up" 
        routing="path" 
        signInUrl="/sign-in"
        afterSignUpUrl="/menu"
      />
    </div>
  )
}