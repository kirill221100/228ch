from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, TextAreaField, MultipleFileField
from wtforms.validators import DataRequired, Length, ValidationError

def num_of_files(form, field):
    if len(field.data) > 4:
        raise ValidationError('У вас больше 4-ёх картинок')
    else:
        list = []
        for i in field.data:
            list.append(len(i.read()))
            i.seek(0, 0)
            #i.tell()
        if sum(list) > 1097152:
            raise ValidationError('Больше 1-ого мегабайта')
    if len([i for i in field.data if 'jpg' not in str(i) and 'png' not in str(i) and 'jpeg' not in str(i)]) > 0 and 'application' not in str(field.data):
        raise ValidationError('Присутствует другой формат файла')

class ThreadForm(FlaskForm):
    text = TextAreaField('Текст', validators=[DataRequired(), Length(max=15000)])
    images = MultipleFileField('Картинки', validators=[num_of_files])
    submit = SubmitField('Отправить')
