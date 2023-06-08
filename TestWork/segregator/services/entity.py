from segregator.models import Entity

def get_all_entities():
    return Entity.objects.all()

def fill_db():
    head_node = Entity(
        title="I. МКДЦ (как юрид. лицо)"
    )
    head_node.save()
    for title in ("1. Деятельность учреждения", "2. Документы общего назначения"):
        node = Entity(title=title, parent=head_node)
        node.save()