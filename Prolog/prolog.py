from pyswip import Prolog
from pathlib import Path

current_path = Path(__file__)
csv_path = current_path / "csv"

prolog = Prolog()

prolog.consult(f"{current_path.as_posix()}/../beer.pl")

# --------- get data from KB --------- #
def getBeers():
    beers = list(prolog.query("beer(Beer_id, Beer_name)"))
    return beers

def getStyles():
    styles = list(prolog.query("style(Style_id, Style_name)"))
    return styles

def getBeerStyle():
    beer_style = list(prolog.query("beerstyle(Beer_id, Style_id)"))
    return beer_style

# --------- rules related to beers --------- #
def whatBeerID(beer_name):
    id = prolog.query(f"what_beer_id('{beer_name}')")
    return id

def whatBeerName(beer_id):
    name = prolog.query(f"what_beer_name('{beer_id})")
    return name

def whatBeerAbv(beer_name):
    abv = prolog.query(f"what_beer_abv('{beer_name}')")
    return abv

def whatBeerStyle(beer_name):
    style = prolog.query(f"what_beer_style('{beer_name}')")
    return style

def whatBeerReview(beer_name):
    review = prolog.query(f"what_beer_review('{beer_name}')")
    return review

# what_beer_mouthfeel, what_beer_taste, what_beer_flavour unuseful...

# --------- rules related to styles --------- #
def whatStyleID(style_name):
    style_id = prolog.query(f"what_style_id('{style_name}')")
    return style_id

def whatStyleName(style_id):
    style_name = prolog.query(f"what_style_name('{style_id}')")
    return style_name

def whatStyleMouthfeel(style_name):
    style_mouthfeel = list(prolog.query(f"what_style_mouthfeel('{style_name}')"))
    return style_mouthfeel

def whatStyleTaste(style_name):
    style_taste = list(prolog.query(f"what_style_taste('{style_name}')"))
    return style_taste

def whatStyleFlavour(style_name):
    style_flavour = list(prolog.query(f"what_style_flavour('{style_name}')"))
    return style_flavour

# --------- simple classifier --------- #
def userTaste(sweet, bitter, sour, salty):
    list(prolog.query(f"dist_style_taste({sweet},{bitter},{sour},{salty})"))
    user_taste = list(prolog.query("order_by([asc(Value)], dist_taste(Style,Value))"))
    return user_taste

def userMouthfeel(astringency, body, alcohol):
    list(prolog.query(f"dist_style_mouthfeel({astringency},{body},{alcohol})"))
    user_mouthfeel = list(prolog.query("order_by([asc(Value)], dist_mouthfeel(Style,Value))"))
    return user_mouthfeel

def userFlavour(fruity, hoppy, malty, spices):
    list(prolog.query(f"dist_style_flavour({fruity},{hoppy},{malty},{spices})"))
    user_flavour = list(prolog.query("order_by([asc(Value)], dist_flavour(Style,Value))"))
    return user_flavour