from django.db import models

class Animal:
    def __init__(self, name, color, sex):
        self.name = name
        self.color = color
        self.sex = sex
