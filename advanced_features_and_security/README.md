# Custom User Model and Admin Permissions

## Overview
This task implements a custom user model using `BaseUserManager` and `AbstractBaseUser` in the `bookshelf` app.
It also configures admin permissions and groups for book access restrictions.

## Files Updated
- bookshelf/models.py
- bookshelf/admin.py
- settings.py
- bookshelf/views.py (permission checks)
- Migrations reset and recreated

## Steps Performed
1. Created the custom user model and manager.
2. Updated project settings to use `AUTH_USER_MODEL = 'bookshelf.CustomUser'`
3. Removed old migrations and db.sqlite3
4. Ran `makemigrations` and `migrate`
5. Created superuser
6. Configured user groups and permissions
   - Can View Books
   - Can Add Books
   - Can Change Books
   - Can Delete Books

## Permission Usage
Examples of permission checks were added to the `views.py` file.

## Admin Instructions
1. Login to admin using superuser credentials.
2. Create groups under `Authentication and Authorization`.
3. Assign permissions and users to the groups.

## How to Run
```bash
python manage.py runserver
