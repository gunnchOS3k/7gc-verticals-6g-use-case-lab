from gunnchos_7gc_verticals.kpi_mapping import map_to_repos

def test_map():
    assert 'digital-twin' in map_to_repos('health')
