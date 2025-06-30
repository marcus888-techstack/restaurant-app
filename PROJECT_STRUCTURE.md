# Restaurant App - Project Structure

## Overview
This restaurant management platform follows a modern two-app architecture pattern optimized for restaurant operations, with a separate marketing landing site and a main restaurant application that includes customer ordering and admin functionality.

```
restaurant-app/
│
├── apps/                          # Restaurant applications (monorepo structure)
│   ├── landing/                   # Marketing/Landing site (React + Vite)
│   │   ├── src/                  # Source code
│   │   │   ├── components/       # Landing page components
│   │   │   │   ├── Hero.tsx     # Hero section with restaurant branding
│   │   │   │   ├── Features.tsx # Restaurant features showcase
│   │   │   │   ├── MenuPreview.tsx # Sample menu preview
│   │   │   │   ├── Testimonials.tsx # Customer testimonials
│   │   │   │   └── CTA.tsx      # Call-to-action for app signup
│   │   │   ├── App.tsx          # Main app component
│   │   │   ├── main.tsx         # Entry point
│   │   │   └── index.css        # Global styles
│   │   ├── public/              # Static assets (restaurant images)
│   │   ├── index.html           # HTML template
│   │   ├── .env.example         # Environment variables template
│   │   ├── vite.config.ts       # Vite configuration
│   │   ├── package.json         # Dependencies
│   │   └── tsconfig.json        # TypeScript config
│   │
│   ├── web/                       # Main restaurant application (React + Vite)
│   │   ├── src/                  # Source code
│   │   │   ├── components/       # React components
│   │   │   │   ├── common/      # Shared UI components
│   │   │   │   ├── layout/      # App layout components
│   │   │   │   ├── menu/        # Menu browsing components
│   │   │   │   ├── cart/        # Shopping cart components
│   │   │   │   ├── order/       # Order management components
│   │   │   │   ├── reservation/ # Table reservation components
│   │   │   │   ├── customer/    # Customer profile components
│   │   │   │   └── admin/       # Admin dashboard components
│   │   │   ├── pages/           # Page components
│   │   │   │   ├── dashboard/   # Customer dashboard pages
│   │   │   │   ├── menu/        # Menu browsing pages
│   │   │   │   ├── order/       # Order management pages
│   │   │   │   ├── reservation/ # Table reservation pages
│   │   │   │   ├── customer/    # Customer profile pages
│   │   │   │   └── admin/       # Admin dashboard pages
│   │   │   │       ├── Dashboard.tsx      # Admin overview
│   │   │   │       ├── MenuManagement.tsx # Menu management
│   │   │   │       ├── OrderManagement.tsx # Order processing
│   │   │   │       ├── ReservationManagement.tsx # Reservation management
│   │   │   │       ├── CustomerManagement.tsx # Customer management
│   │   │   │       └── Analytics.tsx      # Sales analytics
│   │   │   ├── guards/          # Route protection
│   │   │   │   ├── AuthGuard.tsx    # Authentication guard
│   │   │   │   └── AdminGuard.tsx   # Admin role guard
│   │   │   ├── hooks/           # Custom hooks
│   │   │   ├── services/        # API services
│   │   │   ├── store/           # State management (Zustand)
│   │   │   ├── utils/           # Utilities
│   │   │   ├── types/           # TypeScript types
│   │   │   ├── App.tsx          # App root component
│   │   │   └── main.tsx         # Entry point
│   │   ├── public/              # Static assets
│   │   ├── .env.example         # Environment variables template
│   │   ├── .dockerignore        # Docker ignore patterns
│   │   ├── Dockerfile           # Production Docker configuration
│   │   ├── Dockerfile.dev       # Development Docker configuration
│   │   ├── package.json         # Dependencies
│   │   ├── tsconfig.json        # TypeScript config
│   │   └── vite.config.ts       # Vite configuration
│   │
│   └── backend/                   # FastAPI application
│       ├── app/                  # Application code
│       │   ├── api/             # API endpoints
│       │   │   └── v1/          # API version 1
│       │   │       ├── public/  # Public endpoints (menu, restaurant info)
│       │   │       ├── auth/    # Authentication endpoints
│       │   │       ├── menu/    # Menu management endpoints
│       │   │       ├── orders/  # Order processing endpoints
│       │   │       ├── reservations/ # Reservation endpoints
│       │   │       ├── customers/ # Customer management endpoints
│       │   │       └── admin/   # Admin-only endpoints
│       │   ├── core/            # Core configuration
│       │   ├── models/          # Pydantic models
│       │   ├── services/        # Business logic
│       │   ├── middleware/      # Middleware
│       │   └── utils/           # Utilities
│       ├── prisma/              # Database schema
│       │   └── schema.prisma    # Prisma schema
│       ├── scripts/             # Utility scripts
│       │   └── seed.py          # Database seeding
│       ├── tests/               # Test files
│       ├── .env.example         # Environment variables template
│       ├── .dockerignore        # Docker ignore patterns
│       ├── Dockerfile           # Production Docker configuration
│       ├── Dockerfile.dev       # Development Docker configuration
│       ├── main.py              # Application entry point
│       ├── requirements.txt     # Python dependencies
│       └── pyproject.toml       # Python project config
│
├── packages/                      # Shared packages (monorepo)
│   ├── ui/                       # Shared UI components
│   │   ├── src/
│   │   │   ├── components/      # Reusable components
│   │   │   ├── hooks/           # Shared hooks
│   │   │   └── styles/          # Shared styles
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   ├── utils/                    # Shared utilities
│   │   ├── src/
│   │   │   ├── formatters/      # Data formatters
│   │   │   ├── validators/      # Validation functions
│   │   │   └── helpers/         # Helper functions
│   │   ├── package.json
│   │   └── tsconfig.json
│   │
│   └── types/                    # Shared TypeScript types
│       ├── src/
│       │   ├── models/          # Data models
│       │   ├── api/             # API types
│       │   └── common/          # Common types
│       ├── package.json
│       └── tsconfig.json
│
├── docker/                        # Docker-related configurations
│   ├── nginx/                    # Nginx configuration
│   │   ├── nginx.conf           # Main Nginx configuration
│   │   └── conf.d/              # Site-specific configs
│   │       ├── landing.conf     # Landing site config
│   │       └── app.conf         # App + API config
│   ├── postgres/                # PostgreSQL configurations (if needed)
│   └── volumes/                 # Docker volumes (git-ignored)
│       ├── postgres/            # PostgreSQL data
│       ├── redis/               # Redis data
│       ├── pgadmin/             # pgAdmin configuration
│       └── uploads/             # File uploads
│
├── docs/                          # Project documentation
│   ├── restaurant/               # Restaurant-specific documentation
│   │   ├── PROJECT_OVERVIEW.md   # Architecture overview
│   │   ├── FEATURES.md           # Feature specifications
│   │   ├── RESTAURANT_DATABASE.md # Database schema
│   │   ├── RESTAURANT_API.md     # API documentation
│   │   ├── UI_COMPONENTS.md      # Component library
│   │   ├── ADMIN_FEATURES.md     # Admin dashboard guide
│   │   ├── IMPLEMENTATION_GUIDE.md # Step-by-step guide
│   │   └── QUICK_START.md        # Rapid setup guide
│   ├── API.md                    # General API documentation
│   ├── ARCHITECTURE.md           # System architecture and design
│   ├── DATABASE.md               # Database schema and ERD
│   ├── DEPLOYMENT.md             # Deployment guide
│   ├── SPECIFICATION.md          # Technical specifications
│   ├── UI-SPEC.md                # UI/UX design specifications
│   └── ADMIN_DASHBOARD.md        # Admin dashboard documentation
│
├── .env.example                   # Docker Compose environment template
├── .gitignore                     # Git ignore patterns
├── docker-compose.yml             # Main Docker Compose configuration
├── docker-compose.dev.yml         # Development overrides
├── docker-compose.prod.yml        # Production overrides
├── turbo.json                     # Turborepo configuration (optional)
├── pnpm-workspace.yaml           # PNPM workspace config (or npm/yarn)
├── PROJECT_STRUCTURE.md           # This file
└── README.md                      # Main project documentation
```

