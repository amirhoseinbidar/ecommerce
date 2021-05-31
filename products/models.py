from django.db import models


class TemplateImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name

class TemplateTypeOne(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True, blank=True)
    head_image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    insta_link = models.URLField(null=True, blank=True)
    description_image = models.ImageField(null=True, blank=True)
    description_title = models.CharField(max_length=200, null=True, blank=True)
    description_detail = models.TextField(null=True, blank=True)

    template_path = 'temps/temp_type_one.html'


class TemplateTypeTwo(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True, blank=True)
    head_title = models.CharField(max_length=200, null=True, blank=True)
    head_sub_title = models.CharField(max_length=200, null=True, blank=True)
    head_image = models.ImageField(null=True, blank=True)
    about_me_title = models.CharField(max_length=200, null=True, blank=True)
    about_me_description = models.CharField(max_length=200, null=True, blank=True)
    ablility_1_title = models.CharField(max_length=200, null=True, blank=True)
    ablility_1_precent = models.IntegerField( null=True, blank=True)
    ablility_2_title = models.CharField(max_length=200, null=True, blank=True)
    ablility_2_precent = models.IntegerField( null=True, blank=True)
    ablility_3_title = models.CharField(max_length=200, null=True, blank=True)
    ablility_3_precent = models.IntegerField(null=True, blank=True)
    more_info_1_number = models.IntegerField(null=True, blank=True)
    more_info_1_text = models.CharField(max_length=200, null=True, blank=True)
    more_info_2_number = models.IntegerField(null=True, blank=True)
    more_info_2_text = models.CharField(max_length=200, null=True, blank=True)
    more_info_3_number = models.IntegerField(null=True, blank=True)
    more_info_3_text = models.CharField(max_length=200, null=True, blank=True)
    more_info_4_number = models.IntegerField(null=True, blank=True)
    more_info_4_text = models.CharField(max_length=200, null=True, blank=True)
    img_1 = models.ImageField(blank=True, null=True)
    img_2 = models.ImageField(blank=True, null=True)
    img_3 = models.ImageField(blank=True, null=True)
    img_4 = models.ImageField(blank=True, null=True)
    img_5 = models.ImageField(blank=True, null=True)
    img_6 = models.ImageField(blank=True, null=True)
    img_7 = models.ImageField(blank=True, null=True)
    img_8 = models.ImageField(blank=True, null=True)

    template_path = 'temps/temp_type_two.html'

