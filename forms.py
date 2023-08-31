from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Optional

#POS_Choices = [('all', 'All'), ('pronoun', 'Pronouns'), ('noun', 'Nouns'), ('verb', 'Verbs'), ('adjective', 'Adjectives'), ('preposition'), ('Prepositions'), ('adverb'), ('Adverbs'), ('misc'), ('Misc.')]

class contactForm(FlaskForm):
    #name = StringField('Name')
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


class filterForm(FlaskForm):
    search = StringField('', validators = [Optional()])
    partofspeech = SelectField('Part of Speech', choices=[('all', 'All'), ('pronoun', 'Pronouns'), ('noun', 'Nouns'), ('verb', 'Verbs'), ('adjective', 'Adjectives'), ('preposition'), ('Prepositions'), ('adverb'), ('Adverbs'), ('culture'), ('Misc.')], validators = [Optional()])
    submit = SubmitField("Go")

#class indexForm(FlaskForm):
    #search = StringField('')