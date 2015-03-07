# Photo Discovery
A web app to help photographers discover past images by placing them in a new context. 2/3 experiential art experiment 1/3 utility. This is for people like me, artists/photographers who have a backlog of photographs that are sitting, undiscovered, on a HDD, smart phone, Dropbox, etc.
This app is a conduit to discovery of these unseen images, beyond just chronological. A visual organization of the images to set them in a different context, allowing forgotten images to be displayed in an interesting and unique way.

## Personas
* Photographer with an archive of forgotten photos who wants to experience them in a new way. 

## Objectives
* Visual experience of a large number of images user images.

## Requirements
* Web application
* Get a large numbers of photos (100+) from the user
* Process this group of images in interesting ways
* Give the user a unique and visual experience of his/her images
* Allow the user to discover and explore their images

### Functionality and Use Flow
1. User registration
    1. Collect username, email, password
    2. Collect information about image collection
2. File upload by user
    1. Multiple files at once
    2. Upload progress indicator
    3. Parsing of embedded image information
    4. Pre-processing of images
    5. Save processed images to user media file
    6. Write image metadata to database
3. Image processing
    1. Run each image through the processing algorithm
    2. Save processed image information to the database
    3. Verify image data is able to be visualized
    4. Notify user that image collection is ready
4. User login
5. Display of all image collections
6. User selects collection
7. Visualized images are displayed
    1. Interaction and discovery tools are displayed
    2. Option to create unique sharable link (with UUID) to allow view without login
8. User dashboard
    1. Manage user information
    2. Manage image collections (CRUD)
    3. Manage individual collections (CRUD)

### Views
1. Login (index)
2. User Dashboard
  1. User profile view/edit
  2. Image Collection view/edit
  3. Individual collection edit
  4. Create/upload new collection
  4. Collection meta information (Zeitgeist) (default)
3. Image Visualization/Discovery (public and private)
4. User registration (username, email, password)

### Technologies
With what this app will be built
* Django backend
* Database - ???
* Frontend Framwork - Foundation ???
* Image Processing Package - Python packages ???

### Team
* Joshua Ferdaszewski - Developer, Designer, etc.
* Jonathan Marrs - Advisor, willing tester

### Schedule
* MVP by March 27th
