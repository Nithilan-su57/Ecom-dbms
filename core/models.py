ecommerce-dbms/
│
├── core/                       # STAGE 1: Pure Python Business Logic
│   ├── __init__.py
│   ├── exceptions.py           # Custom business exceptions (e.g., OutOfStockError)
│   ├── models.py               # Pure Python data structures/dataclasses
│   └── services/               # Core procedural workflows
│       ├── __init__.py
│       ├── order_service.py    # Order placement, price calculation, validation
│       └── product_service.py  # Catalog handling, inventory level logic
│
├── db/                         # STAGE 2: Database Layer & Connection Wiring
│   ├── __init__.py
│   ├── connection.py           # SQLAlchemy async engine & session pool setup
│   ├── models.py               # ORM Mapping definitions (SQLAlchemy declarations)
│   └── repositories/           # Direct SQL query execution / function calls
│       ├── __init__.py
│       ├── order_repo.py       # Executes standard transactions or stored procedures
│       └── product_repo.py     # Performs raw/ORM database queries
│
├── api/                        # STAGE 3: FastAPI Delivery Network Layer
│   ├── __init__.py
│   ├── main.py                 # Application initialization & middleware configurations
│   ├── dependencies.py         # Database session injection & auth verification middleware
│   ├── schemas/                # Pydantic Request/Response validation layers
│   │   ├── __init__.py
│   │   ├── order_schemas.py
│   │   └── user_schemas.py
│   └── routers/                # Endpoint controllers splitting the two entry points
│       ├── __init__.py
│       ├── customer_api.py     # Storefront endpoints
│       └── manager_api.py      # Administration dashboard endpoints
│
├── web/                        # STAGE 4: The Web Client Interfaces
│   ├── index.html              # Core routing portal (Determines role redirection)
│   ├── customer/               # Stage 1 UI: Storefront
│   │   ├── index.html          # Product catalog grid
│   │   ├── cart.js             # Local state tracking & checkout API dispatcher
│   │   └── styles.css
│   └── manager/                # Stage 2 UI: Analytics Control Dashboard
│       ├── index.html          # Operational metrics dashboard panel
│       ├── dashboard.js        # Data engine processing metrics/trigger events
│       └── styles.css
│
├── tests/                      # Core Testing Framework
│   ├── __init__.py
│   ├── test_core.py            # Verifies service rules function cleanly in Python
│   └── test_db.py              # Assesses transactional database connectivity hooks
│
├── .env                        # Environment variables (DB URL, Port mappings, Secret Keys)
├── .gitignore                  # Keeps system trash out of your version tracking
├── README.md                   # Systematic documentation & setup configuration manual
└── requirements.txt            # Python development execution dependencies package list