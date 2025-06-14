# AlumniVerse - Software Requirements Specification

## Project Overview

**AlumniVerse** is a web-based alumni network management platform built with React/TypeScript frontend and Django REST API backend.

## Tech Stack

- **Frontend**: React with TypeScript, Tailwind CSS
- **Backend**: Django with Django REST Framework
- **Database**: MySQL (development), PostgreSQL (production)
- **Authentication**: JWT with optional Multi-Factor Authentication (MFA)
- **Real-time**: WebSockets via Django Channels and Redis for messaging and notifications

## 🚀 Core Features

### 👤 User & Access

- Email-based registration and login (JWT)
- Optional multi-factor authentication (MFA)
- Roles: Alumni, Staff, Admin
- Password reset & session timeout

### 🧑‍🎓 Alumni Directory

- Rich profiles (education, work, location)
- Filtered search + map view
- Connection requests & privacy settings

### 📅 Events

- Host online/offline events
- Register, track attendance, and integrate calendars
- Support for paid events (Stripe/PayPal)

### 💼 Jobs & Careers

- Post jobs, apply, and upload resumes
- Set alerts and book career sessions
- Track certifications and skills

### 💬 Messaging

- Real-time 1:1 and group chat (WebSockets)
- File sharing, search, and message history
- Forums with moderation tools

### 📚 Learning & Mentorship

- Enroll in courses, track progress
- Get certifications
- Match with mentors and follow learning paths

### 💰 Donations

- One-time or recurring donations
- Campaigns and receipt generation

### 📊 Analytics

- User activity and event insights
- Custom reports and dashboards
- Fundraising and donation metrics

## 🔧 Technical Overview

### 💻 Frontend (What users see)

- Built with modern tools (React, TypeScript) for a fast and smooth experience
- Works well on phones, tablets, and computers
- Clean and responsive design using Tailwind CSS
- Forms, buttons, and pages that update quickly and feel like an app

### 🧠 Backend (What powers the system)

- Built with Django (Python) to handle logic, data, and security
- Uses an API system so frontend and backend can talk to each other
- Handles login, user roles, events, messages, and more
- Includes admin panel to manage users, jobs, events, etc.

### 🔐 Security

- Passwords are safely encrypted
- Login uses secure tokens (JWT)
- Optional two-step verification for better protection
- Private data is kept safe and only visible to the right users

### 💬 Real-Time Messaging

- Users can chat instantly — like WhatsApp or Messenger
- System uses WebSocket technology to send and receive messages live
- Group chats and file sharing are also supported

### 🗃️ Database

- Stores all information (users, messages, jobs, etc.) in a structured way
- Uses MySQL during development and PostgreSQL in live servers

### 💸 Payments & Events

- Supports paid event registrations and donations (via Stripe or PayPal)
- Sends confirmation emails after payments
- Can sync with Google or Outlook Calendar

### 📊 Dashboard & Reports

- Admins can view analytics like:
  - Active users
  - Event attendance
  - Job applications
  - Donation totals
- Reports can be downloaded when needed

### 🚀 Deployment & Hosting

- Runs on reliable servers using modern web hosting tools
- Sends emails, handles chat, stores files, and keeps things running smoothly

### Database Schema (Key Entities) (Subjected to Change)

```
Users: id, email, password_hash, role, created_at, updated_at
Profiles: user_id, first_name, last_name, bio, location, graduation_year
Events: id, title, description, date, capacity, location, event_type
Jobs: id, title, company, description, requirements, salary_range
Messages: id, sender_id, recipient_id, content, timestamp
Donations: id, user_id, amount, campaign_id, payment_status
```

### API Endpoints (Core)(Can be Added/Modified)

```
Authentication:
POST /api/auth/login
POST /api/auth/register
POST /api/auth/refresh

Alumni Directory:
GET /api/alumni?filters
GET /api/alumni/{id}
PUT /api/alumni/{id}

Events:
GET /api/events
POST /api/events
POST /api/events/{id}/register

Jobs:
GET /api/jobs
POST /api/jobs
POST /api/jobs/{id}/apply

Messages:
GET /api/messages
POST /api/messages
WebSocket: /ws/chat/

Donations:
POST /api/donations
GET /api/donations/history
```

## 🧑‍💻 Development Requirements

### 💻 System Requirements

