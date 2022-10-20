from unittest.mock import MagicMock, patch

import tools


# MOKOVANIE!!!!, simulujem data do testov aby som sa nemusel pripajat do databaz
# API system komunikovania medzi programom a datami

class TestTools:
    def test_load_nums_from_file(self):
        test_data = ['1, 1', '1.5, 0.5', '10, 100', '', '12', '1, 2, 3']
        expected = [(1, 1), (1.5, 0.5), (10, 100)]

        fake_api = MagicMock()  # fejkuje
        fake_api.get_data.return_value = test_data
        with patch('tools.API', fake_api):  # pracuje s fake API
            result = tools.load_nums_from_file()
            assert result == expected
