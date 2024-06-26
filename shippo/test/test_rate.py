# -*- coding: utf-8 -*-
import unittest

from mock import patch

import shippo
from shippo.test.helper import (
    create_mock_shipment,
    ShippoTestCase
)

from shippo.test.helper import shippo_vcr


class RateTests(ShippoTestCase):
    request_client = shippo.http_client.RequestsClient

    def setUp(self):
        super(RateTests, self).setUp()

        def get_http_client(*args, **kwargs):
            return self.request_client(*args, **kwargs)

        self.client_patcher = patch(
            'shippo.http_client.new_default_http_client')

        client_mock = self.client_patcher.start()
        client_mock.side_effect = get_http_client

    def tearDown(self):
        super(RateTests, self).tearDown()

        self.client_patcher.stop()

    @shippo_vcr.use_cassette(cassette_library_dir='shippo/test/fixtures/rate')
    def test_retrieve(self):
        shipment = create_mock_shipment()
        rates = shippo.Shipment.get_rates(
            shipment.object_id, asynchronous=False)
        rate = rates.results[0]
        retrieve = shippo.Rate.retrieve(rate.object_id)
        self.assertEqual(rate, retrieve)

    @shippo_vcr.use_cassette(cassette_library_dir='shippo/test/fixtures/rate')
    def test_invalid_retrieve(self):
        self.assertRaises(shippo.error.APIError,
                          shippo.Rate.retrieve, 'EXAMPLE_OF_INVALID_ID')


if __name__ == '__main__':
    unittest.main()
