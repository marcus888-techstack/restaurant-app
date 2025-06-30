# Restaurant Database Schema

## 🗄️ Database Structure

```mermaid
erDiagram
    User ||--o{ Order : places
    User ||--o{ Reservation : makes
    User ||--o{ Review : writes
    User ||--o{ Address : has
    
    Order ||--o{ OrderItem : contains
    Order ||--o| Payment : has
    
    MenuItem ||--o{ OrderItem : "ordered as"
    MenuItem ||--o{ MenuItemVariant : has
    MenuItem ||--o{ Review : receives
    
    Category ||--o{ MenuItem : contains
    
    Reservation ||--o| Table : assigned
    
    User {
        string id PK
        string clerkId UK
        string email UK
        string name
        string phone
        enum role
        datetime createdAt
    }
    
    Order {
        string id PK
        string userId FK
        string orderNumber UK
        decimal subtotal
        decimal tax
        decimal total
        enum status
        enum type
        datetime createdAt
    }
    
    MenuItem {
        string id PK
        string categoryId FK
        string name
        string description
        decimal price
        boolean available
        string imageUrl
        json nutritionInfo
    }
    
    Category {
        string id PK
        string name
        string description
        integer sortOrder
        boolean active
    }
    
    Reservation {
        string id PK
        string userId FK
        string tableId FK
        datetime reservationTime
        integer partySize
        enum status
        datetime createdAt
    }
```

## 🔑 Key Tables

### Core Entities
- **User**: Customer & admin accounts (Clerk integration)
- **Order**: Food orders with status tracking
- **MenuItem**: Menu catalog with variants
- **Category**: Menu organization
- **Reservation**: Table booking system

### Supporting Tables
- **OrderItem**: Individual order line items
- **Payment**: Payment processing records
- **Address**: Customer delivery addresses
- **Review**: Customer feedback system
- **Table**: Restaurant table management

## 📈 Relationships
- One user can have many orders and reservations
- Orders contain multiple order items
- Menu items belong to categories
- Reservations are assigned to tables
- Users can review menu items