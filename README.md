# Django Blog

A simple and functional blog application built with Django. This blog allows users to create, edit, and delete posts, comment on posts, and includes features like comment moderation, user authentication, and a responsive design with Bootstrap and custom CSS.

## Features

### 1. User Authentication
- Users can register, log in, and log out.
- Secure password hashing using Django's built-in authentication system.

### 2. Post Management
- Users can create, edit, and delete their own blog posts.
- Each post contains a title, content, and an author field.
- Posts are associated with a timestamp indicating when they were created and last updated.

### 3. Commenting System
- Users can add comments to individual blog posts.
- Comment moderation: comments must be approved by an admin before being visible.
- Admins can approve, delete, or manage comments from the admin panel.

### 4. Responsive Design
- The blog's interface is built using **Bootstrap**, ensuring that the design is responsive and looks good on all devices.
- Custom **CSS** is used to further style the blog and enhance the user experience.

### 5. Pagination
- The post list page supports pagination, showing a limited number of posts per page and allowing users to navigate through pages.

### 6. Post Details
- Users can view individual post details, including the title, content, and comments (once approved).
- If logged in, users can add comments directly from the post detail page.

### 7. Admin Panel
- Full access to manage posts, users, and comments through Django’s built-in admin panel.
- Admins can manage all user-generated content and moderate comments.

## Technologies Used

- **Python**: Main language
- **Django**: Web framework used to build the blog.
- **SQLite**: Default database used to store all blog data.
- **Bootstrap**: Used to ensure responsive design and consistent UI across different devices.
- **CSS**: Custom styles added to improve the appearance of the blog.
- **HTML**: Template system provided by Django for the frontend structure.

## Setup Instructions

### 1. Clone the repository
```bash
https://github.com/Lorencoshametaj/Django-Blog.git
