from django.db import models



class Articles(models.Model):
    title = models.CharField('Заголовок', max_length = 50)
    anons = models.CharField('Анонс', max_length = 250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.anons
    def __str__(self):   
        return self.full_text
    
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'