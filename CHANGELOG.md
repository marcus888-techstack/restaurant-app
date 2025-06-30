# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [v0.1.3_dev] - 2025-07-01

### Added
- Authentication system with Clerk integration
- JWT verification middleware for backend API
- Protected routes in React frontend
- User authentication flow (sign up, sign in, sign out)
- API client with authentication support

### Changed
- Backend port from 5000 to 5001 to avoid conflicts
- Updated frontend API URL configuration

### Fixed
- CORS configuration to properly handle requests from frontend
- Missing .gitignore entries for backend and frontend

## [v0.1.2_dev] - 2025-06-30

### Added
- Complete FastAPI backend structure with modular design
- React frontend with component architecture
- API endpoints for auth, menu, and orders
- Frontend routing with React Router
- Tailwind CSS configuration
- Comprehensive .gitignore files

### Fixed
- Mermaid ER diagram syntax errors in documentation

## [v0.1.1_dev] - 2025-06-30

### Added
- Minimal restaurant app structure
- FastAPI backend setup
- React frontend apps
- pnpm monorepo configuration

## [v0.1.0_dev] - 2025-06-30

### Added
- Docker Compose configuration for two-app architecture
- Project restructuring for restaurant management platform
- Database authentication setup

### Changed
- Refactored project from generic template to Restaurant Management Platform
- Updated README with restaurant-specific features and deployment instructions

### Removed
- Outdated documentation files for generic admin dashboard

## [v0.1.0] - 2025-06-30

### Added
- Initial project release
- Basic project structure
- Core configuration files

[Unreleased]: https://github.com/marcus888-techstack/restaurant-app/compare/v0.1.3_dev...HEAD
[v0.1.3_dev]: https://github.com/marcus888-techstack/restaurant-app/compare/v0.1.2_dev...v0.1.3_dev
[v0.1.2_dev]: https://github.com/marcus888-techstack/restaurant-app/compare/v0.1.1_dev...v0.1.2_dev
[v0.1.1_dev]: https://github.com/marcus888-techstack/restaurant-app/compare/v0.1.0_dev...v0.1.1_dev
[v0.1.0_dev]: https://github.com/marcus888-techstack/restaurant-app/compare/v0.1.0...v0.1.0_dev
[v0.1.0]: https://github.com/marcus888-techstack/restaurant-app/releases/tag/v0.1.0