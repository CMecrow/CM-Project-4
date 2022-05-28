# Off The Map

### For opinions so out there, they're off the map!

---

As a developer, I've been tasked with creating a website where users can post their unpopular opinions and like and comment on existing posts.

The project has been made using Django / Python, HTML, CSS and JavaScript.

[Here is the live version of this project](https://off-the-map.herokuapp.com/)

## Project Goals

The main goals of this project starting out were:
- To read, input and edit data in a data model, in this case using PostgreSQL.
- To provide a sign up and log in feature to the site, with being logged in providing access to interact with the site
- To create an admin log in where posts, users and comments could be moderated
- To provide the site user the ability to create, edit and delete their own posts

## User Stories



---

### Site Theme

The overall layout used was taken from [startbootstrap.com](https://startbootstrap.com/). This was done to speed up site completion as the functionality of the site was a primary goal, rather than the site appearance. Though the layout was premade, there was some customisation required to fit the overall theme of the site. The idea that users were submitting outlandish opinions that were so far out there they were 'Off the Map' gave a nice old nautical feel, that these opinions were off in uncharted waters. I decided not to lean into this too heavily and only use two ocean images, as not to distract from the posts, and also to use a handwritten style font, found on [GoogleFonts](https://fonts.google.com/specimen/Amatic+SC?category=Display,Handwriting&preview.text=Off%20The%20Map&preview.text_type=custom#standard-styles). This font was chosen because it would suit the theme and appear as though it was handwritten, but was also clearly legible for users with accessibility in mind.

## Features

### Existing Features

#### Homepage

The site has been designed to have a lot of content imediately visible when the site loads. The site will operate around two main layouts, the homepage and the individual post pages. The user generated content is very much the focus of this site so there was no need to add complex and text heavy navbar or header. Instead the choice was made to keep them simple and uncluttered so the content could take center stage.

#### Navbar

The navbar was kept clear and uncluttered with the site name on the left that also functions as 'home' navigation, and then only two links on the right hand side. Before the user had created an account or logged in, these would be 'Sign In' and 'Register'. Because the user can only view posts and not interact with the site before they're logged in, there was no need to add a 'Post' link until they were authenticated. Once an account has been created and the user has signed in, the links change to 'Post' and 'Sign Out', reflecting the new choices that are now available to the user. Getting the user to register and then sign in is very important for the site because it allows them to interact with existing posts, and also create posts themselves. Because of the importance of 'Register', 'Sign In' and then once completed, 'Post'. The navbar was chosen to be fixed at the top of the screen, allowing easy access at all times for the user. This was also important because of the amount of content displayed on the homepage, depending on device width, there could be a lot of scrolling involved for the user. To improve responsiveness, the layout chosen also includes the functionality for the nav links to collapse into a hamburger icon for ease of use. Though this may not have been explicitly useful in the current itteration of the site with there only being two links present, it would future proof any future site growth.

#### Footer

The footer has been designed to mirror the navbar in terms of both size, display and colour. Like the navbar, it is fixed to the bottom of the page, this is again to improve access to the links within the footer, and also to visually bookend the pages. The links included in the footer point to the site's social media presence (though currently link through to the respective homepages). Again, colour choice is kept very simple with clear distinction between link icons and background colour to help with accessibility.

#### Header + Mid page image and text

The header image is the only main image that's repeated across pages throughout the site. As mentioned, it was a priority that the created posts take the forground on the site, so any large images would have to be muted and not drag attention away. Both chosen images are of the ocean to match the theme of the site, and work more to break up the content and page than be a point of interest themselves. The acompanying text, 'Uncharted Waters' and 'Here be Monsters' again fit the nautical theme, but looked very boring and blockish when first put onto the page. To remedy this I duplicated the text and styled it via css to appear as a water reflection, taking guidance from both [this video](https://www.youtube.com/watch?v=nqa-nC6vMqY&t=1s), and [this tutorial](https://www.geeksforgeeks.org/how-to-create-reflection-effect-using-html-and-css/).

#### Post display

The post content is limited to 300 characters, this is by design as the user is meant to be leaving unpopular opinions, rather than sentences to potentially justify the opinions or make a case. It's up to the other users to like the posts to make that decision! Because the posts are then relatively short, on a wider device, we can have them displayed as four across a row, reducing as the width of the page reduces. This is good for the user as it means they can browse more content straight away and then select a post they find interesting to read the comments or give it a like. 
The post cards themselves contain, the post content, the post author, the date and time the post was made and finally the post interactions, the amount of likes and comments left. With this format, the user can see which posts have had the most interaction and can join the conversation or read reactions to the post. The cards have a faint blue patterned background with a drop shadow to lift them off the plain white background of the homepage.
The homepage has 2 displays of 8 posts. The first section of 8 is limited via pagination in the view with posts being ordered by the likes (labelled in the view and model as 'votes'), left on each post. The second section of 8 is limited by slicing the list of posts to display the first 8 when listed in order by which they were created.
This decision was made because the site does not contain any actual pagination, so it was important to display both the most popular posts, but also the new posts so they could be interacted with as well.

#### Individual post view

Each post card visible on the home page is a link to the individual post's page. This is indicated to the user via the cursor changing to pointer, indicating that the card can be clicked to take you elsewhere. The post's page displays the post in a similar format to the homepage, though this time in a much larger container and with some interactable icons. These icons are again only interactable if the user is registered and logged in.
- The first icon that can be clicked is the thumbs up, 'like' icon, with acompanying counter to its left. If clicked, the page is reloaded with the icon now appearing as blue along with the counter increasing, indicating that the like has been added. The icon can also be clicked again to remove the like, again refreshing the page and updating the icon and counter. Functionality has been added so that the likes are added to the database and each user can only like each post once. This keeps the post listing integrity intact, blocking users from inflating a post's like count by themselves.
- The second icon is not interactable, this is the comment icon with acompanything counter. This icon does not need to be interactable because the comment box is visibly situated just below the post, though this will be discussed later. 
- The third icon is the edit icon. This icon is only visible and interactable if the user who is viewing the post, is the user who intially created the post. This icon will take the user through to the 'edit post' page.
- The fourth icon is similar to the third, the delete icon. Again this icon is only visible and interactable if the user who is viewing the post is the user who created the post. Clicking this icon will take the user through to the 'delete post' page.

### Future Features

#### Post Display

 There are issues with the current post layout. For example if the site was used a lot and there were a lot of posts left, potentially posts could get lost inbetween the two displays. They may not fall into the first display as there wasn't enough likes on the post, but the post also wasn't new enough to be displayed in the second section ordered by creation. Should this be a concern the site could have more sections added or potentially pagination could be added for users to browse more or all posts.