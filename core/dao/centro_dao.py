from core.models import Centro


def get_centros():
    return Centro.objects.all()


def get_centro_by_id(id):
    return Centro.objects.get(id_unidade=id)


def get_ceres():
    id_ceres = 1482
    return get_centro_by_id(id_ceres)
