# -*- coding: utf-8 -*-
from unittest.mock import MagicMock, patch

from chaosoci.compute.actions import stop_instance


@patch('chaosoci.compute.actions.oci_client', autospec=True)
def test_stop_instance(oci_client):
    client = MagicMock()
    oci_client.return_value = client
    inst_id = "i-1234567890abcdef0"
    action = "SOFTSTOP"
    stop_instance(inst_id, action)
    client.instance_action.assert_called_with(instance_id=inst_id,
                                              action=action)