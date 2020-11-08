# -------------------------------------------------------------------------------------------------
#  Copyright (C) 2015-2020 Nautech Systems Pty Ltd. All rights reserved.
#  https://nautechsystems.io
#
#  Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
#  You may not use this file except in compliance with the License.
#  You may obtain a copy of the License at https://www.gnu.org/licenses/lgpl-3.0.en.html
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------------------------

import unittest

from nautilus_trader.backtest.loaders import InstrumentLoader
from nautilus_trader.execution.base import ExecutionCacheFacade
from nautilus_trader.model.enums import AccountType
from nautilus_trader.model.identifiers import AccountId
from nautilus_trader.model.identifiers import ClientOrderId
from nautilus_trader.model.identifiers import Symbol
from nautilus_trader.model.identifiers import PositionId
from nautilus_trader.model.identifiers import Venue


FXCM = Venue("FXCM")
USDJPY_FXCM = InstrumentLoader.default_fx_ccy(Symbol('USD/JPY', FXCM))
AUDUSD_FXCM = InstrumentLoader.default_fx_ccy(Symbol('AUD/USD', FXCM))


class ExecutionCacheFacadeTests(unittest.TestCase):

    def setUp(self):
        # Fixture Setup

        self.facade = ExecutionCacheFacade()

    def test_account_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.account, AccountId("FXCM", "000", AccountType.DEMO))

    def test_account_for_venue_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.account_for_venue, FXCM)

    def test_account_id_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.account_id, FXCM)

    def test_order_ids_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.order_ids)

    def test_order_working_ids_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.order_working_ids)

    def test_order_completed_ids_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.order_completed_ids)

    def test_position_ids_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.position_ids)

    def test_position_open_ids_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.position_open_ids)

    def test_position_closed_ids_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.position_closed_ids)

    def test_strategy_ids_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.strategy_ids)

    def test_order_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.order, ClientOrderId("O-123456"))

    def test_orders_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.orders)

    def test_orders_working_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.orders_working)

    def test_orders_completed_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.orders_completed)

    def test_order_exists_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.order_exists, ClientOrderId("O-123456"))

    def test_is_order_working_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.is_order_working, ClientOrderId("O-123456"))

    def test_is_order_completed_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.is_order_completed, ClientOrderId("O-123456"))

    def test_orders_total_count_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.orders_total_count)

    def test_orders_working_count_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.orders_working_count)

    def test_orders_completed_count_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.orders_completed_count)

    def test_position_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.position, PositionId("P-123456"))

    def test_positions_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.positions)

    def test_positions_open_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.positions_open)

    def test_positions_closed_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.positions_closed)

    def test_position_exists_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.position_exists, PositionId("P-123456"))

    def test_is_position_open_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.is_position_open, PositionId("P-123456"))

    def test_is_position_closed_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.is_position_closed, PositionId("P-123456"))

    def test_positions_total_count_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.orders_total_count)

    def test_positions_open_count_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.positions_open_count)

    def test_positions_completed_count_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.positions_closed_count)

    def test_strategy_id_for_order_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.strategy_id_for_order, ClientOrderId("O-123456"))

    def test_strategy_id_for_position_when_not_implemented_raises_exception(self):
        self.assertRaises(NotImplementedError, self.facade.strategy_id_for_position, PositionId("P-123456"))
