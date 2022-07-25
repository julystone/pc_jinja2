import os
from jinja2 import Environment, FileSystemLoader


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    env = Environment(loader=FileSystemLoader(path or './'))
    return env.get_template(filename).render(**kwargs)


if __name__ == '__main__':
    temp={'x1_flag': True}
    path = 'template.jinja'
    base_import = 1
    x1_flag = True
    chap = "A"
    CampaignMap = "s1"
    class MapBase:
        def __init__(self):
            self.chap = 'C'
            self.shape = 11
            self.camera_data = 22
    MapData = MapBase()
    res = render(path, **locals())
    print(res)
    x = 2
    y = 3
