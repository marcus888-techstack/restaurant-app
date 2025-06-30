# Restaurant App - Project Overview

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph "Landing Site (React + Vite)"
        A[Marketing Page] --> B[Menu Preview]
        A --> C[Features Showcase]
        A --> D[App Signup CTA]
    end
    
    subgraph "Restaurant Web App (React + Vite)"
        E[Menu Browser] --> F[Shopping Cart]
        F --> G[Checkout]
        E --> H[Admin Dashboard]
        E --> I[Table Reservations]
    end
    
    subgraph "Backend (FastAPI)"
        J[API Gateway] --> K[Order Service]
        J --> L[Menu Service]
        J --> M[Reservation Service]
        J --> N[User Service]
    end
    
    subgraph "Database"
        O[(PostgreSQL)]
    end
    
    subgraph "External Services"
        P[Stripe Payment]
        Q[Clerk Auth]
        R[Twilio SMS]
        S[SendGrid Email]
    end
    
    A --> J
    E --> J
    K --> O
    L --> O
    M --> O
    N --> O
    G --> P
    J --> Q
    J --> R
    J --> S
```

## 🍽️ Core Features

```mermaid
mindmap
  root((Restaurant App))
    Customer Features
      Menu Browsing
      Online Ordering
      Table Reservations
      Takeaway Orders
      Food Planner
      Order Tracking
    Admin Features
      Menu Management
      Order Processing
      Reservation Calendar
      Customer Analytics
      Sales Reports
      Settings
```

## 🔄 Order Flow

```mermaid
sequenceDiagram
    participant C as Customer
    participant W as Web App
    participant A as API
    participant D as Database
    participant S as Stripe
    participant K as Kitchen
    
    C->>W: Browse Menu
    W->>A: Get Menu Items
    A->>D: Query Menu
    D-->>A: Return Items
    A-->>W: Menu Data
    W-->>C: Display Menu
    
    C->>W: Add to Cart
    C->>W: Checkout
    W->>S: Process Payment
    S-->>W: Payment Success
    W->>A: Create Order
    A->>D: Save Order
    A-->>K: Notify Kitchen
    A-->>C: Order Confirmation
```

## 🗄️ Data Model

```mermaid
erDiagram
    User ||--o{ Order : places
    User ||--o{ Reservation : makes
    Order ||--o{ OrderItem : contains
    MenuItem ||--o{ OrderItem : "ordered as"
    Category ||--o{ MenuItem : contains
    Order ||--o| Review : "can have"
    
    User {
        string id PK
        string email
        string name
        string role
    }
    
    Order {
        string id PK
        string userId FK
        decimal total
        string status
        datetime createdAt
    }
    
    MenuItem {
        string id PK
        string categoryId FK
        string name
        decimal price
        boolean available
    }
```

## 🚀 Deployment

```mermaid
flowchart LR
    subgraph "Development"
        A[Local Dev]
        B[Docker Compose]
    end
    
    subgraph "Production"
        C[Vercel Frontend]
        D[Railway Backend]
        E[PlanetScale DB]
        F[Cloudflare CDN]
    end
    
    A --> B
    B --> C
    B --> D
    D --> E
    C --> F
```

## Tech Stack
- **Landing Site**: React 18, Vite, Tailwind (apps/landing/)
- **Restaurant App**: React 18, Vite, Tailwind, shadcn/ui (apps/web/)
- **Backend**: FastAPI, Prisma, PostgreSQL (apps/backend/)
- **Auth**: Clerk
- **Payments**: Stripe
- **Notifications**: Twilio (SMS), SendGrid (Email)