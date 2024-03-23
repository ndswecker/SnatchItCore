import maps.maps_reference_data as REFERENCE_DATA


def stations(request):
    return {"stations": list(REFERENCE_DATA.SITE_LOCATIONS.keys())}
