
# Terramo Backend

This repository contains the backend services for the Terramo project, including API, Celery workers, and more.

---

## 🧰 Prerequisites

- **Docker** and **Docker Compose** must be installed on your machine.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd terramo-backend
```

---

### 2. Set up environment variables

Navigate to the `.envs` directory:

```bash
cd .envs
```

Create a `.env` file by copying from the example:

```bash
cp .env.example .env
```

Then open `.env` and fill in the required values (e.g., database credentials, secret keys).

---

### 3. Create Docker network

Before starting the containers, create the required Docker network:

```bash
docker network create terramo_local_nw
```

---

### 4. Start the containers

Navigate to the directory where `local.yml` is located, then run:

```bash
docker compose -f local.yml up --build -d --remove-orphans
```

This will build and start the containers in detached mode.

---

### 5. Stop and remove the containers

When you're done, shut everything down with:

```bash
docker compose -f local.yml down -v
```

This stops and removes all containers and associated volumes.

---

## 🧼 Notes

- Make sure the `.env` file is correctly filled out to avoid runtime errors.
- The `terramo_local_nw` Docker network must exist before starting the services.

---
