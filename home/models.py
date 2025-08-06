from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='blogpics/')
    text_1 = models.TextField(max_length=500,blank=True,null=True)
    picture_2 = models.ImageField(upload_to='blogpics/',blank=True,null=True)
    text_2 = models.TextField(max_length=500,blank=True,null=True)
    note_title = models.CharField(max_length=200,blank=True,null=True)
    mini_pic_1 = models.ImageField(upload_to='blogpics/',blank=True,null=True)
    mini_pic_2 = models.ImageField(upload_to='blogpics/',blank=True,null=True)
    mini_pic_3 = models.ImageField(upload_to='blogpics/',blank=True,null=True)
    final_note_title = models.CharField(max_length=200,blank=True,null=True)
    final_note_text = models.TextField(max_length=400,blank=True,null=True)

    def __str__(self):
        return self.title
    

class TableTitle(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='tabletitle')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class TableTitleInfo(models.Model):
    TableTitle = models.ForeignKey(TableTitle,on_delete=models.CASCADE,related_name='info')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='info',blank=True,null=True)
    info = models.CharField(max_length=100)

    def __str__(self):
        return self.info

class FinalNoteInfo(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='note')
    title = models.CharField(max_length=50)
    info = models.TextField(max_length=200)

    def __str__(self):
        return self.title