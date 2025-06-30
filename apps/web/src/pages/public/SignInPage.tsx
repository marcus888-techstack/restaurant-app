import { SignIn } from '@clerk/clerk-react'

export function SignInPage() {
  return (
    <div className="auth-container">
      <SignIn 
        path="/sign-in" 
        routing="path" 
        signUpUrl="/sign-up"
        afterSignInUrl="/menu"
      />
    </div>
  )
}