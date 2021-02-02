# Copyright 2020 Camptocamp SA (http://www.camptocamp.com)
# Copyright 2021 ACSONE SA/NV (http://www.camptocamp.com)
# @author Simone Orsi <simahawk@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.addons.component.core import Component

from .common import CommonCase
from .common_misc import ScanAnythingTestMixin


class ScanAnythingCase(CommonCase, ScanAnythingTestMixin):
    def _get_test_handlers(self):
        class PartnerFinder(Component):
            _name = "shopfloor.scan.partner.handler"
            _inherit = "shopfloor.scan.anything.handler"

            record_type = "partner"

            def search(self, identifier):
                return (
                    self.env["res.partner"]
                    .sudo()
                    .search([("ref", "=", identifier)], limit=1)
                )

            @property
            def converter(self):
                return self._data.partner

            def schema(self):
                return self._schema._simple_record()

        class CurrencyFinder(Component):
            _name = "shopfloor.scan.currency.handler"
            _inherit = "shopfloor.scan.anything.handler"

            record_type = "currency"

            def search(self, identifier):
                return (
                    self.env["res.currency"]
                    .sudo()
                    .search([("name", "=", identifier)], limit=1)
                )

            @property
            def converter(self):
                return lambda record: record.jsonify(
                    self._data._simple_record_parser(), one=True
                )

            def schema(self):
                return self._schema._simple_record()

        return (PartnerFinder, CurrencyFinder)

    def test_scan(self):
        service = self._get_service()

        for finder_class in self._get_test_handlers():
            finder_class._build_component(service.work.components_registry)

        handlers = service._scan_handlers()
        self.assertEqual(len(handlers), 2)

        record = self.env.ref("base.res_partner_4").sudo()
        record.ref = "1234"
        rec_type = "partner"
        identifier = record.ref
        data = record.jsonify(("id", "name"), one=True)
        self._test_response_ok(rec_type, data, identifier)

        record = self.env.ref("base.EUR").sudo()
        rec_type = "currency"
        identifier = record.name
        data = record.jsonify(("id", "name"), one=True)
        self._test_response_ok(rec_type, data, identifier)

    def test_scan_error(self):
        self._test_response_ko("404-NOTFOUND")
