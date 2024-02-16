from random import choices
from django.core.management.base import BaseCommand
from myapp3.models import Author, Post


LOREM = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit. A accusantium aliquid animi'
         ' atque commodi debitis deleniti dolores eligendi excepturi explicabo fuga fugiat fugit '
         'incidunt inventore iste, labore laboriosam minima minus mollitia natus necessitatibus'
         ' neque nihil officia officiis optio perferendis quasi quibusdam quisquam quo, recusandae'
         ' sapiente tenetur ullam vel velit vero voluptas voluptates? Accusantium ad alias aliquid '
         'amet animi asperiores at atque, aut corporis delectus deleniti dolorem, eos est eveniet'
         ' ex ipsa itaque iure modi mollitia necessitatibus nihil nisi numquam odit placeat porro '
         'possimus quasi quibusdam quos, rem reprehenderit sequi sunt veniam vitae. Aliquid amet,'
         ' aspernatur cum eligendi et facere illo inventore ipsum, modi necessitatibus obcaecati '
         'quia vel veritatis. Accusamus at commodi doloremque harum illo in laborum natus quasi '
         'sed sunt! A accusantium aperiam atque beatae cumque debitis dolore doloremque doloribus'
         ' est facilis, harum ipsum laborum magnam maiores maxime minima nam natus nemo numquam '
         'obcaecati, officia omnis pariatur possimus quas quasi qui quod reprehenderit sapiente '
         'soluta temporibus unde veritatis vitae voluptatum! Ab accusamus ad alias assumenda at.')


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of users')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=' '.join((choices(text, k=64))),
                    author=author
                )
                post.save()
