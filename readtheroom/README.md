DOCUMENTATION:

## VIDEO LINK: https://youtu.be/jDwvcfCPQrU

## Background & Inspiration

Have you ever been at a function where the DJ was absolutely horrible? Have you noticed that at parties some DJs never look up from their computers to vibe check the crowd? Can your DJ just NOT read the room? This is why we created Read The Room, a web application that helps DJs do just that – Read The Room.

## How does it work?
Through our web interface, DJs are able to register an access code to their playing session. They can then share this with the people at the rager they’re playing for. All party goers have to do is type this access code into our login page, from their phone or another device, and BAM! 4 random songs are displayed on the page and they can vote for the one they want to play next. The DJ is able to call the vote at any time and only has to refresh the page in order to suggest new songs to vote on. When the vote is called, the winning song is displayed and the DJ can queue it on their song mix for their party!

## Running & Visualizing
We used the flask feature, combined with JavaScript (directly on the html pages) and Python in order to create our website. In order to generate a working version of the web application, you first need to create an API Token. We got ours from IEX cloud, which is the same website we used to get an API token from the finance Problem set in week 9. All you have to do is
1. Create an account as an “individual”
2. Choose a plan, we chose the free 30 day one.
3. Confirm your account via email
4. Copy the API Key on the Access & Security webpage
5. Type and run this into your terminal, with x representing your API token:
    $ export API_KEY= x
6. Then type and run this:
    $ flask run


## Using the website, page breakdown

Read The Room has in total 8 pages. When you first go to the website, you will first be met with the login page (login.html). Partygoers who have been given an access code by their DJ are able to type in the code here and then will be rerouted to enter the Select Song page (select.html). If they fail to enter a correct code, you will be rerouted to apology.html where you will see an image of Bad Bunny to indicate your error.

On this page, you will see on the left that there is an option in blue text on the left that says “DJ: Register”. Whoever is reviewing our project will need to press this option and create a code on the register page (register.html). Once created, you will be rerouted to the home page (index.html), which gives a description of the Read The Room web application. You will then have access to the Browse, Select Music, and  Rate DJ pages and be given an option of logging out through a navigation bar at the top of every page.

Since you’re the DJ who just created the access code in this scenario, if you navigate to the Select Music page (select.html) you will be able to see the randomly displayed songs, 4 buttons referring to the song displaced in the 1st, 2nd, 3rd, or 4th row, and a button on the bottom that says “call vote.”  In the table that shows the songs, you will see the artist who made the song, the song title, a danceability score, an energy score, and the genre of the song.  Every user who joins with your access code will have access to this same page and will be able to vote for their song an unlimited number of times, and will be able to base their vote on the relative danceability, energy, and genre of the songs. You can vote too. Whenever the DJ feels they have received enough votes, or near the time the currently playing song (at whatever party) ends, they can call the vote and a message saying “Song x wins!” will appear with x being either song 1, 2, 3, or 4. After the vote is called, you can refresh the page which will bring the vote counts back to 0 and show 4 randomly selected songs again.
To get a feel of what the partygoer side looks like, go ahead and log out. Now you will be redirected to the login page, and there you should type in your access code you made when you were a DJ. You will be rerouted to the Select Music page again and will be able to vote. Other partygoers will have access to this same page in this same session.

If you go to the Browse (browse.html) page via the top navigation bar after logging in with your access code, you will see a description of what the Danceability and Energy Scores represent and a Genre description. This will help the users understand what these mean on the select song page.

Users also have the ability to rate their DJ (rate.html)! While you’re still logged in, go ahead and navigate to the Rate DJ page through the top navigation bar. You will see an option to input your name into the text box feature and then a text box where you can write your feedback. Once these two boxes are filled, press the post comment button and your comment will be displayed on the bottom!
