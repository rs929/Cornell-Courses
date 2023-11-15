# Form Feedback Interactivity Planning

## _Planning_ Sketch(es)
> Include _planning_ sketch(es) of your form feedback interactivity.

![Planning Sketch](IMG_0431.jpg)


### Pseudocode Plan
> Write your interactivity pseudocode plan here.
> Pseudocode is not JavaScript. Please do not put JavaScript code here.

```
If pre-order button is clicked, and Name field empty, remove .hidden attribute from name-warning

If pre-order button is clicked, and Email field empty, remove .hidden attribute from email-warning

If pre-order button is clicked, and Number of Tickets field empty, remove .hidden attribute from ticket-warning

If pre-order button is clicked, and Location field empty, remove .hidden attribute from location-warning

If all fields are filled out and pre-order button is clicked, submit form

```


## Form Feedback Interactivity Critique
> Explain how your form feedback interactivity design employs each interactivity design principle.

- Affordances

    The affordance of our design is not idea since fails to indicate to the user that they need to fill out all the fields before submitting the form. Thus, the user may assume that they can submit the form even if some fields are left empty.


- Visibility

    The design has some visibility issues since the warning messages are hidden until the user clicks the pre-order button, which means that the user may not realize that there are missing fields until they try to submit the form. There should be a visibile indicator text that informs the user that all fields should be filled out.


- Feedback

    The design provides feedback by displaying warning messages if the user has not filled out all the required fields, so the feedback provided is sufficient in telling the user about missing information, but not about the submission of the form

- Familiarity

    Our design is decently familiar as it follows common web design practices for displaying warning messages when required fields are not filled out.
