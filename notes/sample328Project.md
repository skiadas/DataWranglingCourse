# Sample Project for CS 328

## Project H.E.M.P.

### Overview

H.E.M.P (Helpful Event and Meeting Planner) is a service designed to manage people's schedules.

- It will keep track of individuals as well as events for these individuals.
- It will provide a way for individuals to see their calendar, to create new events and to search for common meeting times for a set of individuals.

### Information Retrieval and Storage

We will maintain a database that likely contains the following tables:

- `users` contains personal user information, such as a user's name, possibly an affiliation or role.
- `events` contains events. An event has a title, some location information, start and end times/days, and an owner.
- `participants` pairs events with "participants". Each row contains an event, a participant/invitee to the event, and their "status" (accept/decline/waiting etc).

Later on it would be nice to integrate our app with something like Google Calendar.

### API

We describe here some of the resource paths we will consider.

- `/user` gives access to the list of users.
- `/user/{userid}` accesses a user's profile. Anyone can view/get, but may need permissions in order to edit/post.
- `/schedule` provides schedules for a one or more users (userids passed as parameters). It expects also a timeframe, and provides information about the schedules of the users on that timeframe and any common free times they have.
- `/event` provides access to the list of all events. It should allow passed parameters for filtering the list of events (e.g. all events that occur today). A lot of query possibilities here.
- `/event/{eventId}` provides access to a specific event.
- `/event/{eventId}/invite` is the list of invites to users for this event.
- `/event/{eventId}/invite/{userId}` pertains to the invite of a specific user to the event, and its status.
