import yaml

def read_yaml_data(filename):
    with open(f'{filename}.yaml','r') as f:
        output = yaml.safe_load(f)
        print(output)
    return output

read_yaml_data("credentials")
