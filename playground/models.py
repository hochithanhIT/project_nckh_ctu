import os
from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class diagnose(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/')
    labels = models.FileField(upload_to='labels/')
    filename = models.CharField(max_length=255, unique=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Save original file names
        new_image_name = os.path.basename(self.images.name)
        new_label_name = os.path.splitext(new_image_name)[0] + '.txt'

        if os.path.basename(self.labels.name) != new_label_name:
            old_label_path = self.labels.path
            new_label_path = os.path.join(default_storage.location, 'labels', new_label_name)
            
            # Rename the label file
            if default_storage.exists(old_label_path):
                # Move the file to the new location with the new name
                default_storage.save(new_label_path, default_storage.open(old_label_path))
                default_storage.delete(old_label_path)

                # Update the label field with the new name
                self.labels.name = new_label_name

            # Save again to apply the changes
            super().save(*args, **kwargs)

    def __str__(self):
        return self.images.name