""" 
 curl -X POST -d "username=user1&&password=firstuser" http://django-blog-api.herokuapp.com/api/auth/token

 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0NzQ5NDY4MjEsImVtYWlsIjoidXNlcjFAdXNlcjEuY29tIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJ1c2VyMSJ9.KFkWuxtizF5aPKxi87lHt7imAU_21Sigsd4KqPQPLYs


curl -X POST -d "username=user1&&email=user1@user1.com&&email2=user1@user1.com&&password=firstuser" http://django-blog-api.herokuapp.com/api/users/register/



curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0NzQ5NDY4MjEsImVtYWlsIjoidXNlcjFAdXNlcjEuY29tIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJ1c2VyMSJ9.KFkWuxtizF5aPKxi87lHt7imAU_21Sigsd4KqPQPLYs" -d "title=first article&&body=this is the first article" http://django-blog-api.herokuapp.com/api/articles/create/


 """
