import jmespath

# модуль для удобства работы с данными json
d = {"foo": {"bar": "baz"}}
print(jmespath.search('foo.bar', d))

d = {"foo": {"bar": [{"name": "one"}, {"name": "two"}]}}
print(jmespath.search('foo.bar[*].name', d))