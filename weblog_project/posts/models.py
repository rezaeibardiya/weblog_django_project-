from django.db import models


class teacher(models.Model):
    name = models.CharField(max_length=40)
    subject = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class club(models.Model):
    club_name = models.CharField(max_length=40)
    club_mem_num = models.PositiveIntegerField()
    club_des = models.TextField()

    def __str__(self):
        return self.club_name


# Create your models here.
class students(models.Model):
    name =models.CharField()
    teacher = models.ForeignKey(teacher , on_delete=models.CASCADE)
    club = models.ManyToManyField(club , blank=True)

    
class image(models.Model):
    image_name =models.CharField()
    photo = models.ImageField(upload_to='recipes/', height_field='image_height', width_field='image_width')
    image_height = models.PositiveIntegerField()
    image_width = models.PositiveIntegerField()
    def __str__(self):
        return self.image_name
    
def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

