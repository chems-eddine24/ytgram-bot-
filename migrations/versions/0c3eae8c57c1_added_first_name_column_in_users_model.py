"""added first_name column in users model

Revision ID: 0c3eae8c57c1
Revises: a3f812bc9e21
Create Date: 2026-03-16 00:09:52.753067

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c3eae8c57c1'
down_revision: Union[str, Sequence[str], None] = 'a3f812bc9e21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users",
                  column=sa.Column("first_name", sa.String, nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users",
                   column_name="first_name")
