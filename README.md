# 🍽️ Restaurant Management Platform

A modern, full-featured restaurant application with integrated ordering system, table reservations, and admin dashboard. Built with React, FastAPI, TypeScript, Prisma, and PostgreSQL.

![Restaurant App Preview](./docs/images/restaurant-preview.png)

## 🚀 Features

### Restaurant Operations
- **Customer Landing Page** (`restaurant.com`): Menu browsing, ordering, and reservations
- **Integrated Admin Dashboard** (`restaurant.com/admin`): Complete restaurant management
- **Unified Backend**: FastAPI serving both customer and admin features
- **Mobile-First Design**: Optimized for mobile ordering experience

### Core Restaurant Features
- **Online Food Ordering**: Complete cart, checkout, and order tracking system
- **Table Reservations**: Real-time availability and booking management
- **Takeaway Orders**: Scheduled pickup with time slot selection
- **Catering Services**: Event catering requests and management
- **Food Planner**: Meal planning with nutritional tracking
- **Menu Management**: Dynamic menu with categories, variants, and add-ons
- **Order Processing**: Real-time kitchen display and order tracking
- **Customer Management**: Profiles, order history, and loyalty program
- **Analytics Dashboard**: Sales reports, popular items, and performance metrics
- **Payment Processing**: Multiple payment methods with Stripe integration

## 📋 Prerequisites

- Node.js 18+ and npm/yarn/pnpm (for frontend)
- Python 3.11+ (for backend)
- Docker and Docker Compose (for database)
- Git

## 🛠️ Tech Stack

### Restaurant Frontend (React + Vite)
- **React 18** - UI library with TypeScript
- **Vite** - Lightning-fast build tool and dev server
- **shadcn/ui** - Accessible and customizable component library
- **Tailwind CSS** - Utility-first CSS framework
- **React Router v6** - Client-side routing for SPA
- **Clerk React** - Authentication UI components
- **Framer Motion** - Smooth animations and transitions
- **React Hook Form + Zod** - Form handling and validation
- **TanStack Query** - Data fetching, caching, and synchronization
- **Zustand** - State management for cart and user data
- **Axios** - HTTP client for API communication

### Restaurant Backend (FastAPI)
- **FastAPI** - High-performance Python web framework
- **Pydantic** - Data validation and settings management
- **Prisma** - Type-safe database ORM (Python client)
- **PostgreSQL** - Relational database for restaurant data
- **Python-Jose[cryptography]** - JWT token verification
- **HTTPX** - HTTP client for external API integration
- **Python-Multipart** - File uploads for menu images
- **Pillow** - Image processing and optimization
- **Uvicorn** - ASGI server for production
- **Python-dotenv** - Environment variables management
- **WebSockets** - Real-time order updates and notifications

### Payment & External Services
- **Stripe** - Payment processing for orders
- **Twilio** - SMS notifications for order updates
- **SendGrid** - Email notifications and confirmations
- **Google Maps API** - Delivery zone mapping and distance calculation

### DevOps & Development
- **Docker** - Containerization for consistent environments
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Reverse proxy and static file serving
- **pnpm** - Efficient package management for monorepo
- **ESLint + Prettier** - Code quality and formatting
- **Husky** - Git hooks for code quality
- **GitHub Actions** - CI/CD pipeline automation

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/restaurant-app.git
cd restaurant-app
```

### 2. Install dependencies

#### Using pnpm (Recommended)
```bash
# Install all dependencies
pnpm install
```

#### Or install individually

##### Restaurant Frontend
```bash
cd apps/landing
npm install
```

##### Restaurant Backend
```bash
cd apps/backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
# Copy environment files
cp .env.example .env
cp apps/landing/.env.example apps/landing/.env.local
cp apps/backend/.env.example apps/backend/.env
```

Restaurant Frontend `.env.local`:
```env
VITE_API_URL=http://localhost:5000/api/v1
VITE_CLERK_PUBLISHABLE_KEY=pk_test_your_clerk_key
VITE_STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_key
VITE_GOOGLE_MAPS_API_KEY=your_maps_api_key
```

Restaurant Backend `.env`:
```env
DATABASE_URL="postgresql://postgres:password@localhost:5432/restaurant_db"
PORT=5000
SECRET_KEY="your-super-secret-jwt-key"
CLERK_JWKS_URL=https://your-restaurant.clerk.accounts.dev/.well-known/jwks.json
STRIPE_SECRET_KEY=sk_test_your_stripe_secret
TWILIO_ACCOUNT_SID=your_twilio_sid
SENDGRID_API_KEY=your_sendgrid_key
```

### 4. Start the database
```bash
# From project root - start PostgreSQL with Docker
docker-compose up -d postgres

