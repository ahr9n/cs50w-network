# Network
Project 4 for CS50’s Web Programming with Python and JavaScript.

## Overview
A design of Twitter-like social network website for making posts and following users.

## Preview
![Home Page](https://github.com/ahr9n/cs50w-network/blob/master/network/static/network/assests/network.png)

## Specification
This project fulfills the following requirements:

* **New Post:** Users who are signed in will be able to write a new text-based post by filling in text into a text area and then clicking a button to submit the post. 
  * The screenshot at the top of this specification shows the “New Post” box at the top of the “All Posts” page.
* **All Posts:** The “All Posts” link in the navigation bar takes the user to a page where they can see all posts from all users, with the most recent posts first.
  * Each post includes the username of the poster, the post content itself, the date and time at which the post was made, and the number of “likes” the post has.
* **Profile Page:** Clicking on a username loads that user’s profile page. This page:
  * Displays the number of followers the user has, as well as the number of people that the user follows.
  * Displays all the posts for that user, in reverse chronological order.
  * For any other user who is signed in, this page also displays a “Follow” or “Unfollow” button that will let the current user toggle whether they are following this user’s posts. Notice that this only applies to any “other” user: a user can not be able to follow themselves.
* **Following:** The “Following” link in the navigation bar takes the user to a page where they see all posts made by users that the current user follows.
  * This page behaves just as the “All Posts” page does, just with a more limited set of posts.
  * This page is only be available to users who are signed in.
* **Pagination:** On any page that displays posts, posts are only displayed 10 on a page. If there are more than ten posts, a “Next” button is appeared to take the user to the next page of posts (which is older than the current page of posts). If not on the first page, a “Previous” button appears to take the user to the previous page of posts as well.
* **Edit Post:** Users are able to click an “Edit” button or link on any of their own posts to edit that post.
  * When a user clicks “Edit” for one of their own posts, the content of their post should be replaced with a `textarea` where the user can edit the content of their post.
  * The user should then be able to “Save” the edited post, without reloading the page, using JavaScript.
  * For security, this application is designed such that it is not possible for a user, via any route, to edit another user’s posts.
* **“Like” and “Unlike”:** Users are able to click a button or link on any post to toggle whether they “like” that post.
  * Using JavaScript, asynchronously I let the server know to update the like count (as via a call to `fetch`) and then update the post’s like count displayed on the page, without requiring a reload of the entire page.

## Setup
Requires Python3 and the package installer for Python (pip) to run:

* Install requirements (Django4): `pip install -r requirements.txt`
* After cloning the repository, head/refer to the project folder and:
  1. Create new migrations based on the changes in models: `python3 manage.py makemigrations network`
  2. Apply the migrations to the database: `python3 manage.py migrate`
  3. Create a superuser to be able to use Django Admin Interface: `python3 manage.py createsuperuser`
  4. Run the app locally: `python3 manage.py runserver`
  5. Visit the site: `http://localhost:8000`
  6. Enjoy!

## Topics
Built with [`Python`](https://www.python.org/downloads/), [`Django`](https://www.djangoproject.com/), [`JavaScript`](https://www.javascript.com/), and HTML/CSS..
