from django.db import models
from django.conf import settings   # ✅ இதை use பண்ணணும்

class Leave(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ FIX

    reason = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return str(self.user) + " - " + self.status