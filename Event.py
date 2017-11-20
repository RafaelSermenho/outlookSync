class Event:
    def __init__(self, start, end, subject, location, html_body, text_body, attendees, required_attendees, optional_attendees, recurrence, recurrence_interval, recurrence_end_date, recurrence_days):
      self.start = start
      self.end = end
      self.subject = subject
      self.location = location
      self.html_body = html_body
      self.text_body = text_body
      self.attendees = attendees
      self.required_attendees = required_attendees
      self.optional_attendees = optional_attendees
      self.recurrence = recurrence
      self.recurrence_interval = recurrence_interval
      self.recurrence_end_date = recurrence_end_date
      self.recurrence_days = recurrence_days
   
    def __eq__(self, other):
        return self.start == other.start and self.end == other.end \
            and self.subject == other.subject and self.location == other.location \
            and self.html_body == other.html_body and self.text_body == other.text_body \
            and self.attendees == other.attendees and self.required_attendees == other.required_attendees \
            and self.optional_attendees == other.optional_attendees and self.recurrence == other.recurrence \
            and self.recurrence_interval == other.recurrence_interval and self.recurrence_end_date == other.recurrence_end_date \
            and self.recurrence_days == other.recurrence_days
