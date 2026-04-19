## 📊 Repository Overview

```
Repository: EmranHejazi/banker
Owner: EmranHejazi
Created: 3 minutes ago
Last Updated: 1 minute ago
Visibility: Public
Default Branch: main
```

**Language Composition:**
- Python: 59.2%
- TypeScript: 29.2%
- JavaScript: 4.4%
- CSS: 4.4%
- Dockerfile: 2.8%

---

## 📁 Project Structure

```
banker/
├── .DS_Store
├── README.md (minimal - just contains "# banker")
├── docker-compose.yml
├── backend/
│   ├── .env
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
├── frontend/
│   ├── .gitignore
│   ├── Dockerfile
│   ├── README.md
│   ├── package.json
│   ├── package-lock.json
│   ├── tsconfig.json
│   ├── next.config.ts
│   ├── eslint.config.mjs
│   ├── tailwind.config.js
│   ├── postcss.config.mjs
│   ├── app/
│   └── public/
├── data/
├── db/
└── scripts/
```

---

## 🐳 Docker Configuration

```yaml name=docker-compose.yml url=https://github.com/EmranHejazi/banker/blob/main/docker-compose.yml
services:
  postgres:
    image: postgres:16
    container_name: banker_db
    restart: always
    environment:
      POSTGRES_DB: banker
      POSTGRES_USER: banker
      POSTGRES_PASSWORD: password
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U banker -d banker"]
      interval: 5s
      timeout: 3s
      retries: 10
    volumes:
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    container_name: banker_api
    restart: always
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      DATABASE_URL: postgres://banker:password@postgres:5432/banker
    ports:
      - "8000:8000"

  frontend:
    container_name: banker_web
    build:
      context: ./frontend
      dockerfile: Dockerfile
    restart: unless-stopped
    ports:
      - "3000:3000"
    environment:
      NEXT_PUBLIC_API_URL: http://localhost:8000
    depends_on:
      - backend
    volumes:
      - ./frontend:/app # bind mount for live reload
      - /app/node_modules # so node_modules stays INSIDE container

volumes:
  postgres-data:
```

---

## 📝 Frontend Documentation

```markdown name=frontend/README.md url=https://github.com/EmranHejazi/banker/blob/main/frontend/README.md
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app).

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
```

---

## 🔍 Root README Status

The root README.md is minimal:
```markdown name=README.md url=https://github.com/EmranHejazi/banker/blob/main/README.md
# banker
```


## 💡 Project Analysis

**Technology Stack:**
- **Backend:** Python (likely FastAPI or Flask based on the requirements.txt)
- **Frontend:** Next.js (TypeScript, Tailwind CSS, ESLint)
- **Database:** PostgreSQL 16
- **Infrastructure:** Docker + Docker Compose

**Architecture:**
- Multi-container setup with proper service dependencies
- Database health checks ensure proper initialization order
- Live reload support for frontend development
- Environment-based configuration
