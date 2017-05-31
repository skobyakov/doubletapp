from flask import render_template, abort, Blueprint, request, redirect, url_for
from .models import Event
import requests
import base64


event_page = Blueprint('event_page', __name__,
                       template_folder='templates',
                       static_folder='static')


def encode_to_base64(data):
    return base64.b64encode(data).decode('ascii')


def get_google_map(latitude, longitude, zoom, width, height):
    api_key = 'AIzaSyAf5F5cNRwizQpj0RODu_X1nPRKlN6YgNM'
    url = 'https://maps.googleapis.com/maps/api/staticmap'
    params = {
        'key' : api_key,
        'center' : '{},{}'.format(latitude, longitude),
        'zoom' : zoom,
        'size' : '{}x{}'.format(width, height),
        'format' : 'jpg',
        'markers' : '{},{}'.format(latitude, longitude),
    }
    response = requests.get(url, params=params)
    return encode_to_base64(response.content)


def extract_event_from_db(oid):
    e = Event.objects(pk=oid)
    if len(e) == 0:
        return dict()
    e = e[0]
    result = {
        'title': e.title,
        'organizer': e.organizer,
        'description': e.description,
        'what': e.what,
        'when': e.when,
        'call': e.call,
        'website': e.website,
        'logo': encode_to_base64(e.logo.read()),
        'location': e.location.split(', ')
    }
    result['map'] = get_google_map(*result['location'], 18, 750, 450)
    return result


@event_page.route('/<event_oid>/')
def event(event_oid):
    e = extract_event_from_db(event_oid)
    if len(e) == 0:
        abort(404)
    return render_template('event/event.html', params=e)