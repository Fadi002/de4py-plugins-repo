from plugins.plugins import DeobfuscatorPlugin
import re

class DeobfuscatorExample(DeobfuscatorPlugin):
    def __init__(self):
        super().__init__(
            plugin_name="deobfuscator",
            creator="creator",
            link="https://github.com/Fadi002/de4py-plugins-repo/deobfuscators/example1.py",
            regex=re.compile(r'regex'),
            deobfuscator_function=self.deobfuscator_function
        )

    def deobfuscator_function(self, file_path) -> str:
        ...
