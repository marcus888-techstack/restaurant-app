# Restaurant App - Project Overview

## 🏗️ System Architecture

```mermaid
graph TB
    subgraph "Frontend (React + Vite)"
        A[Landing Page] --> B[Menu Browser]
        A --> C[Admin Dashboard]
        B --> D[Shopping Cart]
        D --> E[Checkout]
    end
    
    subgraph "Backend (FastAPI)"
        F[API Gateway] --> G[Order Service]
        F --> H[Menu Service]
        F --> I[Reservation Service]
        F --> J[User Service]
    end
    
    subgraph "Database"
        K[(PostgreSQL)]
    end
    
    subgraph "External Services"
        L[Stripe Payment]
        M[Clerk Auth]
        N[Twilio SMS]
        O[SendGrid Email]
    end
    
    A --> F
    C --> F
    G --> K
    H --> K
    I --> K
    J --> K
    E --> L
    F --> M
    F --> N
    F --> O
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
- **Frontend**: React 18, Vite, Tailwind, shadcn/ui
- **Backend**: FastAPI, Prisma, PostgreSQL
- **Auth**: Clerk
- **Payments**: Stripe
- **Notifications**: Twilio (SMS), SendGrid (Email)