# Library Management Server

## Run development server:
Clone project form git and go to project directory

Copy .env-example file to .env and override there.
```bash
cp .env-example .env
```

Build and run docker
```bash
docker-compose up --build -d
```

Run docker
```bash
docker-compose up -d
```

Open your browser and goto http://localhost:8000

## APIS
### Authors APIS
| HTTP Verb| Endpoints |
| ------------- | ------------- |
|GET    | /api/v1/authors/          |
|POST   | /api/v1/authors/          |
|GET    | /api/v1/authors/{id}/     |
|PUT    | /api/v1/authors/{id}/     |     
|PATCH  | /api/v1/authors/{id}/     |     
|DELETE | /api/v1/authors/{id}/     |

### Books APIS
| HTTP Verb| Endpoints |
| ------------- | ------------- |
|GET    | /api/v1/books/            |
|POST   | /api/v1/books/            |
|GET    | /api/v1/books/{id}/       |
|PUT    | /api/v1/books/{id}/       |
|PATCH  | /api/v1/books/{id}/       |
|DELETE | /api/v1/books/{id}/       |

### Categories APIS
| HTTP Verb| Endpoints |
| ------------- | ------------- |
|GET    | /api/v1/categories/       |
|POST   | /api/v1/categories/       |
|GET    | /api/v1/categories/{id}/  |
|PUT    | /api/v1/categories/{id}/  |
|PATCH  | /api/v1/categories/{id}/  |
|DELETE | /api/v1/categories/{id}/  |

### Library stats (counts) APIS
| HTTP Verb| Endpoints |
| ------------- | ------------- |
|GET    | /api/v1/library-stat/     |
