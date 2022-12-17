# Legal.ly

#### Video Demo:  <https://youtu.be/jRRkORdLFi4>
#### Description:

This is my final project for CS50. I developed a web application that enables users get access to legal aides from anywhere in Africa and named it the most effortless name ever - 	***Legal.ly***.

Now, let's delve into the depths of Legal.ly. Lets say for instance, we're home on a Friday night, hungry but too busy to go out, we grab our phones, open our food delivery app, and we scroll through looking for restaurants close to us, that particular meal we're craving and that the price that fits our need, we make our order and before we know it, our food is here.
Take all this and replace food with the legal world. Many persons or 'users' out there do not know the basic steps needed to get legal help in whatever situation they might find themselves in.
Legal.ly is made to deliver your legal aide to you. All you need to do is choose based on your preferences, i.e area of law you might require help in, the location you would like your attorney to be and the price that is well within your comfort range and before you know it, you're on a one on one with a hands-on attorney ready to help you.

Legal.ly is built on the Django framework and languages which include _PYTHON_, _HTML_, _CSS_ AND _JAVASCRIPT_.

__Python__ helped to bind the database, forms to the frontend and to implement the framework.

The __HTML__ on the various linked pages pages form a skeleton for Legal.ly to develop upon. Originally, I had tried to create a base.html page and continue to extend all other pages off of it, but due to design concerns, I created individual _html_ and _css_ for each page.

The __JAVASCRIPT__ really had me in a chokehold, but I was able to implement it using the _onclick_ function for the _carousel_ on the _homepage_.

I enjoyed coding with __CSS__ the most. I loved the free reign design options and exploration it gave me.

#### **WALKTHROUGH LEGAL.LY**
As a new, unregistered user looking up _Legal.ly_, the user is met with the _homepage_ with explains the basic mission of the web app and shows a sneak peek of the services rendered. A _contact form_ is also made available for any requests, enquries or complaints.
The code for this page can be found in the ***template and static*** folders under the ***legally*** main folder.

Navigating to the top of the page, the navigation bar displays the _'Home', 'Find An Attorney, 'Services' and 'Book An Appointment'_ tabs respectively.
The **Find An Attorney** and **Book An Appointment** pages are _restricted_ to the user as they are not yet registered or logged in on the app.
If clicked, the user is navigated to the login page and alternatively the register page.

To the right of the navigation bar is found the _Login and Register_ page.
The code for these pages can be found in the ***template and static*** folders under the ***users*** main folder.

Once the user registers, they are added to the _django database_ made available by the framework and can be accessed by only the admin on the admin page.
User is then redirected to the login page, where they login and are then again redirected to the homepage. Here, they would notice that the Login and register tabs have now been replaced by a _'Logout tab'_.
This was made possible by the user authentication provided by the Django Framework and can be found on the ***'urls' and 'views'*** under the ***users*** main folder.

Having registered and logged in, the user now has access to the _find an attorney_ page.

The **Find An Attorney** page displays all the attorneys registered on the web app's database. Their details such as _area of specialization_, _charging rate per hour_ amongst others are made available to the user to select based on their needs and preferences.
A _search bar_ is displayed on the top right where the user can search for a particular area of law and all attorneys practicing are shown up on the results.
Alternatively, a _filter option_ is provided for the user to select specific details such as gender(using Male or Female) and firm of practice.
Once these choices are selected, the practicing lawyers are displayed for the user to make a choice and book an appointment following the _'book an appointment'_ button.
The code for these pages can be found in the ***template and static*** folders under the ***legally main folder***.

The ***Book An Appointment*** page is a form for a user to fill in with their details, a date and time which falls within their comfort ranges.
Unfortunately, the forms do not go anywhere as the lawyers aren't particularly real, but in a real life, real time situation, the user would be reached out to by a member of the selected Firm's team to proceed on the case at hand.
The code for this page can also be found in the ***template and static*** folders in the ***legally main folder***.

Legal.ly functions as a bridge between the justice system of the society and the individuals of the society.
Working on this project massively expanded my knowledge in both the programming world and the legal world.

THIS IS LEGAL.LY by Stephanie Eigobhor

THIS IS CS50