## Architecture Overview

### Two-App Restaurant Architecture
1. **Landing Site** (`restaurant.com`)
   - Marketing and conversion-focused
   - Restaurant branding and showcase
   - Menu preview and testimonials
   - Call-to-action for app signup
   - React + Vite for fast loading

2. **Restaurant Web Application** (`app.restaurant.com`)
   - Main restaurant ordering application
   - Menu browsing and online ordering
   - Table reservations and takeaway
   - Customer dashboard and order history
   - Admin dashboard integrated at `/admin`
   - React + Vite for fast development
   - Protected routes for authenticated users

### Shared Resources
- **Backend API**: Serves both landing and restaurant web app
- **Database**: Single PostgreSQL database for all restaurant data
- **External Services**: Stripe (payments), Clerk (auth), Twilio (SMS), SendGrid (email)

## Directory Purposes

### `/apps`
Contains all restaurant applications in a monorepo structure:
- **landing**: React + Vite marketing website for restaurant
- **web**: React + Vite main restaurant ordering application
- **backend**: FastAPI backend serving both applications

### `/packages`
Shared code between applications:
- **@[project]/ui**: Reusable UI components
- **@[project]/utils**: Common utilities
- **@[project]/types**: Shared TypeScript types

### `/docker`
All Docker-related configurations:
- **nginx/**: Reverse proxy with subdomain routing
- **volumes/**: Persistent data storage

### `/docs`
Comprehensive project documentation

## URL Structure

### Landing Site
```
restaurant.com/                  # Single-page restaurant landing
restaurant.com/#features         # Features section (anchor)
restaurant.com/#menu-preview     # Menu preview (anchor)
restaurant.com/#testimonials     # Customer testimonials (anchor)
restaurant.com/#contact          # Contact section (anchor)
```

### Restaurant Web Application
```
app.restaurant.com/              # Restaurant app dashboard
app.restaurant.com/login         # Authentication
app.restaurant.com/menu          # Menu browsing
app.restaurant.com/cart          # Shopping cart
app.restaurant.com/order         # Order management
app.restaurant.com/reservation   # Table reservations
app.restaurant.com/profile       # Customer profile
app.restaurant.com/order-history # Order history

# Admin Routes (protected)
app.restaurant.com/admin         # Admin dashboard
app.restaurant.com/admin/menu    # Menu management
app.restaurant.com/admin/orders  # Order processing
app.restaurant.com/admin/reservations # Reservation management
app.restaurant.com/admin/customers # Customer management
app.restaurant.com/admin/analytics # Sales analytics
```

### API Endpoints
```
app.[domain].com/api/v1/         # API base
app.[domain].com/api/docs        # API documentation
```

## Development Workflow

### Initial Setup
```bash
# Clone repository
git clone [repository-url]
cd [project-name]

# Install dependencies (using pnpm)
pnpm install

# Copy environment files
cp .env.example .env
cp apps/landing/.env.example apps/landing/.env.local
cp apps/web/.env.example apps/web/.env.local
cp apps/backend/.env.example apps/backend/.env
```

### Running Applications

#### Using Docker (Recommended)
```bash
# Build images
docker-compose build

# Start all services
docker-compose up -d

# Access applications
# Landing: http://localhost:3000
# Web App: http://localhost:5173
# Backend: http://localhost:5000
```

#### Manual Development
```bash
# Terminal 1 - Landing site
cd apps/landing
pnpm dev

# Terminal 2 - Web application
cd apps/web
pnpm dev

# Terminal 3 - Backend
cd apps/backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

# Terminal 4 - Database (if not using Docker)
docker run -p 5432:5432 -e POSTGRES_PASSWORD=password postgres:15
```

### Building for Production
```bash
# Build all applications
pnpm build

# Or build individually
cd apps/landing && pnpm build
cd apps/web && pnpm build
cd apps/backend && docker build -t [project]-backend .
```

## Deployment Strategy

### Landing Site
- Deploy to Vercel/Netlify (optimized for Next.js)
- Configure domain: `[domain].com`
- Enable CDN and edge caching

### Web Application
- Deploy to cloud provider (AWS/GCP/Azure)
- Configure subdomain: `app.[domain].com`
- Set up SSL certificates

### Backend API
- Deploy as containerized service
- Configure at: `app.[domain].com/api`
- Set up database and Redis

## Package Management

### Using Shared Packages
```typescript
// In apps/web/package.json
{
  "dependencies": {
    "@[project]/ui": "workspace:*",
    "@[project]/utils": "workspace:*",
    "@[project]/types": "workspace:*"
  }
}

// Usage in code
import { Button } from '@[project]/ui';
import { formatDate } from '@[project]/utils';
import { User } from '@[project]/types';
```

### Creating New Shared Components
```bash
# Add to UI package
cd packages/ui/src/components
# Create new component

# Build package
cd packages/ui
pnpm build

# Use in apps
pnpm install
```

## Benefits of This Structure

1. **Performance Optimization**
   - Landing site can be fully static/CDN-served
   - App bundle doesn't include marketing assets
   - Separate optimization strategies

2. **Development Efficiency**
   - Clear separation of concerns
   - Shared code through packages
   - Independent deployment cycles

3. **Scalability**
   - Easy to extract admin to separate app later
   - Can add more apps as needed
   - Natural microservices evolution path

4. **SEO & Marketing**
   - Landing site optimized for search engines
   - Fast page loads for better conversion
   - A/B testing without affecting app

5. **Security**
   - App code not exposed to public visitors
   - Separate authentication boundaries
   - Admin routes additionally protected