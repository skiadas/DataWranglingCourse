# SQL Practice

This is a list of practice problems for creating SQL queries. They are based on the following tables:

messages
  ~ Contains messages. Fields:

    - `id`: INTEGER, primary key
    - `from`: VARCHAR(20) NOT NULL
    - `to`': VARCHAR(20) NOT NULL
    - `subject`: VARCHAR(140) NOT NULL
    - `body`: VARCHAR(5000) NOT NULL
    - `reply_to`: INTEGER  (foreign key to messages.id)
    - `created`: TIMESTAMP NOT NULL
    - `read`: INTEGER (0=false, 1=true) NOT NULL DEFAULT 0
    - `priority`: VARCHAR(1) NOT NULL DEFAULT "M" (possible values L/M/H)

tags
  ~ Contains message/tag pairs. Fields:

    - `msg_id`: INTEGER NOT NULL (foreign key messages.id)
    - `tag`: VARCHAR(20) NOT NULL

    Primary key is the pair `(msg_id, tag)`.

Practice problems:

1. Find the ids of all messages that are not replies to another message.
2. Find all messages with the tag "work".
3. Produce a list of all tags that are present on messages received by "peter" along with the number of messages each tag appears in, and order them from most used to least used.
4. Find all pairs of tags that appear in the same message. Ensure that the tags are distinct and that each pair appears only once (and regardless of which of the two tags is first in the pair).
5. Find all messages that contain the tag "work", and add the tag "todo" to them. (Optionally: make sure no error is generated if the "todo" tag is already present).
6. List all from/subject/body information for messages that are not read, that are of high priority. Optionally, restrict to those messages that contain the tag "work".
7. For each tag and priority level, count the number of unread messages with that tag and priority level.
8. Find all messages that are unread but have been replied to, and mark them as read.

