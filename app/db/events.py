from datetime import datetime, UTC
from sqlalchemy import event
from .base_table import BaseTableMixin


@event.listens_for(BaseTableMixin, 'before_update', propagate=True)
def timestamp_before_update(mapper, connection, target):
    target.updated_at = datetime.now(UTC)
