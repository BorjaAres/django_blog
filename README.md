# Django Blog Web App

[Link to Deployed Project](http://poleroso.pythonanywhere.com/)

## Project Description

This site is a Django-based web application that serves as a platform for sharing and discussing various topics related to tea. Users can register and authenticate to access the blog, read and search for posts, leave comments, and contact the site owners.

## Technologies Used

- Python
- Django
- HTML/CSS

## Features

The key features of the Poleroso Blog project include:

- User registration and authentication
- Blog post creation and management
- Commenting on blog posts
- Contact page for sending messages
- Social media sharing of blog posts

## Project Structure

The project is structured with the following Django apps:
- User (manages user authentication)
- Posts (manages blog post-related functions)
- Comments (handles comments on blog posts)
- Utilities (includes homepage, contact, and about us pages)

## User Stories

The project addresses the following user stories:

1. **User Registration and Authentication:**
   - Users can register for an account by providing their username, email, and password.
   - Registered users can securely log in using their email and password.
   - Users can log out of their account.

2. **Posts:**
   - Users can read blog posts on various tea topics.
   - Users can click on a blog post to read the full article.
   - Users can search for a post.
   - Users can share interesting blog posts on social media.
   - Admins and staff members can create and delete posts.

3. **Comments:**
   - Users can leave comments on blog posts.
   - Users can see their comment after creating it.
   - Users can read other people's comments.
   - Users can edit and delete their comments.
   - Only registered users can comment.

4. **Contact:**
   - Users can send messages to the page owners.
   - Users can send a message without re-entering their name and email if they are logged in.
   - Admins receive an email when a user sends a message.
   - User messages are stored in the database.

## Code Implementation

The project features custom user authentication, dynamic blog post creation, and a comment system. Code for comment handling allows users to edit and delete their comments.

## Testing

A total of 113 tests were implemented to ensure the project's functionality. These tests include unit tests for models, views, and URLs, resulting in a fully tested site.

## Future Improvements

In the future, the project may include additional features such as user profiles, image uploads, NLP for sentiment analisys in the comments, and improved search functionality among other features.


## Author

- Borja Ares