- **Operating System**: Linux (recommended because I use that 😂), macOS, or Windows (WSL works well)
- **Python**: 3.10 or later
- **Node.js**: 18 or later (required for React + Vite)
- **npm** or **pnpm**: Latest stable version
- **MySQL**: 8.x (for development)
- **PostgreSQL**: 14+ (optional, for production testing)
- **Redis**: 6.x or later (for WebSocket and caching)
- **Docker** (optional): For containerized development

---

### 🔧 Development Tools

- **Code Editor**: VS Code or Neovim (with your favorite plugins)
- **Version Control**: Git + GitHub
- **API Testing & Documentation**: Swagger or Django REST Framework’s built-in documentation UI
- **Browser DevTools**: Chrome or Firefox (for frontend debugging)

### 📦 Backend Setup (Django)

- Create and activate virtual environment
- Install dependencies via `pip` or `uv`
- Set up `.env` file with:
  - `SECRET_KEY`
  - `DEBUG`
  - `DB_CONFIG` (MySQL/Postgres)
  - `REDIS_URL`
  - `EMAIL_CONFIG`
- Run database migrations: `python manage.py migrate`
- Start development server: `python manage.py runserver`

### 💻 Frontend Setup (React + Tailwind)

- Navigate to the frontend directory
- Install dependencies: `npm install` or `pnpm install`
- Start dev server: `npm run dev`
- Tailwind is pre-configured using `postcss` and `autoprefixer`
- Axios is used to connect to the backend API

### 🔄 Real-time Features

- Redis server must be running locally
- WebSocket is enabled via Django Channels
- Use `daphne` or `uvicorn` for running ASGI app in dev
- Configure CORS and allowed origins for frontend-backend communication

### 🧪 Testing & Linting

- Django tests: `python manage.py test`
- React tests: `npm run test`
- Linting:
  - Python: `ruff` or `flake8`
  - JavaScript/TS: `eslint` + `prettier`
- Git pre-commit hooks (optional): Set up using `pre-commit`

### 🐳 Docker (Optional Dev Workflow)

- Dockerfile and `docker-compose.yml` included
- Run full stack with: `docker-compose up`
- Supports live-reloading in both frontend and backend

### 📝 Other Requirements

- Keep code modular and reusable
- Follow project naming conventions and folder structure
- Write docstrings, comments, and maintain clean commits
- Regularly pull and merge from the main branch

---

> ✅ Tip: Use a `.env.example` file to share config structure with the team.

## User Roles & Permissions (Will be Added/Modified)

**Alumni:**

- View/edit own profile
- Search directory
- Register for events
- Apply for jobs
- Send messages
- Make donations

**Staff:**

- Manage events
- Moderate content
- View analytics
- Manage job postings

**Admin:**

- Full system access
- User management
- System configuration
- Analytics access

## Development Phases

**The development will be divided into the following phases:**
**Most of the process may not be possible to cover all the phases**

### 1. Planning & Requirement Analysis

- Finalize feature list and project scope
- Define user roles and access levels
- Design database schema and API endpoints
- Prepare wireframes and UI mockups

### 2. Backend Development (Django)

- Set up Django project with REST Framework and Channels
- Implement user authentication (JWT + MFA)
- Build core APIs for Alumni Directory, Events, Jobs, Messaging, etc.
- Integrate Redis for caching and WebSocket support
- Write unit tests for backend functionality

### 3. Frontend Development (React + Vite + Tailwind)

- Initialize React project with TypeScript and Tailwind CSS
- Build reusable UI components aligned with wireframes
- Connect frontend to backend APIs using Axios
- Implement real-time messaging via WebSocket connection
- Add client-side validation and error handling
- Write frontend tests for critical components

### 4. Integration & Testing

- Test full user flows end-to-end (registration, messaging, events)
- Perform cross-browser and responsiveness testing
- Fix bugs and optimize performance
- Use Swagger or DRF docs to validate API contracts

### 5. Deployment & Monitoring (It May not be Possible to cover all the steps in this phase)

- Prepare production environment (PostgreSQL, Redis, Docker)
- Deploy backend and frontend (e.g., on VPS, cloud provider)
- Set up SSL, domain, and environment variables
- Monitor logs and app performance post-deployment
- Collect user feedback for future improvements

---

> 🔑 Tip: Follow Agile iterations with regular commits, code reviews, and testing in each phase for smoother delivery.

---

**Document Version:** 0.1
**Last Updated:** June 15, 2025
**Target Audience:** Development Team
