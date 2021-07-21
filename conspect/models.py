from django.db.models import *



class SubjectModel(Model):
    name = CharField(max_length=255, unique=True, verbose_name='Название предмета')
    author = CharField(max_length=255, verbose_name='Автор', blank=True, null=True)

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class StructureComponentModel(Model):
    subject = ForeignKey(SubjectModel, on_delete=CASCADE,
                         verbose_name='Предмет', related_name='structure_components')
    name = CharField(max_length=255, verbose_name='Название ')
    author = CharField(max_length=255, verbose_name='Автор')

    class Meta:
        verbose_name = 'Структурный компонент'
        verbose_name_plural = 'Структурные компоненты'

    def __str__(self):
        return f'{self.name}'


class AnswerModel(Model):
    structure_component = ForeignKey(StructureComponentModel, on_delete=CASCADE,
                                     verbose_name='Структурный компонент', related_name='answers')
    content = TextField(verbose_name='Вариант')
    author = CharField(max_length=255, verbose_name='Автор')

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return f'{self.content}'



class ConspectModel(Model):
    name = CharField(max_length=255, verbose_name='Название', default='Noname')
    owner = CharField(max_length=255, blank=True, verbose_name='Автор')
    answers = ManyToManyField(AnswerModel, verbose_name='Ответы', related_name='conspects')
    date_created = DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Конспект'
        verbose_name_plural = 'Конспекты'
        ordering = ('date_created',)

    def __str__(self):
        return f'Конспект: {self.name}  Автор: {self.owner} Дата создания: {self.date_created}'


class FooterInfoModel(Model):
    requisites = TextField(verbose_name='реквизиты')
    contacts = TextField(verbose_name='контакты')
    about = TextField(verbose_name='О сайте')

    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'

    def __str__(self):
        return f'информация "контакты/о сайте" редактируется здесь..'