# Wait for database to be ready
sleep 30
```

### 5. Set up the database
```bash
cd apps/backend
# Generate Prisma client
npx prisma generate

# Run database migrations
npx prisma migrate dev --name restaurant_init

# Seed with sample restaurant data (optional)
python -m scripts.seed_restaurant_data
```

### 6. Start the development servers

#### Option A: Start all services with pnpm
```bash
# From project root
pnpm dev
```

#### Option B: Start services individually

##### Terminal 1 - Restaurant Backend
```bash
cd apps/backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn main:app --reload --port 5000
```

##### Terminal 2 - Restaurant Frontend
```bash
cd apps/landing
npm run dev  # Runs on port 3000
```

#### Access Your Restaurant App
- **Restaurant Website**: [http://localhost:3000](http://localhost:3000)
- **Menu & Ordering**: [http://localhost:3000/menu](http://localhost:3000/menu)
- **Admin Dashboard**: [http://localhost:3000/admin](http://localhost:3000/admin)
- **API Documentation**: [http://localhost:5000/docs](http://localhost:5000/docs)
- **Alternative API Docs**: [http://localhost:5000/redoc](http://localhost:5000/redoc)

## 📁 Project Structure

```
restaurant-app/
├── apps/                          # Restaurant applications
│   ├── landing/                   # Customer-facing restaurant app
│   │   ├── src/
│   │   │   ├── components/        # UI components
│   │   │   │   ├── menu/         # Menu browsing components
│   │   │   │   ├── cart/         # Shopping cart components
│   │   │   │   ├── order/        # Order management components
│   │   │   │   ├── reservation/  # Table reservation components
│   │   │   │   └── admin/        # Admin dashboard components
│   │   │   ├── pages/            # Page components
│   │   │   ├── hooks/            # Custom React hooks
│   │   │   ├── services/         # API services
│   │   │   ├── stores/           # Zustand state stores
│   │   │   └── types/            # TypeScript definitions
│   │   └── public/               # Static assets (logos, images)
│   └── backend/                   # Restaurant API server
│       ├── app/
│       │   ├── api/              # API route handlers
│       │   │   ├── menu/         # Menu management endpoints
│       │   │   ├── orders/       # Order processing endpoints
│       │   │   ├── reservations/ # Reservation endpoints
│       │   │   ├── admin/        # Admin-only endpoints
│       │   │   └── auth/         # Authentication endpoints
│       │   ├── core/             # Core configuration
│       │   ├── models/           # Pydantic data models
│       │   └── services/         # Business logic services
│       ├── prisma/               # Database schema & migrations
│       ├── scripts/              # Database seeding scripts
│       └── main.py               # FastAPI entry point
├── docs/                          # Documentation
│   ├── restaurant/               # Restaurant-specific docs
│   │   ├── PROJECT_OVERVIEW.md   # Architecture overview
│   │   ├── FEATURES.md           # Feature specifications
│   │   ├── RESTAURANT_DATABASE.md # Database schema
│   │   ├── RESTAURANT_API.md     # API documentation
│   │   ├── UI_COMPONENTS.md      # Component library
│   │   ├── ADMIN_FEATURES.md     # Admin dashboard guide
│   │   ├── IMPLEMENTATION_GUIDE.md # Step-by-step guide
│   │   └── QUICK_START.md        # Rapid setup guide
│   └── original/                 # Original template docs
├── docker/                        # Docker configurations
│   ├── nginx/                    # Nginx reverse proxy
│   └── volumes/                  # Persistent data storage
├── docker-compose.yml             # Development orchestration
└── pnpm-workspace.yaml           # Monorepo configuration
```

## 📝 Available Scripts

### Monorepo Scripts (from root)
- `pnpm dev` - Start all restaurant services (frontend + backend)
- `pnpm build` - Build all applications for production
- `pnpm lint` - Run ESLint on all projects
- `pnpm format` - Format all code with Prettier
- `pnpm test` - Run tests across all packages

### Restaurant Frontend (apps/landing)
- `npm run dev` - Start restaurant app development server (port 3000)
- `npm run build` - Build for production deployment
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint for code quality
- `npm run type-check` - TypeScript type checking

### Restaurant Backend (apps/backend)
- `uvicorn main:app --reload` - Start API development server (port 5000)
- `uvicorn main:app` - Start production API server
- `pytest` - Run backend tests
- `black .` - Format Python code
- `ruff check .` - Lint Python code
- `npx prisma generate` - Generate Prisma client
- `npx prisma migrate dev` - Run database migrations
- `npx prisma studio` - Open database GUI
- `python -m scripts.seed_restaurant_data` - Seed with sample menu data

## 🐳 Docker Development

### Quick Start with Docker

1. **Copy environment file**
```bash
cp .env.example .env
```

2. **Start all restaurant services**
```bash
# From project root - starts everything
docker-compose up -d
```

This will start:
- **PostgreSQL database** (port 5432) - Restaurant data storage
- **Redis cache** (port 6379) - Session and cart caching
- **Restaurant Backend API** (port 5000) - FastAPI server
- **Restaurant Frontend** (port 3000) - Customer-facing app
- **pgAdmin** (port 5050) - Database management interface

3. **Set up restaurant database**
```bash
# Wait for services to start
sleep 30

