<div align="center">
  <h1>BookView - Code Institute Project 4</h1>
</div>

<a href="https://bookviewc-7148162b5406.herokuapp.com/"><strong>BookView</a></strong> is a full-stack blog platform built using Django that allows users to create, share, and engage with book reviews. It provides a space for book lovers to express their thoughts and opinions, explore new literary works, and interact with a community of like-minded readers. The platform combines robust back-end functionality with an intuitive front-end interface, making it easy for users to contribute reviews and comment on posts.

<div align="center">
  <img src="https://github.com/user-attachments/assets/7f488f67-3863-4c0f-9cb7-d65484b0542a" alt="BookView Preview">
</div>

## Table of Contents

- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Goals](#goals)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Wireframes](#wireframes)
  - [Entity-Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
- [Methodology](#methodology)
  - [Agile Approach](#agile-approach)
- [Key Features](#key-features)
  - [Homepage](#homepage)
  - [Profile Page](#profile-page)
  - [Review Pages](#review-pages)
- [Technologies Used](#technologies-used)
- [Deployment & Development](#deployment--development)
  - [Local Setup](#local-setup)
  - [Deployment Process](#deployment-process)
- [Testing](#testing)
- [Credits](#credits)


# User Experience (UX)

BookView is designed with simplicity and community engagement in mind, providing an intuitive and enjoyable experience for book lovers. Here's an overview of the key features and user journey on the platform:

 #### User Stories

 Site Owner Goals

- **Create a Community for Book Lovers**:  
  As the site owner, I want to create a welcoming platform where users can share their book reviews, discover new reads, and interact with others who share their passion for literature.

- **Encourage User Engagement**:  
  I want users to engage with content by creating reviews, commenting on others' posts, and forming discussions around their favorite books.

- **Provide a User-Friendly Experience**:  
  I aim to ensure that the platform is easy to navigate, intuitive, and accessible across various devices so that users can enjoy a seamless experience.

- **Ensure Content Quality**:  
  I want to implement moderation features to maintain high-quality content and foster respectful discussions within the community.

#### User Goals

- **Discover and Explore Book Reviews**:  
  As a user, I want to easily browse book reviews so that I can discover new books to read and find inspiration from other readers.

- **Create an Account and Personalize My Profile**:  
  I want to create an account and customize my profile to represent my identity within the community.

- **Write and Share Reviews**:  
  I want to write and share my book reviews with other users to express my thoughts and share my literary experiences.

- **Engage with Other Users**:  
  I want to comment on other users' reviews, join discussions, and connect with like-minded book lovers.

- **Easily Navigate the Platform**:  
  I want a simple and intuitive interface so that I can quickly find what I'm looking for, whether it's browsing reviews, creating a post, or interacting with others.

![image](https://github.com/user-attachments/assets/6ec47717-ad2c-4d2b-a593-fdd09a0a4082)

## Color Scheme

The BookView color palette creates a clean, balanced, and user-friendly design, focusing on visual clarity and minimalism.

**Neutral Base Colors**

- Light Gray, Neutral Gray, Off White: Clean background for a spacious, uncluttered look.

**Accent Colors**

 - Bright Blue (#546CFF): Interactive elements like buttons and links.

 - Deep Purple (#1D1141): Headers, navigation bars, and important content.

 - Muted Gray (#888888): Secondary information.

**Contrasting Dark Color**

- Dark Charcoal (#2B2B25): Emphasizes headers and key text for readability.

**Design Approach**

- Minimalist Palette: Limited colors for a clean design, focusing on content.

- Accessibility: High contrast for readability.

## Typography

For the visual identity of this project, I have selected two fonts to maintain a consistent and professional look:

- **The Bold Font**: Used for the **logo**. It gives a strong and distinctive personality.
  - Font URL: [The Bold Font](https://fonts.cdnfonts.com/css/the-bold-font)

- **Lato**: Used for the **body text** to ensure readability and clarity across various devices and screen sizes.
  - Font URL: [Lato](https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap)

These fonts help create a modern, cohesive style for the branding and readability of the project.

## Wireframes

For designing the wireframes of this project, I chose **Figma** due to its powerful, visual, and collaborative design capabilities. Figma allows for:

- **Visual-first approach**: Its intuitive, drag-and-drop interface makes it easier to create wireframes with precision and clarity.
- **Cloud-based**: Access the wireframes from anywhere, without worrying about software installation.

You can view the project wireframes or contribute to the design directly in my [Figma project](https://www.figma.com/design/rzCnEerXNQuigsn4g0sbp4/Untitled?node-id=1-2&node-type=frame).

#### Entity-Relationship Diagram (ERD)
![Entity-Relationship Diagram](https://github.com/user-attachments/assets/cf53a6b9-00d5-4968-a74b-3b5d90f91f54)



To design and visualize the Entity-Relationship Diagram (ERD) for this project, I chose **drawSQL** due to its user-friendly interface and powerful features. 


## Agile Methodology

I use Agile methodology with a Kanban board to visually track progress. Each user story breaks the project into manageable tasks, which are prioritized in the User Story List.

To prioritize, I apply the MoSCoW method (Must-Have, Should-Have, Could-Have, Won’t-Have), ensuring critical features are done first. Each story also has clear Acceptance Criteria to confirm when it's complete and functioning correctly.

![Agile User Stories Screenshot](https://github.com/user-attachments/assets/67a37df2-c2a1-4fd4-8fcf-b7fb326ec0ab)
![MoSCoW Prioritization Screenshot](https://github.com/user-attachments/assets/a245feb7-5093-4dde-8dd1-32c3d3b39dce)


## Features

### Homepage

The homepage offers a range of features designed to provide users with an intuitive and engaging experience. Below is a breakdown of the key features in the order users would naturally encounter them:

#### 1. **Navigation Bar**
   - A fixed top navigation bar with easy access to core sections of the website: **Home**, **Reviews**, and **About**.
   - A **Search bar** is available to quickly search for reviews or books.
   - **Login** and **Sign-Up** buttons are prominently displayed in the top-right corner for user authentication and new user registration.

#### 2. **Homepage Banner**
   - A large, visually engaging banner welcomes users to "Read, Review, and Reflect."
   - Includes a **Call-to-Action button** labeled **Join the Club**, encouraging users to become a part of the community.

#### 3. **Latest Reviews Section**
   - This section highlights the **latest book reviews** from the community.
   - Each review card features:
     - **Book Title** and cover image.
     - **Author Information** and publication date.
     - A **short snippet** of the review content.
     - A **"Read full post"** button to view the full review details.

#### 4. **Call to Action (Sign-Up Prompt)**
   - Located near the bottom of the homepage, this section invites users to **Sign Up**.
   - It emphasizes community building, encouraging users to share their passion for books with like-minded readers.

#### 5. **Footer**
   - Contains copyright information and credits to the platform creator.


#### Homepage (Logged In)

- **Banner Section**: 
  - Includes a search bar to quickly find books or reviews.
  
- **Call to Action**:
  - Located at the bottom of the page, inviting users to write their own reviews with a **Write a Review** button.
  - A message encouraging users to share their thoughts and help fellow readers.

- **Navigation Bar**:
 - A new **My Reviews** link has been added to the navigation, allowing users to view a dedicated page with all of their posted reviews.


This logged-in homepage is designed to keep users engaged by showcasing the latest content and encouraging them to participate in the community.

--- 

### My Reviews Page

The **My Reviews Page** allows logged-in users to view all the posts they have written.


- **Page Title**: Displays "My Reviews" to indicate the current page, followed by the user's name and their posts.
  
- **Posts List**: 
  - If there are no reviews yet, a message appears saying "Currently no posts to display," along with a **Write a Review** button to encourage users to write their first review.
  - If the user has posts, they are displayed in a grid format, each featuring:
    - The book title and cover image.
    - A brief excerpt of the review.
    - The publication date and the option to read the full review.
    - **Edit/Delete** icons, allowing users to modify or remove their reviews.
  
- **Pagination**: 
  - Pagination controls allow users to navigate through multiple pages of their reviews if they have posted many.
  
- **Write a Review Button**: 
  - A clear button that takes users directly to the **Write a Review** page if they want to create new content.

- **Navigation Bar**:
  - Provides easy access to **Home**, **My Reviews**, **Reviews**, and **About** sections.
  - Includes a **Write a Review** button and a **Logout** button for managing account access.

---

### Login Page

The **Login Page** allows returning users to sign in to their accounts and access the platform’s features.

- **Welcome Message**: A friendly welcome back message greets users, making the login process more personable.
- **Login Form**: Users are prompted to enter their:
  - **Email**: The email address associated with their account.
  - **Password**: The corresponding account password.
- **Continue Button**: A clear and prominent button for submitting login credentials and signing in.
- **Sign-Up Option**: For new users, a link to the **Sign-Up** page is provided below the form to encourage account creation.
- **Forgot Password Option**: A link for users who may have forgotten their password, allowing them to recover or reset it.
- **Navigation Bar**: Provides easy access to **Home**, **Reviews**, and **About** sections, with **Login** and **Sign-Up** buttons visible at the top.

---

### Sign-Up Page

The **Sign-Up Page** allows new users to create an account on the platform.

- **Welcome Message**: A friendly greeting to welcome new users.
- **Sign-Up Form**: A simple form for new users to create their account by entering:
  - **Username**: The desired username for the account.
  - **First Name** and **Last Name**: User's personal details.
  - **E-mail**: A valid email address for account verification.
  - **Password** and **Password Confirmation**: Secure password entry with confirmation.
- **Continue Button**: A clear button to submit the sign-up form and create the account.
- **Navigation Bar**: Provides easy access to **Home**, **Reviews**, and **About** sections, with **Login** and **Sign-Up** buttons prominently displayed.

---

### Post Review Page

The **Post Review Page** presents the full content of a selected review.

- **Full Review Content**: Displays the complete review written by the user, including detailed insights and opinions on the book.
- **Author Info**: Shows the author’s name and the date the review was published.
- **Comments Section**: Allows users to read and leave comments on the review.
- **Sign-In Prompt**: If not signed in, users are prompted to log in to leave a comment.

---

### Profile Page

The **Profile Page** showcases the user's public information and all of their posted reviews.

- **Profile Information**: Displays the user’s profile picture, username, and a brief bio.
- **Location**: Displays the user’s location if provided.
- **List of Reviews**: Shows all the reviews the user has posted, with links to view each review in full.

#### Profile Page (Logged In)

Allows users to view and manage their personal information and see a list of their posted reviews.

- **Profile Information**: 
  - Shows the user’s location if provided.
  - An edit icon next to the bio allows users to update their profile details.
  
- **List of Reviews**:
  - Displays a list of all the reviews the user has posted.
  - Each review is clickable, directing the user to the full review details.
  
- **Navigation Bar**:
  - Provides easy access to **Home**, **My Reviews**, **Reviews**, and **About** sections.
  - Includes a **Write a Review** button to create new posts.
  - Shows the **Logout** button for users to sign out of their account.
  
  
This profile page is designed to give users an overview of their activity and easy access to review management and account settings.

#### Update Profile Page

The **Update Profile Page** allows users to edit their personal information and update their profile.

#### Features:
- **Profile Picture Upload**: Users can choose and upload a new profile picture.
- **Personal Details**: Fields to edit first name, last name, username, and bio.
- **Publish Button**: A button to save and publish the updated profile information.

---

### Write a Review Page

The **Write a Review Page** provides users with a form to submit new book reviews.

- **Title Field**: Users can enter the title of their review.
- **Post Image Upload**: Allows users to upload an image related to the book (e.g., cover).
- **Excerpt Field**: A short description or teaser for the review.
- **Content Field**: The main body of the review where users provide their thoughts and analysis.
- **Publish Button**: A button to submit the review and publish it on the platform.

---

### About Page

The **About Page** introduces **BookView** and its purpose, welcoming users to the community.

- **Welcome Message**: A brief description of the platform’s mission, inviting book lovers to join the community, share reviews, and discuss their favorite books.
- **Call to Action**: Encourages users to sign up and participate in discussions about literature.


## Technologies

### Programming Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Applications and Libraries

- [Visual Studio Code](https://code.visualstudio.com/)  
  My go-to code editor—lightweight, flexible, and packed with useful extensions that make development a breeze.

- [Django](https://www.djangoproject.com/)  
  A robust web framework that handles all the heavy lifting, letting me focus on building features rather than reinventing the wheel.

- [PostgreSQL](https://www.postgresql.org/)  
  My reliable database of choice—fast, powerful, and able to handle all the data my app throws at it.

- [Git](https://git-scm.com/)  
  Essential for version control—helps me track changes, collaborate, and avoid the dreaded "lost code" nightmare.

- [Figma](https://www.figma.com/)  
  Perfect for designing and prototyping visually before diving into code. It keeps my UI ideas clear and structured.

- [Heroku](https://heroku.com/)  
  A user-friendly platform to deploy my project without the hassle of managing servers—just push, and it’s live.

- [DrawSQL](https://drawsql.app/)  
  My go-to for visualizing database structures—makes it easy to map out relationships and see how everything fits together.



## Deployment & Local Development

### Local Development

To set up the project locally, follow these steps:

1. **Clone the Repository**:  
   First, clone the project to your local machine using Git:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create a Virtual Environment**:  
   Set up a virtual environment to isolate project dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:  
   Install the required dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:  
   Run migrations to set up the local PostgreSQL database:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:  
   Create an admin user for your local instance:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:  
   Start the development server to view the project locally:
   ```bash
   python manage.py runserver
   ```

### Deployment

The project is deployed using **Heroku**. Here's how you can deploy it:

1. **Set Up Heroku**:  
   Install the Heroku CLI and log in:
   ```bash
   heroku login
   ```

2. **Create a Heroku App**:  
   Create a new app on Heroku:
   ```bash
   heroku create your-app-name
   ```

3. **Set Environment Variables**:  
   Configure environment variables such as `SECRET_KEY`, `DATABASE_URL`, etc. using Heroku’s CLI:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   ```

4. **Deploy to Heroku**:  
   Push your code to Heroku:
   ```bash
   git push heroku main
   ```

5. **Migrate the Database**:  
   Run migrations on the Heroku database:
   ```bash
   heroku run python manage.py migrate
   ```

6. **Create a Superuser on Heroku**:  
   Create a superuser for your Heroku app:
   ```bash
   heroku run python manage.py createsuperuser
   ```

7. **Access the Live Site**:  
   Once the deployment is complete, visit your Heroku app at:
   ```bash
   https://your-app-name.herokuapp.com/
   ```

This section provides clear instructions for setting up the project locally and deploying it to Heroku.


## Testing

[Link to TESTING.md](TESTING.md)

## Credits

- **Favicon**:  
  The book icon used as the favicon was sourced from [Icons8](https://icons8.com/icons/set/book).

- **Hamburger Menu Tutorial**:  
  The responsive hamburger menu design was implemented following this helpful [YouTube tutorial](https://www.youtube.com/watch?v=flItyHiDm7E).

- **SVG to WebP Converter**:  
  SVG images were converted to WebP format using [CloudConvert](https://cloudconvert.com/svg-to-webp).

- **Code Institute's "I Think Therefore I Blog" Project**:  
  This project was inspired by Code Institute’s **"I Think Therefore I Blog"** walkthrough from the **Developing with Django** module, which provided a foundation for creating the blog functionality in this app.
- **ChatGPT**:  
  I used **ChatGPT** to help me write and generate content for the blog posts. It made the process quicker and easier by providing ideas and keeping the tone consistent, which let me focus more on building the platform itself. ChatGPT really helped take the pressure off when it came to writing, and made sure everything flowed smoothly.
