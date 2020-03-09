# Copyright 2018 Carlos Dauden - Tecnativa <carlos.dauden@tecnativa.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    """Update database from previous versions, after updating module."""

    if not version:
        return
    cr = env.cr

    # update charge_bearer for all bank_payment_line
    cr.execute(
        "UPDATE bank_payment_line as l "
        "SET charge_bearer = ("
        "SELECT charge_bearer FROM account_payment_order as o "
        "WHERE o.id = l.order_id)")
