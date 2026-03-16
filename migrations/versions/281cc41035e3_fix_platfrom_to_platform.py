"""fix platfrom to platform 

Revision ID: 281cc41035e3
Revises: 0c3eae8c57c1
Create Date: 2026-03-16 22:51:34.241697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '281cc41035e3'
down_revision: Union[str, Sequence[str], None] = '0c3eae8c57c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column("users",
                    "platfrom",
                    new_column_name="platform")


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column("users",
                    "platform",
                    new_column_name="platfrom")