# Run database migrations
docker-compose exec backend npx prisma migrate dev

# Seed with sample restaurant data
docker-compose exec backend python -m scripts.seed_restaurant_data
```

4. **Access your restaurant app**
- Restaurant app: http://localhost:3000
- Admin dashboard: http://localhost:3000/admin
- API docs: http://localhost:5000/docs

### Volume Management

All persistent restaurant data is stored in `docker/volumes/`:
- **PostgreSQL data**: `docker/volumes/postgres/` - Menu items, orders, reservations
- **Redis data**: `docker/volumes/redis/` - Session data and cart state
- **pgAdmin config**: `docker/volumes/pgadmin/` - Database GUI settings
- **File uploads**: `docker/volumes/uploads/` - Menu item images and assets

### Useful Docker Commands

```bash
# Start all restaurant services
docker-compose up -d

# View real-time logs
docker-compose logs -f backend     # API server logs
docker-compose logs -f frontend    # React app logs
docker-compose logs -f postgres    # Database logs

# Stop all services
docker-compose down

# Restart specific service
docker-compose restart backend

# Clean database (careful - removes all restaurant data!)
docker-compose down -v
rm -rf docker/volumes/postgres

# Backup restaurant data
tar -czf restaurant-backup-$(date +%Y%m%d).tar.gz docker/volumes/

# Restore from backup
tar -xzf restaurant-backup-20240101.tar.gz

# Production deployment
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## 🔧 Restaurant Configuration

### Database Setup
Configure your restaurant database in backend `.env`:
```env
DATABASE_URL="postgresql://postgres:password@localhost:5432/restaurant_db"
```

### Restaurant Architecture
This project uses a simplified restaurant-focused architecture:

1. **Customer Frontend** (`restaurant.com`)
   - Menu browsing and online ordering
   - Table reservations and takeaway orders
   - User accounts and order history
   - Integrated admin dashboard at `/admin`

2. **Restaurant Backend API**
   - Unified FastAPI server for all restaurant operations
   - Menu management and order processing
   - Real-time order tracking and notifications
   - Payment processing and customer management

### Authentication & Security
Clerk handles customer authentication with JWT verification:

**Frontend Configuration:**
```env
VITE_CLERK_PUBLISHABLE_KEY=pk_test_your_restaurant_key
```

**Backend JWT Verification:**
```env
CLERK_JWKS_URL=https://your-restaurant.clerk.accounts.dev/.well-known/jwks.json
SECRET_KEY="your-super-secret-jwt-key"
```

### Payment Processing
Stripe integration for order payments:
```env
STRIPE_SECRET_KEY=sk_test_your_stripe_secret
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_publishable
```

### External Services
Configure notification services:
```env
# SMS notifications for order updates
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token

# Email confirmations
SENDGRID_API_KEY=your_sendgrid_key

# Delivery zone mapping
GOOGLE_MAPS_API_KEY=your_maps_api_key
```

## 📚 Restaurant Documentation

