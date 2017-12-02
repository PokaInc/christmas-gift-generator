import json
import random
from collections import namedtuple

Object = namedtuple(field_names=['determiner', 'object'], typename='Object')

objects = [
    Object('A', 'Star Wars Mug'),
    Object('A', 'Mickey Mouse Toaster'),
    Object('Some', 'Socks'),
    Object('A', 'Cup of tea'),
    Object('A', 'Pack of Bacon'),
    Object('A', 'Sweater'),
    Object('A', 'Cat'),
    Object('A', 'Waffle maker'),
    Object('A', 'Robot vacuum cleaner'),
    Object('A', 'Harry Potter Scarf'),
    Object('A', 'Ring'),
    Object('A', 'String'),
    Object('A', 'Hamster'),
    Object('A', 'Macbook'),
    Object('A', 'Ghost'),
    Object('A', 'Anaconda'),
    Object('A', 'Dwarf'),
    Object('A', 'Mathieu Marcotte BubbleHead'),
]

adjectives = [
    'Crazy',
    'Cool',
    'Funny-looking',
    'Sweet',
    'Ugly',
    'Disturbing',
    'Awesome',
    'Scary',
    'Unfunny',
    'Useless',
    'Out of control',
    'Huge',
    'Long',
    'Small',
    'Tiny',
    'Splendid',
    'Expensive',
    'Unique',
    'Precious',
]


def generate_gift_idea():
    obj = random.choice(objects)
    adjective = random.choice(adjectives)

    return f'{obj.determiner} {adjective.lower()} {obj.object}'


def handler(event, context):
    gift_idea_count = random.randint(2, 6)
    gift_ideas = [generate_gift_idea() for _ in range(gift_idea_count)]

    return {
        "statusCode": 200,
        "body": json.dumps({
            'gift_ideas': gift_ideas
        })
    }
