# -*- coding: utf-8 -*-
"""
* order list question example
"""
from __future__ import print_function, unicode_literals

from PyInquirer import prompt, print_json

from examples import custom_style_2


questions = [
    {
        'type': 'list_order',
        'name': 'size',
        'message': 'What size do you need?',
        'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
    },
    {
        'type': 'list_order',
        'name': 'size2',
        'message': 'What size do you need?',
        'choices': ['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
        'target': 3,
    },
]

answers = prompt.prompt(questions, style=custom_style_2)
print_json(answers)
