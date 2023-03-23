# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import pytest

from pci_get_input_values import verify

def expected():
    return {
        "filter_name": "SHARR_Filter_PCI_321_Finding_CW1_RootAccountUsage",
        "filter_pattern": '{$.userIdentity.type="Root" && $.userIdentity.invokedBy NOT EXISTS && $.eventType !="AwsServiceEvent"}',
        "metric_name": "SHARR_PCI_321_Finding_CW1_RootAccountUsage",
        "metric_value": 1,
        "alarm_name": "SHARR_Alarm_PCI_321_Finding_CW1_RootAccountUsage",
        "alarm_desc": "Alarm for PCI finding CW.1 RootAccountUsage",
        "alarm_threshold": 1
    }

def test_verify():
    assert verify({'ControlId': 'PCI.CW.1'}, {}) == expected()
