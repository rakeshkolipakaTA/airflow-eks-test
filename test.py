import json 
import sys




def update_yaml(market,version):
    import yaml

    fname = "env/{}/deploy_config.yaml".format(market)

    stream = open(fname, 'r')
    data = yaml.load(stream.read(), Loader=yaml.FullLoader)
    data['app_version'] = version

    with open(fname, 'w') as yaml_file:
        yaml_file.write( yaml.dump(data, default_flow_style=False))


def get_update(version,markets):
    markets = markets.split(",")
    for market in markets:
        try:
            update_yaml(market,version)
        except Exception as e:
            print(e)

version = sys.argv[1]
markets = sys.argv[2]
get_update(version,markets)
