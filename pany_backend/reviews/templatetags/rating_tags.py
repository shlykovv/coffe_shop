from django import template


register = template.Library()


# @register.filter
# def rating_to_percent(rating: str):
#     try:
#         rating = float(rating)
#     except (TypeError, ValueError):
#         rating = 0
    
    
#     full_stars = int(rating)
#     half_star = rating - full_stars >= 0.5
#     empty_stars = 5 - full_stars - int(half_star)
    
#     stars_html = '<i class="fas fa-star"></i>' * full_stars
#     if half_star:
#         stars_html += '<i class="fas fa-star-half-alt"></i>'
#     return stars_html


@register.filter
def rating_to_percent(rating):
    try:
        rating = float(rating)
    except (TypeError, ValueError):
        rating = 0

    full_stars = int(rating)
    half_star = rating - full_stars >= 0.5
    empty_stars = 5 - full_stars - int(half_star)

    stars_html = '<i class="fas fa-star text-yellow-500"></i>' * full_stars
    if half_star:
        stars_html += '<i class="fas fa-star-half-alt text-yellow-500"></i>'
    stars_html += '<i class="far fa-star text-gray-400"></i>' * empty_stars

    return stars_html
