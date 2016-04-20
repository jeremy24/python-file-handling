

from config import init_config

# load the config values
init_config()

from process_data import handle_orders
from process_data import handle_tests

handle_orders()
handle_tests()
