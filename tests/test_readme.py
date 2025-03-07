import os
import re

from django.conf import settings


class TestReadme:

    def test_readme(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "README.md")}', 'r') as f:
                readme = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что добавили файл README.md'

        re_str = r'https:\/\/github\.com\/[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+\/workflows\/[-a-zA-Z0-9()%_+]+\/badge\.svg'

        assert re.search(
            re_str, readme), 'Проверьте, что добавили бейдж о статусе работы workflow в файл README.md'
