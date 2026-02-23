<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=220&section=header&text=SQL%20%26%20PostgreSQL%20Learning%20Journal&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=FastAPI%20%7C%20SQLAlchemy%20%7C%20Authentication%20%7C%20Clean%20Backend%20Architecture&descAlignY=58" alt="Header Banner" />
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-Production%20API-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" /></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/PostgreSQL-Relational%20Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" /></a>
  <a href="https://www.sqlalchemy.org/"><img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" /></a>
  <a href="https://jwt.io/"><img src="https://img.shields.io/badge/JWT-Authentication-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT" /></a>
</p>

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnE4Zzl0Zm81aGp6aXU2a2M5b3Q1NG0xN3NvdHFwdjBzYjV0ejh6ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l0HlBO7eyXzSZkJri/giphy.gif" alt="Backend development visual" width="760" />
</p>

---

## Project Purpose

This repository is my structured backend learning journal. It captures what I learned while building and improving a FastAPI + PostgreSQL application through iterative commits.

Each phase of development documents practical growth in:

- API design and HTTP standards
- Relational data modeling
- ORM-based query patterns
- Authentication and authorization
- Code organization using routers and schemas

The repository is intentionally maintained as both a working project and a professional progress record.

---

## Learning Timeline Through Commits

The commit history reflects the progression from fundamentals to production-style backend patterns:

1. Core CRUD operations with PostgreSQL integration
2. Migration from direct SQL usage to SQLAlchemy models
3. Schema validation with Pydantic
4. Modularization through dedicated routers
5. User creation and secure password hashing
6. JWT authentication and login workflows
7. OAuth2-compatible token flow
8. Ownership-based authorization in product routes
9. Like/unlike functionality with relationship logic

This progression represents practical, hands-on backend engineering rather than isolated examples.

---

## Current Architecture

```text
Client Request
   |
   v
FastAPI Routers
(products, users, auth, likes)
   |
   v
Pydantic Schemas (request/response validation)
   |
   v
SQLAlchemy ORM Models
   |
   v
PostgreSQL Database
