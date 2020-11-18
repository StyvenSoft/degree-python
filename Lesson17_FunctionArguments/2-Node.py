from review_lib import get_next_review, submit_review

none_var = None
if none_var:
  print("Hello!")
else:
  print("Goodbye")
 
# Prints "Goodbye"


# first we define session_id as None
session_id = None
active_session = ""
 
if session_id is None:
  print("session ID is None!")
  # this prints out "session ID is None!"
 
# we can assign something to session_id
if active_session:
  session_id = active_session.id
 
# but if there's no active_session, we don't send sensitive data
if session_id is not None:
  send_sensitive_data(session_id)


## Grab a new review using get_next_review(). Save the results into a variable called review

# define review here!
review = get_next_review()

if review is not None:
  submit_review(review)