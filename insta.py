import instaloader

insta = instaloader.Instaloader()
profile_name = input(str("Nome do Perfil: "))


try:
    profile = instaloader.Profile.from_username(insta.context, profile_name)
except:
    print("O perfil não existe!")


for post in profile.get_posts():
    insta.download_post(post, target=profile.username)
