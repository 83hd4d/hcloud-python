import datetime
from datetime import timezone

from hcloud.firewalls.domain import Firewall


class TestFirewall:
    def test_created_is_datetime(self):
        firewall = Firewall(id=1, created="2016-01-30T23:50+00:00")
        assert firewall.created == datetime.datetime(
            2016, 1, 30, 23, 50, tzinfo=timezone.utc
        )
