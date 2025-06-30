# Restaurant Admin Dashboard

## 🏗️ Admin Architecture

```mermaid
graph TB
    A[Admin Dashboard] --> B[Dashboard Overview]
    A --> C[Menu Management]
    A --> D[Order Processing]
    A --> E[Reservations]
    A --> F[Customers]
    A --> G[Analytics]
    A --> H[Settings]
    
    B --> I[Sales Metrics]
    B --> J[Recent Orders]
    B --> K[Quick Actions]
    
    C --> L[Menu Items CRUD]
    C --> M[Categories]
    C --> N[Pricing]
    
    D --> O[Order Queue]
    D --> P[Kitchen Display]
    D --> Q[Status Updates]
    
    E --> R[Calendar View]
    E --> S[Table Management]
    E --> T[Booking Confirmation]
```

## 🎛️ Dashboard Components

### Overview Dashboard
```mermaid
graph LR
    A[Today's Revenue] --> E[Dashboard]
    B[Active Orders] --> E
    C[Pending Reservations] --> E
    D[New Customers] --> E
    
    E --> F[Sales Chart]
    E --> G[Order Status Pie]
    E --> H[Peak Hours Graph]
```

### Order Management Flow
```mermaid
stateDiagram-v2
    [*] --> NewOrder
    NewOrder --> Confirmed : Admin confirms
    Confirmed --> Preparing : Start cooking
    Preparing --> Ready : Complete order
    Ready --> Delivered : Mark delivered
    Ready --> PickedUp : Customer pickup
    Delivered --> [*]
    PickedUp --> [*]
    
    NewOrder --> Cancelled : Cancel order
    Confirmed --> Cancelled : Cancel order
    Cancelled --> [*]
```

### Menu Management
```mermaid
flowchart TD
    A[Menu Management] --> B[Add Item]
    A --> C[Edit Item]
    A --> D[Delete Item]
    A --> E[Bulk Operations]
    
    B --> F[Item Details]
    B --> G[Image Upload]
    B --> H[Pricing]
    B --> I[Availability]
    
    E --> J[Price Updates]
    E --> K[Availability Toggle]
    E --> L[Category Changes]
```

## Key Admin Features
- **Real-time Dashboard**: Live metrics and order updates
- **Order Processing**: Kitchen display and status management
- **Menu Management**: Complete CRUD for menu items
- **Reservation Calendar**: Table booking management
- **Customer Analytics**: Insights and behavior tracking
- **Sales Reports**: Revenue and performance analysis
- **Settings**: Restaurant configuration and preferences