import argparse
import sys
import yaml
import os
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(description="Template Terraform files")
parser.add_argument("varsfile", type=str)
parser.add_argument("indir", type=str)
parser.add_argument("outdir", type=str)

args = parser.parse_args()

variables = {}
with open(args.varsfile, 'r') as stream:
    try:
        variables = yaml.load(stream)
    except Exception as e:
        print("Error loading/parsing variables: {}".format(e.message))
        sys.exit(1)

if not os.path.exists(args.outdir):
    os.mkdir(args.outdir)

env = Environment(
    loader=FileSystemLoader(args.indir),
    trim_blocks=True,
)

for template in env.list_templates():
    path = os.path.join(args.outdir, os.path.splitext(template)[0]+'.tf')
    with open(path, 'w') as stream:
        stream.write(env.get_template(template).render(variables))

sys.exit(0)
