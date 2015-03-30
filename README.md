# mamigot.me

(Currently, mamigot.me points to my LinkedIn profile. This will change relatively soon.)


API-centric personal web application built on AngularJS, Flask and MongoDB. The back-end, which is built on Python, Flask and MongoDB, hosts the website's data (primarily blog posts, project posts and configuration variables). The data is provided to the front-end, which is an AngularJS application, via asynchronous REST API calls. The server is configured through Nginx and Gunicorn.


The application, [mamigot](https://github.com/miguel5/mamigot.me/tree/master/mamigot), is divided at its highest level (once we're past the configurable server/WSGI layer) into the [api](https://github.com/miguel5/mamigot.me/tree/master/mamigot/api) and the [front-end](https://github.com/miguel5/mamigot.me/tree/master/mamigot/frontend/static).



### To-Do (in order of importance):
 * Database
  * Place projects and blog posts in the database (MongoDB)
<br>
 * Frontend
  * Fetch projects and blog posts using Angular's services
  * Set up contact form
<br>
 * Other
  * Add authentication to the API (for POST, PUT and DELETE)
  * Configure Nginx and Gunicorn
<br>
 * Create unit tests
 * Prepare back-up system for MongoDB and website data using cron
 * Implement Google's reCAPTCHA for contact form
 * Add CMS and WYSIWYG editor to website (be able to handle file uploads)
 * Resize images in the backend and improve website loading speed (compress, etc.)
 * Use a profiler to identify bottlenecks
  * https://gist.github.com/shreyansb/86b74ae47719a27bbb25
<br>
 * Add more external web services under "projects" (such as Stack Overflow)
