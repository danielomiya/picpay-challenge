import pytest
from src.config import ConfigLoader

def test_configloader_reads_file(tmpdir):
    tmp_file = tmpdir / 'config.ini'
    tmp_file.write("""[DEFAULT]
any_key=I work
""")

    config = ConfigLoader()
    config.add_config(tmp_file.realpath())

    assert config.get_string('any_key') == 'I work'


def test_configloader_can_read_multiple_files(tmpdir):
    tmp_file1 = tmpdir / 'config1.ini'
    tmp_file2 = tmpdir / 'config2.ini'

    tmp_file1.write("""[DEFAULT]
key_a=5
""")

    tmp_file2.write("""[DEFAULT]
key_a=2
key_b=3
""")

    config = ConfigLoader().add_config(tmp_file1.realpath())

    assert config.get_string('key_a') == '5'
    assert config.get_string('key_b', default='>fallback<') == '>fallback<'

    config.add_config(tmp_file2.realpath())

    assert config.get_string('key_a') == '2'
