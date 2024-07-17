import os

files = os.listdir('configlets')


for file in files:
    name, ext = file.split('.')
    print(f"  {name}: \"\u007b\u007b lookup('file', '../configlets/{name}-BASE.cfg') \u007d\u007d\"")



# for file in files:
#     name, ext = file.split('.')
#     print(f"  - fqdn: {name}")
#     print(f"    parentContainerName: Tenant")
#     print(f"    configlets:")
#     print(f"      - 'ATD-INFRA'")
#     print(f"      - '{name}'")


#   - fqdn: Edge10-BASE
#     parentContainerName: Tenant
#     configlets:
#         - 'ATD-INFRA'
#         - 'Edge10-BASE'