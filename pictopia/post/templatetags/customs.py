from datetime import datetime

from django import template

register = template.Library()


@register.filter(name='postedTime')
def postedTime(value: datetime):
    time = datetime.now()
    if time.date().year >= value.date().year:
        if time.date().month >= value.date().month:
            if time.date().day >= value.date().day:
                if time.hour >= value.hour:
                    if time.minute >= value.minute:
                        if time.second >= value.second:
                            return str(time.second - value.second) + ' seconds ago'
                        return str(time.minute - value.minute) + ' minutes ago'
                    return str(time.hour - value.hour) + ' hours ago'
                return str(time.date().day - value.date().day) + ' days ago'
            return str(time.date().month - value.date().month) + ' months ago'
        return str(time.date().year - value.date().year) + ' year ago'
