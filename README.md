Pastebin API (Django REST Framework)

A minimal Pastebin-style REST API built using Django REST Framework (DRF).
This project is based on the official DRF tutorial and demonstrates how to build, serialize, and expose APIs using Django.

🚀 Features

Create, read, update, delete code snippets

Syntax highlighting with Pygments

User authentication

Permissions & ownership

Browsable REST API

Clean DRF ViewSets & Routers

🛠 Tech Stack

Python 3

Django

Django REST Framework

🌐 API Endpoints
Method	Endpoint	Description
GET	/snippets/	List all snippets
POST	/snippets/	Create a snippet
GET	/snippets/{id}/	Retrieve a snippet
PUT	/snippets/{id}/	Update a snippet
DELETE	/snippets/{id}/	Delete a snippet
GET	/users/	List users

SQLite (default)

Pygments (syntax highlighting)

🔐 Permissions

Read access for everyone

Write access only for authenticated users

Only owners can edit or delete their snippets

🎨 Syntax Highlighting

Snippets support syntax highlighting using Pygments with selectable:

Programming language

Style/theme

Line numbers

📚 Learning Goals

This project helps you understand:

Serializers & ModelSerializers

ViewSets & Routers

Permissions & authentication

RESTful API design

Browsable DRF UI
