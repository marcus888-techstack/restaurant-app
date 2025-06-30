# Restaurant API Documentation

## 🌐 API Structure

```mermaid
graph TD
    A[API Gateway] --> B[Public Routes]
    A --> C[Auth Routes]
    A --> D[Customer Routes]
    A --> E[Admin Routes]
    
    B --> F[Menu Items]
    B --> G[Categories]
    B --> H[Restaurant Info]
    
    C --> I[Login/Register]
    C --> J[Token Refresh]
    
    D --> K[Orders]
    D --> L[Reservations]
    D --> M[Profile]
    D --> N[Reviews]
    
    E --> O[Menu Management]
    E --> P[Order Processing]
    E --> Q[Analytics]
    E --> R[Settings]
```

## 🔒 Authentication

```mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant K as Clerk
    
    C->>A: Request with JWT
    A->>K: Verify Token
    K-->>A: User Info
    A-->>C: Authorized Response
```

## 📍 Key Endpoints

### Public Routes
- `GET /menu` - Get menu items
- `GET /categories` - Get categories
- `GET /restaurant/info` - Restaurant details

### Customer Routes
- `POST /orders` - Place order
- `GET /orders` - Order history
- `POST /reservations` - Book table
- `GET /reservations` - View bookings

### Admin Routes
- `POST /admin/menu-items` - Add menu item
- `PUT /admin/orders/{id}/status` - Update order status
- `GET /admin/analytics` - Sales data
- `PUT /admin/settings` - Update settings

## 🔄 Order Status Flow

```mermaid
stateDiagram-v2
    [*] --> PENDING
    PENDING --> CONFIRMED
    CONFIRMED --> PREPARING
    PREPARING --> READY
    READY --> DELIVERED
    READY --> PICKED_UP
    PENDING --> CANCELLED
    CONFIRMED --> CANCELLED
    DELIVERED --> [*]
    PICKED_UP --> [*]
    CANCELLED --> [*]
```

## Response Format
```json
{
  "success": true,
  "data": {},
  "message": "Operation completed",
  "timestamp": "2024-01-01T00:00:00Z"
}
```