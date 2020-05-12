from unittest.mock import Mock
mock = Mock()
mock
import main
class TestGCFPyGCSSample(object):
    def test_hello_gcs_generic(self, capsys):
        event = {
            'bucket': 'some-bucket',
            'name': 'some-filename',
            'metageneration': 'some-metageneration',
            'timeCreated': '0',
            'updated': '0'
        }
        context = mock.MagicMock()
        context.event_id = 'some-id'
        context.event_type = 'gcs-event'
        main.hello_gcs_generic(event, context)
        out, _ = capsys.readouterr()
        assert 'some-bucket' in out
        assert 'some-id' in out
#With this main i dont have issues but dont run a test
#if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
#With this main i have issues but it read the test
if __name__ == '__main__':
    unittest.main()
