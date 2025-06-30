# Restaurant App - Quick Start

## ⚡ 5-Minute Setup

```mermaid
flowchart LR
    A[Clone Repo] --> B[Install Dependencies]
    B --> C[Setup Environment]
    C --> D[Start Database]
    D --> E[Run Migrations]
    E --> F[Start Dev Servers]
    F --> G[Access App]
```

## 🚀 Quick Commands

```bash
# 1. Clone and setup
git clone <repo-url>
cd restaurant-app
pnpm install

# 2. Environment setup
cp .env.example .env
cp apps/landing/.env.example apps/landing/.env.local
cp apps/backend/.env.example apps/backend/.env

# 3. Database startup
docker-compose up -d postgres
sleep 30

# 4. Database setup
cd apps/backend
npx prisma generate
npx prisma migrate dev --name init
npx prisma db seed

# 5. Start development
cd ../..
pnpm dev
```

## 🌐 Access Points

After setup, your app will be available at:

- **Landing Site**: http://localhost:3000
- **Restaurant App**: http://localhost:5173
- **Admin Dashboard**: http://localhost:5173/admin
- **API Docs**: http://localhost:5000/docs

## 🔧 Configuration

### Quick Environment Setup

**Frontend (.env.local):**
```env
VITE_API_URL=http://localhost:5000/api/v1
VITE_CLERK_PUBLISHABLE_KEY=pk_test_your_key
```

**Backend (.env):**
```env
DATABASE_URL="postgresql://postgres:password@localhost:5432/restaurant_db"
PORT=5000
SECRET_KEY="your-secret-key"
```

## 🛠️ Development Commands

```bash
# Start all services
pnpm dev

# Individual services
pnpm dev:frontend  # Port 3000
pnpm dev:backend   # Port 5000

# Database management
npx prisma studio  # Database GUI
npx prisma migrate dev  # Run migrations

# Testing
pnpm test          # Run all tests
pnpm test:e2e      # End-to-end tests
```

## 🎯 Quick Demo

1. **Landing Site**: Visit http://localhost:3000 for marketing page
2. **Browse Menu**: Visit http://localhost:5173/menu
3. **Add Items**: Click "Add to Cart" on menu items
4. **View Cart**: Click cart icon in header
5. **Admin Access**: Visit http://localhost:5173/admin
6. **Manage Orders**: Process orders in admin dashboard

## 🔍 Troubleshooting

**Database Connection Issues:**
```bash
docker-compose restart postgres
```

**Port Already in Use:**
```bash
lsof -i :3000  # Check what's using port 3000
kill -9 <PID>  # Kill the process
```

**Module Not Found:**
```bash
rm -rf node_modules package-lock.json
pnpm install
```