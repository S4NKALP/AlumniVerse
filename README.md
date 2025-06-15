# 🎓 AlumniVerse

A web-based platform designed to connect, engage, and empower alumni. This project aims to build a strong, lifelong alumni community through user profiles, messaging, events, job opportunities, and more.

## 🚧 Project Status

> **Status**: 🛠 In development
> The repository has been initialized. Core architecture, models, and features are currently being designed. Code will be pushed incrementally as development progresses.

## 📄 Software Requirements Specification (SRS)

Check out our detailed [Software Requirements Specification](docs/SRS.md) that includes:

- Complete tech stack (React/TypeScript, Django, PostgreSQL, Redis, etc.)
- Detailed core features (User & Access, Alumni Directory, Events, Jobs, Messaging, etc.)
- Technical architecture and implementation details
- Database schema and API endpoints
- Development requirements and setup instructions
- User roles and permissions
- Development phases and deployment guidelines

## 🌟 Planned Features

### Core Features

- Alumni registration and login (with verification)
- Profile management (education, job, contact info)
- Alumni directory with search and filters (batch, program, location)
- Event creation and RSVP functionality
- Admin panel for managing users and content

### Advanced Features

- Private messaging and group chats
- Job and internship board
- Community posts, forums, and announcements
- Email/newsletter notifications
- Privacy settings for public/private profiles
- Batch-wise or interest-based groups and feeds

## 🛠 Tech Stack

- **Frontend**: React + TypeScript
- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT or OAuth 2.0
- **Dev Tools**: Docker, GitHub Actions, Postman
- **Deployment**: Render, Railway, or VPS

## 📁 Folder Structure

```
alumnivarse/
├── apps/                    # Django applications
│   ├── accounts/           # User authentication & profiles
│   ├── achievements/       # Alumni achievements & recognition
│   ├── dashboard/          # User dashboard & analytics
│   ├── events/            # Event management
│   ├── forum/             # Discussion forums
│   ├── jobs/              # Job board & opportunities
│   ├── messaging/         # Private messaging system
│   ├── mentorship/        # Mentorship program
│   ├── news/              # News & announcements
│   └── notifications/     # User notifications
│
├── config/                 # Project configuration
│   ├── settings/          # Settings modules
│   │   ├── base.py       # Base settings
│   │   ├── development.py # Development settings
│   │   └── production.py  # Production settings
│   ├── urls.py           # Project URL configuration
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
│
├── docs/                   # Documentation
│   └── SRS.md            # Software Requirements Specification
│
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project metadata and dependencies
├── manage.py              # Django management script
├── .env.example           # Example environment variables
└── .gitignore            # Git ignore rules
```

## 📅 Roadmap (Can be Modified)

### Phase 1: Project Setup & Core Backend 🚀

- [x] Repository initialization and project structure
- [x] Basic project configuration and settings
- [x] Authentication system implementation (accounts app)
- [ ] Database schema design and models
- [ ] Core API endpoints development
- [ ] User profile and settings functionality

### Phase 2: Feature Development 🛠

- [ ] Events management system
- [ ] Job board functionality
- [ ] Messaging system implementation
- [ ] News and announcements features
- [ ] Forum and discussion board
- [ ] Notifications system
- [ ] Mentorship program features
- [ ] Alumni achievements tracking

### Phase 3: Frontend Development 🎨

- [ ] UI/UX design system
- [ ] Component library setup
- [ ] Authentication and user flows
- [ ] Dashboard and profile pages
- [ ] Events and jobs interfaces
- [ ] Messaging and notifications UI
- [ ] Forum and discussions interface
- [ ] Mobile responsive design

### Phase 4: Integration & Testing ⚙️

- [ ] API integration with frontend
- [ ] Unit tests for backend
- [ ] Integration tests
- [ ] E2E testing setup
- [ ] Performance optimization
- [ ] Security testing and fixes
- [ ] Bug fixes and improvements

### Phase 5: Deployment & Launch 🌐

- [ ] Production environment setup
- [ ] CI/CD pipeline configuration
- [ ] Documentation completion
- [ ] Beta testing phase
- [ ] Production deployment
- [ ] Monitoring and logging setup
- [ ] Initial user onboarding

## 🤝 Contributing

Contributions are welcome after the initial setup is complete.
Please follow standard practices and guidelines for AGPL-licensed software.

## ⚖ License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.
See the full license in the [LICENSE](./LICENSE) file.

> 🔐 Under the AGPL, if you deploy this project for public use, you must also make the complete source code publicly available.

---

> Stay tuned for project updates, SRS release, and development milestones. 🚀

---

<sub>
_"A man without aims is like a monkey."_ 🐒
— Sankalp, building one line of code at a time
</sub>
