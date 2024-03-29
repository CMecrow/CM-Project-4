# Off The Map

### For opinions so out there, they're off the map!

---

As a developer, I've been tasked with creating a website where users can post their unpopular opinions and like and comment on existing posts.

The project has been made using Django / Python, HTML, CSS and JavaScript.

~~[Here is the live version of this project](https://off-the-map.herokuapp.com/)~~

The project was redeployed via Render because of the changes to free Heroku hosting. [Link here.](https://cm-project-4.onrender.com/)

## Project Goals

The main goals of this project starting out were:
- To read, input and edit data in a data model, in this case using PostgreSQL.
- To provide a sign up and log in feature to the site, with being logged in providing access to interact with the site
- To create an admin log in where posts, users and comments could be moderated
- To provide the site user the ability to create, edit and delete their own posts

## User Stories

- As a site user I can register an account so that I can comment, like and post.
- As a site user I can view a paginated list of posts so that I can view the post without the comments
- As a site user I can leave comments on a post so that I can share my opinion
- As a site user / admin I can view the interaction on each post so that I can judge user reaction
- As a site user / admin I can view comments on an individual post so that I can read reaction
- As a site user I can click on a post so that I can read the post with the comments
- As a site user I can upvote or downvote a post so that I can interact with the content
- As a site user I can edit my own post so that I can edit if required or delete it

Note: These are available in the GitHub repo via a kanban board created in Projects. The second and seventh user story are discussed in more detail in the Future Features section

---

### Site Theme

- The overall layout used was taken from [startbootstrap.com](https://startbootstrap.com/). This was done to speed up site completion as the functionality of the site was a primary goal, rather than the site appearance. Though the layout was pre-made, there was some customisation required to fit the overall theme of the site. The idea that users were submitting outlandish opinions that were so far out there they were 'Off the Map' gave a nice old nautical feel, that these opinions were off in uncharted waters. I decided not to lean into this too heavily and only use two ocean images, as not to distract from the posts, and also to use a handwritten style font, found on [GoogleFonts](https://fonts.google.com/specimen/Amatic+SC?category=Display,Handwriting&preview.text=Off%20The%20Map&preview.text_type=custom#standard-styles). This font was chosen because it would suit the theme and appear as though it was handwritten, but was also clearly legible for users with accessibility in mind.

---

## Wireframes

![https://i.imgur.com/Ag3mu5L](https://i.imgur.com/Ag3mu5L.jpg "Site wireframes")

## Features

### Existing Features

### Homepage

- The site has been designed to have a lot of content immediately visible when the site loads. The site will operate around two main layouts, the homepage and the individual post pages. The user generated content is very much the focus of this site so there was no need to add complex and text heavy navbar or header. Instead the choice was made to keep them simple and uncluttered so the content could take centre stage.

### Navbar

![https://i.imgur.com/PDxoA1D](https://i.imgur.com/PDxoA1D.jpg "Site Navbar")

- The navbar was kept clear and uncluttered with the site name on the left that also functions as 'home' navigation, and then only two links on the right hand side. Before the user had created an account or logged in, these would be 'Sign In' and 'Register'. Because the user can only view posts and not interact with the site before they're logged in, there was no need to add a 'Post' link until they were authenticated. Once an account has been created and the user has signed in, the links change to 'Post' and 'Sign Out', reflecting the new choices that are now available to the user. Getting the user to register and then sign in is very important for the site because it allows them to interact with existing posts, and also create posts themselves. Because of the importance of 'Register', 'Sign In' and then once completed, 'Post'. The navbar was chosen to be fixed at the top of the screen, allowing easy access at all times for the user. This was also important because of the amount of content displayed on the homepage, depending on device width, there could be a lot of scrolling involved for the user. To improve responsiveness, the layout chosen also includes the functionality for the nav links to collapse into a hamburger icon for ease of use. Though this may not have been explicitly useful in the current iteration of the site with there only being two links present, it would future proof any future site growth.

### Footer

![https://i.imgur.com/qyn9swy](https://i.imgur.com/qyn9swy.jpg "Site Footer")

- The footer has been designed to mirror the navbar in terms of both size, display and colour. Like the navbar, it is fixed to the bottom of the page, this is again to improve access to the links within the footer, and also to visually bookend the pages. The links included in the footer point to the site's social media presence (though currently link through to the respective homepages). Again, colour choice is kept very simple with clear distinction between link icons and background colour to help with accessibility.

### Header + Mid page image and text

![https://i.imgur.com/vjbNOOm](https://i.imgur.com/vjbNOOm.jpg "Site header and text")

- The header image is the only main image that's repeated across pages throughout the site. As mentioned, it was a priority that the created posts take the foreground on the site, so any large images would have to be muted and not drag attention away. Both chosen images are of the ocean to match the theme of the site, and work more to break up the content and page than be a point of interest themselves. The accompanying text, 'Uncharted Waters' and 'Here be Monsters' again fit the nautical theme, but looked very boring and blockish when first put onto the page. To remedy this I duplicated the text and styled it via CSS to appear as a water reflection, taking guidance from both [this video](https://www.youtube.com/watch?v=nqa-nC6vMqY&t=1s), and [this tutorial](https://www.geeksforgeeks.org/how-to-create-reflection-effect-using-html-and-css/).

### Register

![https://i.imgur.com/oxYPwQB](https://i.imgur.com/oxYPwQB.jpg "Site Sign Up")

- The register page, accessed via the navbar is a simple sign up form. There is a direction to the sign in page should the user already have an account and then fields for Username, Email and Password. All fields are left aligned which means the input fields aren't aligned and appear a bit haphazard. This actually suits the theme of the site, with the 'Sign Up' font above it being handwritten, certain letters at an angle and at different heights. The email field is optional as the site does not currently have email verification, this is a feature that could be added in future and will be listed in the future features section below. The account authorisation, including registration is handled by django-allauth, [details here](https://django-allauth.readthedocs.io/en/latest/).

### Sign in

![https://i.imgur.com/ibe8Z49](https://i.imgur.com/ibe8Z49.jpg "Site Sign In")

- The sign in page is very similar to the register page described above. There is a link to the sign up page, should the user have clicked on the wrong option in the nav. Then there are input fields for username and password with a checkbox for remember me. After clicking submit, if unsuccessful an error of 'The username and/or password you specified are not correct.' If successful the user is taken back to the home page with a message to say that they've successfully signed in as their username.

### Sign out

![https://i.imgur.com/Z7nPdso](https://i.imgur.com/Z7nPdso.jpg "Site Sign Out")

- Only visible once the user is signed in, Sign Out if accessible via the navbar. Clicking the link takes you to a simple page with confirmation that you want to sign out and a submit button. If the button is pressed the user is given another confirmation message that they have successfully signed out.

### Post display

![https://i.imgur.com/Auxulat](https://i.imgur.com/Auxulat.jpg "Site post display")

- The post content is limited to 300 characters, this is by design as the user is meant to be leaving unpopular opinions, rather than sentences to potentially justify the opinions or make a case. It's up to the other users to like the posts to make that decision! Because the posts are then relatively short, on a wider device, we can have them displayed as four across a row, reducing as the width of the page reduces. This is good for the user as it means they can browse more content straight away and then select a post they find interesting to read the comments or give it a like. 
The post cards themselves contain, the post content, the post author, the date and time the post was made and finally the post interactions, the amount of likes and comments left. With this format, the user can see which posts have had the most interaction and can join the conversation or read reactions to the post. The cards have a faint blue patterned background with a drop shadow to lift them off the plain white background of the homepage.
The homepage has 2 displays of 8 posts. The first section of 8 is limited via pagination in the view with posts being ordered by the likes (labelled in the view and model as 'votes'), left on each post. The second section of 8 is limited by slicing the list of posts to display the first 8 when listed in order by which they were created.
This decision was made because the site does not contain any actual pagination, so it was important to display both the most popular posts, but also the new posts so they could be interacted with as well.

### Individual post view

![https://i.imgur.com/Au366ba](https://i.imgur.com/Au366ba.jpg "Individual post view")

- Each post card visible on the home page is a link to the individual post's page. This is indicated to the user via the cursor changing to pointer, indicating that the card can be clicked to take you elsewhere. The post's page displays the post in a similar format to the homepage, though this time in a much larger container and with some icons the user can interact with. These icons are again only accessible if the user is registered and logged in.
    - The first icon that can be clicked is the thumbs up, 'like' icon, with accompanying counter to its left. If clicked, the page is reloaded with the icon now appearing as blue along with the counter increasing, indicating that the like has been added. The icon can also be clicked again to remove the like, again refreshing the page and updating the icon and counter. Functionality has been added so that the likes are added to the database and each user can only like each post once. This keeps the post listing integrity intact, blocking users from inflating a post's like count by themselves.
    - The second icon is not interactable, this is the comment icon with accompanything counter. This icon does not need to be interactable because the comment box is visibly situated just below the post, though this will be discussed later. 
    - The third icon is the edit icon. This icon is only visible and interactable if the user who is viewing the post, is the user who initially created the post. This icon will take the user through to the 'edit post' page.
    - The fourth icon is similar to the third, the delete icon. Again this icon is only visible and interactable if the user who is viewing the post is the user who created the post. Clicking this icon will take the user through to the 'delete post' page.

#### Comments

- The comments box is displayed underneath the post (see image above). Under a heading of 'Comments', a list of all existing comments is displayed with most recent at the top, each comment details the user, the comment left and then the date and time that the comment was created. If the user viewing the post is logged in, they can leave a comment. They will be notified who they are posting as, should they have multiple accounts. If the comment field is left blank when the user hits submit then they will receive a prompt to enter a comment. Once the comment is successfully submitted, the page is refreshed so the user can see their entered comment, and a message is also shown at the top of the page confirming that the comment was left successfully. 

### Edit Post

![https://i.imgur.com/uamur0T](https://i.imgur.com/uamur0T.jpg "Edit post")

- As mentioned, if the user viewing the post is the post's author, an edit icon is visible. Clicking this will take the user to an edit post page where the title and post itself can be changed. Hitting submit on the post will then submit the post, take the user back to the post detail page and provide a message confirming this to the user.

### Delete Post

![https://i.imgur.com/JxW3and](https://i.imgur.com/JxW3and.jpg "Delete post")

- Again, if the user viewing the post is the post's author, a delete icon is visible. Clicking this will take the user to a delete post page where the post is displayed along with the like and comment counter. There is a distinct confirmation box displayed below the post providing the user with the option of cancelling which redirects back to the post detail page, or confirming, where the post will be deleted and a message displayed to the user.

### Create Post

![https://i.imgur.com/Tbp9gXH](https://i.imgur.com/Tbp9gXH.jpg "Create post")

- If the user is signed in, they'll have access to the 'Post' option on the navbar. Clicking this link will take the user to the new post page. This is a very simple form where they'll be asked for a post title and the post content itself. Both fields are required to complete the form and there's validation to make sure that they are completed. Once done, the user can hit Submit and they'll be sent to the home page with a confirmation message that their post was successful.

### Messages

![https://i.imgur.com/YtMQsIa](https://i.imgur.com/YtMQsIa.jpg "Site messages")

- Inbuilt django messages have been configured in this project to display successes to the user. A user will receive a message placed just under the nav that will disappear after 3 seconds on the following actions:
    - Signing In
    - Signing Out
    - Leaving a comment
    - Submitting a post
    - Editing a post
    - Deleting a post

### Admin Page

![https://i.imgur.com/JoFNUSR](https://i.imgur.com/JoFNUSR.jpg "Admin page")

- The admin page is handled by django's built in admin panel. From here the site admin can moderate posts and comments, deleting or editing them as required. They can also moderate users and change passwords. One particularly useful action that can be taken on the admin page is archiving posts. As the first 8 posts on the homepage are displayed in order of popularity, the posts there could remain there for a long time. Should the admin decide to archive a post, it will then be removed from the page but still accessible via the admin page. The admin page also provides the user the ability to add comments or posts. When the project was first started, there was much more emphasis placed on the creation of posts from this page, so tools such a summernote were added to enhance the created posts. However, as the project developed it became clear that this functionality wouldn't be necessary in the current project iteration, as it was much easier and quicker to add posts from the main site pages. There was also an issue found with adding and then editing posts created in summernote, which is detailed in the testing document.

---

## Future Features

### Post Display

- There are issues with the current post layout. For example if the site was used a lot and there were a lot of posts left, potentially posts could get lost inbetween the two displays. They may not fall into the first display as there wasn't enough likes on the post, but the post also wasn't new enough to be displayed in the second section ordered by creation. This relates to the second listed user story of viewing a paginated list of posts. The goal of this user story was so that the user can view posts without the accompanying comments. This second section was important so that the user could glance over posts and find one that interested them, rather than having to trawl through content they weren't grabbed by, and the discussion surrounding them. This goal of the user story has been met with the current structure of the home page. A concern over adding extra site pages and pagination was that the site could become cluttered and slow to load. Should these concerns be addressed, there are a couple of solutions that could be implemented. You could keep the current structure of 8 posts, then an image, then 8 posts, carrying on for a much larger quantity, potentially add a menu to 'Sort By'. Or the home page could be kept the same but new pages added, one for 'Most Popular' where a larger amount of posts could be displayed and one for 'New' where all the new posts across a certain period would be shown. This feature was not added to the original design of the site because of the size of the task and aforementioned concerns, impacting both time constraints and knowledge gaps.

### Post Categories

- With some expansion on the post model and PostList view, each post could be assigned a category by the post author or admin, so users could select to view only posts of that category, for example 'food', 'sports', 'politics' or 'animals'. This feature was outside the scope of the current project iteration due to time constraints.

### Post images

- At the beginning of the project, there was an idea to include an image with posts, set by the post author. To facilitate this, cloudinary was installed. It become clear however that this was unnecessary given the site purpose, and an image would detract from the theme of the site, and also from the user experience as a whole. It's benefits would be very niche and it would be potentially open to misuse, making the moderation of the site more difficult. Cloudinary has been left in the project should any image functionality be required once a solution has been found to the aforementioned problems, as well as to host static and media files once deployed to Heroku. One such use of images that would not impact the site's theme would be adding more customisation and an image upload for user profiles.

### User Profiles

- One feature that may improve user engagement with the site would be adding customisation to user profiles. As mentioned this could utilize cloudinary's image hosting to display a small thumbnail profile picture next to a user's comment. Including images in this way would not impact the homepage, with comments only being visible on each individual post's page. Django's built in admin panel does have sections for user's first name or last name, which could be utilised in the register page to improve communications from the site admin to the site user, instead of having to refer to people via their usernames. This feature was not included in the current iteration due to knowledge gaps and the time that'd be required to implement it. 

### Downvote

- The main feature that could not be added in the project's current iteration was the downvote feature. The project was started with the idea of having posts voted on, rather than being liked. Because of this, any classes or variables related to this functionality are usually called vote or votes, rather like or likes, which is what the feature became. The primary block on this feature was a knowledge gap, and a concern over the amount of time required to fill that gap so the feature could be implemented. The current iteration of the like functionality is flawed and would be one of the first features to be reviewed in the feature. The way that likes are stored and displayed via the page refreshing is far from ideal and I'm certain a more suitable solution could be found. Although not the original goal, users being able to like posts has still provided a large benefit to the project, not only improving the user experience and interaction with the site, but also providing a conventional pleasing way to sort the posts on the main page. A user would want and expect to see popular posts at the top of the page, and it makes the site look good to the user because it's promoting the posts with the most user interactions.

---

## Data Model

![https://i.imgur.com/oVbPugO](https://i.imgur.com/oVbPugO.jpg "Data Model")

The data model used relates to the Post and Comments features with the Post being the tying link between the two, identified via the post slug. This link is required for the comments to be attached to the relevant post. There are two aspects of the data model that are not currently being displayed to the user, namely the 'Update On' data in both post and comments. This was a conscious decision to stop the home page or post page from becoming too cluttered and text heavy. The data was left in the models as it could be used in future were users editing their posts to make the commenters look silly, so some sort of 'updated on' field needed to be displayed, or should it be required for some other functionality.

---

## Deployment procedure

- I created a new app on Heroku named off-the-map
- I then added a postgres database to the app in Heroku
- I took the postgres url from Heroku and added it as an environment variable in an env.py file in gitpod
- I added a secretkey as an environment variable in the same env.py file, then stored this as a config var in Heroku
- I imported the database url in settings.py along with adding the created environment variables to complete the database set up
- From my cloudinary account, I copied over my API environment variable and stored it as another environment variable in my env.py file and a config var in Heroku
- After making sure that cloudinary was installed in settings.py, I ensured that all media and static files would be stored there
- Once the templates directory has been created and joined with the base directory, I changed the DIRS key to refer to template directory variable
- I then added the Heroku link into the allowed hosts in settings.py
- I created a proc file to show Heroku what's required to run the project, entering web and gunicorn
- I set Debug to False in settings.py and added X_FRAME_OPTIONS = 'SAMEORIGIN' to enable the summernotes editor to work once the site has been deployed to Heroku.
- I removed the DISABLE_COLLECTSTATIC config var in Heroku
- Rather than then linking the Heroku app with Github's deployment, as that functionality had been removed due to a security concern, I deployed to Heroku directly from the gitpod terminal via the following commands:
    - heroku login -i
    - heroku git:remote -a off-the-map 
    - git push origin main (pushing to GitHub)
    - git push heroku main (pushing to Heroku)

---

## Credits

- Initial project creation, first deployment and starting structure was built from the Code Institute 'I Think Therefore I Blog' walkthrough project
- Chosen bootstrap template can be found [here.](https://startbootstrap.com/template/full-width-pics)
- Google Font can be found [here.](https://fonts.google.com/specimen/Amatic+SC?category=Display,Handwriting&preview.text=Off%20The%20Map&preview.text_type=custom#standard-styles)
- CSS text reflection tutorials [here](https://www.geeksforgeeks.org/how-to-create-reflection-effect-using-html-and-css/) and [here.](https://www.youtube.com/watch?v=nqa-nC6vMqY&t=1s)
- Creating the Edit and Delete functionality was aided by watching [this video.](https://www.youtube.com/watch?v=EX6Tt-ZW0so)
- Changing variables defined in the generic.ListView to display two views on one page was found [here.](https://stackoverflow.com/questions/31133963/multiple-models-generic-listview-to-template)
- Images were taken from [pexels.com](https://www.pexels.com/)

