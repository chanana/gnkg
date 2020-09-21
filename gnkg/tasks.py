from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task(name="add_two_numbers_task")
def add(x, y):
    return x + y


@app.task(name="multiply_two_numbers_task")
def mul(x, y):
    return x * y


@app.task(name="sum_many_numbers_task")
def xsum(numbers):
    return sum(numbers)