### 🍽️ Restaurant-Specific Guides
- [**📋 Project Overview**](./docs/restaurant/PROJECT_OVERVIEW.md) - Architecture and system design
- [**🍕 Features Guide**](./docs/restaurant/FEATURES.md) - Complete feature specifications based on Figma
- [**🗄️ Database Schema**](./docs/restaurant/RESTAURANT_DATABASE.md) - Restaurant-specific database design
- [**🌐 API Documentation**](./docs/restaurant/RESTAURANT_API.md) - All restaurant API endpoints
- [**🎨 UI Components**](./docs/restaurant/UI_COMPONENTS.md) - Component library and design system
- [**👨‍💼 Admin Features**](./docs/restaurant/ADMIN_FEATURES.md) - Complete admin dashboard guide
- [**🔧 Implementation Guide**](./docs/restaurant/IMPLEMENTATION_GUIDE.md) - Step-by-step development guide
- [**⚡ Quick Start**](./docs/restaurant/QUICK_START.md) - 15-minute setup guide

### 📖 Original Template Documentation
- [General Architecture](./docs/ARCHITECTURE.md) - System design patterns
- [Deployment Guide](./docs/DEPLOYMENT.md) - Production deployment instructions
- [UI Specification](./docs/UI-SPEC.md) - Base design system
- [Admin Dashboard](./docs/ADMIN_DASHBOARD.md) - General admin patterns

## 🧪 Testing Your Restaurant App

### Frontend Testing
```bash
cd apps/landing

# Run unit tests for components
npm run test

# Run E2E tests for user flows
npm run test:e2e

# Test with coverage reports
npm run test:coverage

# Type checking
npm run type-check
```

### Backend Testing
```bash
cd apps/backend

# Run API tests
pytest

# Test specific modules
pytest tests/test_orders.py
pytest tests/test_menu.py

# Run with coverage
pytest --cov=app tests/
```

### Manual Testing Flows
1. **Customer Journey**: Browse menu → Add to cart → Checkout → Track order
2. **Reservation Flow**: Check availability → Book table → Receive confirmation
3. **Admin Workflow**: Login → Manage menu → Process orders → View analytics

## 🚀 Restaurant Deployment

See [Implementation Guide](./docs/restaurant/IMPLEMENTATION_GUIDE.md) for detailed production deployment.

### Quick Deploy Options

#### Frontend (Vercel)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/restaurant-app&root-directory=apps/landing)

#### Backend (Railway)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/yourusername/restaurant-app&root-directory=apps/backend)

#### Full Stack (DigitalOcean)
- Use Docker Compose with production configuration
- Set up managed PostgreSQL database
- Configure domain and SSL certificates

## 🤝 Contributing to Restaurant App

1. Fork the restaurant app repository
2. Create your feature branch (`git checkout -b feature/new-restaurant-feature`)
3. Make your changes following the restaurant app patterns
4. Test your changes with the restaurant workflows
5. Commit your changes (`git commit -m 'Add new restaurant feature'`)
6. Push to the branch (`git push origin feature/new-restaurant-feature`)
7. Open a Pull Request with a detailed description

### Development Guidelines
- Follow the restaurant domain patterns established in the codebase
- Add tests for new restaurant features (orders, menu, reservations)
- Update relevant documentation in `docs/restaurant/`
- Ensure mobile-first responsive design for customer experience

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Figma Design**: Restaurant app design inspiration
- **Icons**: [Heroicons](https://heroicons.com/) and [Lucide React](https://lucide.dev/)
- **Images**: [Unsplash](https://unsplash.com/) for sample food photography
- **UI Components**: [shadcn/ui](https://ui.shadcn.com/) component library
- **Restaurant Inspiration**: Modern food delivery and restaurant management platforms

## 📞 Restaurant Support

- **Documentation**: Check [restaurant-specific guides](./docs/restaurant/)
- **Issues**: Create issues for bugs or feature requests
- **Discussions**: Use GitHub Discussions for restaurant app questions
- **Email**: support@your-restaurant-domain.com

## 🚀 Ready to Build Your Restaurant App?

1. **Quick Start**: Follow the [15-minute setup guide](./docs/restaurant/QUICK_START.md)
2. **Full Implementation**: Use the [comprehensive implementation guide](./docs/restaurant/IMPLEMENTATION_GUIDE.md)
3. **Customize**: Adapt the features to your restaurant's specific needs
4. **Deploy**: Launch your restaurant's digital ordering platform

**Happy cooking and coding! 🍽️👨‍💻**