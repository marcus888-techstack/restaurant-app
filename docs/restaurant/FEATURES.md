# Restaurant Features Overview

## 🍽️ Customer Features

```mermaid
flowchart TD
    A[Landing Page] --> B[Menu Browser]
    B --> C[Add to Cart]
    C --> D[Checkout]
    D --> E[Order Tracking]
    
    A --> F[Table Reservation]
    F --> G[Date/Time Selection]
    G --> H[Confirmation]
    
    A --> I[Takeaway Orders]
    I --> J[Pickup Scheduling]
    
    A --> K[Catering Requests]
    K --> L[Event Details]
    
    A --> M[Food Planner]
    M --> N[Meal Planning]
    N --> O[Nutrition Tracking]
```

## 👨‍💼 Admin Features

```mermaid
flowchart TD
    A[Admin Dashboard] --> B[Menu Management]
    B --> C[Add/Edit Items]
    B --> D[Categories]
    B --> E[Pricing]
    
    A --> F[Order Processing]
    F --> G[Kitchen Display]
    F --> H[Status Updates]
    
    A --> I[Reservations]
    I --> J[Calendar View]
    I --> K[Table Management]
    
    A --> L[Analytics]
    L --> M[Sales Reports]
    L --> N[Customer Insights]
    
    A --> O[Settings]
    O --> P[Restaurant Info]
    O --> Q[Payment Config]
```

## 🔄 User Journey

```mermaid
journey
    title Customer Ordering Experience
    section Discovery
        Browse Menu: 5: Customer
        Filter Items: 4: Customer
        View Details: 4: Customer
    section Ordering
        Add to Cart: 5: Customer
        Customize Items: 4: Customer
        Review Cart: 4: Customer
        Checkout: 3: Customer
    section Fulfillment
        Receive Confirmation: 5: Customer
        Track Order: 4: Customer
        Receive Order: 5: Customer
        Leave Review: 3: Customer
```

## Key Features
- **Online Ordering**: Full e-commerce cart with customization
- **Table Reservations**: Real-time availability checking
- **Takeaway**: Scheduled pickup with time slots
- **Catering**: Event planning and custom quotes
- **Food Planner**: Meal planning with nutrition data
- **Admin Dashboard**: Complete restaurant management
- **Analytics**: Sales, customers, and performance insights