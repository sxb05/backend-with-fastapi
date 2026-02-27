# Deploying to Render

Render is a modern cloud platform that makes it easy to deploy Docker applications and databases.

## Prerequisites

- GitHub account with your code pushed to a repository
- Render account (https://render.com)

## Step 1: Push Your Code to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit with Docker setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/backend-with-fastapi.git
git push -u origin main
```

## Step 2: Create PostgreSQL Database on Render

1. **Log in to Render** and go to the Dashboard
2. **Click "New+" → "PostgreSQL"**
3. **Configure the database:**
   - **Name:** `fastapi-db` (or your preferred name)
   - **Database:** `fastapi_db` (or your preferred name)
   - **User:** `postgres` (default)
   - **Region:** Choose closest to your users
   - **PostgreSQL Version:** 16 (or latest)
4. **Click "Create Database"**
5. **Note the connection details** (you'll need them in Step 5):
   - Internal Database URL (for services in same region)
   - Host
   - Port (usually 5432)
   - Database name
   - User
   - Password

## Step 3: Update Dockerfile for Production

Update your [Dockerfile](Dockerfile) to remove the `--reload` flag for production:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Step 4: Create render.yaml (Infrastructure as Code)

Create a `render.yaml` file in your repository root for easy redeployment:

```yaml
services:
  - type: web
    name: fastapi-api
    env: docker
    dockerfilePath: ./Dockerfile
    autoDeploy: true
    envVars:
      - key: DATABASE_HOST
        fromDatabase:
          name: fastapi-db
          property: host
      - key: DATABASE_PORT
        fromDatabase:
          name: fastapi-db
          property: port
      - key: DATABASE_NAME
        fromDatabase:
          name: fastapi-db
          property: database
      - key: DATABASE_USERNAME
        fromDatabase:
          name: fastapi-db
          property: user
      - key: DATABASE_PASSWORD
        fromDatabase:
          name: fastapi-db
          property: password
      - key: SECRET_KEY
        generateValue: true
      - key: ALGORITHM
        value: HS256
      - key: ACCESS_TOKEN_EXPIRE_MINUTES
        value: "30"

databases:
  - name: fastapi-db
    databaseName: fastapi_db
    user: postgres
    region: oregon
    postgresMajorVersion: "16"
```

## Step 5: Create Web Service on Render

### Option A: Using GitHub Integration (Recommended)

1. **Go to Render Dashboard** → click **"New +"** → **"Web Service"**
2. **Connect GitHub repository:**
   - Click "Connect your GitHub account"
   - Select your `backend-with-fastapi` repository
3. **Configure the service:**
   - **Name:** `fastapi-api`
   - **Environment:** `Docker`
   - **Region:** Same as database (e.g., Oregon)
   - **Branch:** `main`
   - **Dockerfile:** `./Dockerfile` (default)
   - **Plan:** Free tier (or Starter for production)
4. **Add Environment Variables** (under Advanced):
   ```
   DATABASE_HOST: [From PostgreSQL Internal URL]
   DATABASE_PORT: 5432
   DATABASE_NAME: fastapi_db
   DATABASE_USERNAME: postgres
   DATABASE_PASSWORD: [Your DB password]
   SECRET_KEY: [Generate a secure key - use Python: secrets.token_urlsafe(32)]
   ALGORITHM: HS256
   ACCESS_TOKEN_EXPIRE_MINUTES: 30
   ```
5. **Click "Create Web Service"**

### Option B: Using Infrastructure as Code

1. Push your `render.yaml` to GitHub
2. In Render Dashboard → **"New +"** → **"Infrastructure as Code"**
3. Select your repository with `render.yaml`
4. Click **"Deploy"**

## Step 6: Configure Your Database Connection

The database URL from Render will look like:
```
postgresql://user:password@host:5432/database_name
```

Extract the components and add as environment variables:
- `DATABASE_HOST`: The hostname
- `DATABASE_PORT`: 5432
- `DATABASE_NAME`: Your database name
- `DATABASE_USERNAME`: postgres
- `DATABASE_PASSWORD`: Your password

## Step 7: Run Database Migrations

Once your service is deployed:

1. **Go to your Render service**
2. **Click the "Shell" tab** at the top
3. **Run migrations:**
   ```bash
   alembic upgrade head
   ```

## Step 8: Verify Deployment

- **Access your API:** `https://your-service-name.onrender.com`
- **View API docs:** `https://your-service-name.onrender.com/docs`
- **Check logs:** Click "Logs" tab in your service

## Environment Variables to Set on Render

| Variable | Value | Notes |
|----------|-------|-------|
| `DATABASE_HOST` | From Postgres service | Use internal URL for same region |
| `DATABASE_PORT` | `5432` | Standard PostgreSQL port |
| `DATABASE_NAME` | `fastapi_db` | Your database name |
| `DATABASE_USERNAME` | `postgres` | Default user |
| `DATABASE_PASSWORD` | Your secure password | Store securely in Render |
| `SECRET_KEY` | Generate with `secrets.token_urlsafe(32)` | Keep secure, change in production |
| `ALGORITHM` | `HS256` | JWT algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Token expiration time |

## Troubleshooting

### "Connection refused" from FastAPI to Database
- Ensure you're using the **Internal Database URL** for services in the same region
- Check that environment variables match your database credentials
- Verify the PostgreSQL service is in the same region as your web service

### Migrations fail on deployment
- Connect to your service shell and run: `alembic upgrade head`
- Ensure your Alembic config uses environment variables for database connection

### Service keeps restarting
- Check logs for errors: Click "Logs" tab
- Verify all required environment variables are set
- Ensure database is accessible and credentials are correct

### Port issues
- Render automatically maps port 8000
- Change in `.on_render.com` environment, the service uses port 8000 internally

## Useful Render Commands

**View deployment logs:**
- Go to your service → "Logs" tab

**SSH into running container:**
- Go to your service → "Shell" tab

**Restart service:**
- Go to your service → "Manual Deploy" → "Deploy latest commit"

**Scale service:**
- Go to your service → "Settings" → change Plan tier

## Scaling & Production Considerations

- **Free tier:** Limited to hobby-grade performance, may sleep after inactivity
- **Starter tier:** $7/month, always running guaranteed
- **PostgreSQL:** Render's free tier databases may be slower; consider upgrading for production

## Next Steps

1. Monitor your application logs regularly
2. Set up automated backups for your PostgreSQL database
3. Consider adding monitoring and alerts
4. Scale up if you need production-level performance
5. Implement HTTPS SSL/TLS (Render handles this automatically)

---

For more details, visit [Render Docs](https://render.com/docs)
