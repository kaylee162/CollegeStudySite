from django.db import models
from django.contrib.auth.models import User

class TutoringSession(models.Model):
    # Main fields
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_sessions')
    subject = models.CharField(max_length=100)

    # Time fields
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # Additional fields
    is_remote = models.BooleanField(default=False)
    capacity = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)

    # Location fields
    location = models.CharField(max_length=255, default='Remote')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)    

    class Meta:
        ordering = ['-date', 'start_time']
    
    def __str__(self):
        return f"{self.subject} - {self.date} ({self.tutor.username}"
    
    def seats_taken(self):
        return self.requests.filter(status="approved").count()

    def is_full(self):
        return self.seats_taken() >= self.capacity


class SessionRequest(models.Model):
    STATUS = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("declined", "Declined"),
        ("canceled", "Canceled"),
    ]
    session = models.ForeignKey(TutoringSession, on_delete=models.CASCADE, related_name="requests")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="session_requests")
    note = models.TextField(blank=True)
    status = models.CharField(max_length=16, choices=STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("session", "student")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.student.username} -> {self.session} [{self.status}]"