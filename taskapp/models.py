from django.db import models
from account.models import CustomUser


class TaskPost(models.Model):

    CATEGORY = (('science','科学'),
                ('IT','IT'),
                ('sports','スポーツ'),
                ('entertainment','エンタメ'),
                ('economy','経済'),
                ('international','国際'),
                ('domestic','国内'),
            )

    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )

    content = models.TextField(
        verbose_name='本文'
    )

    posted_at = models.DateField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    category = models.CharField(
        verbose_name='カテゴリ',
        max_length=50,
        choices=CATEGORY
    )


    def __str__(self):
        return self.title
    
    
class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(TaskPost, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # 同じユーザーが同じ投稿に複数回「いいね」できないようにする

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"