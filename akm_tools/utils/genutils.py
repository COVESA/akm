import yaml


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 1:
            super().write_line_break()


class YamlCustomDumper:
    def dumps(dictToDump):
        yamlString = yaml.dump(
            dictToDump,
            default_flow_style=False,
            sort_keys=False,
            width=120,
            Dumper=NoAliasDumper,
        )
        return yamlString

    def dump(dictToDump, fileHandle):
        yaml.dump(
            dictToDump,
            fileHandle,
            default_flow_style=False,
            sort_keys=False,
            width=120,
            Dumper=NoAliasDumper,
        )
