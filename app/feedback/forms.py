from django import forms
from feedback.tasks import send_feedback_email_task



class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        """Sends an email when the feedback form has been submitted."""
        send_feedback_email_task.delay(   # Calling .delay() is the quickest way to send a task message to Celery.
            self.cleaned_data["email"], self.cleaned_data["message"]
        )

        send_feedback_email_task.apply_async(args=[  # additionally supports execution options for fine-tuning your task message.
            self.cleaned_data["email"], self.cleaned_data["message"]
            ]
        )
        
        '''While .delay() is the better choice in a straightforward task message like this, 
        you'll benefit from many execution options with .apply_async(), such as countdown and retry.'''