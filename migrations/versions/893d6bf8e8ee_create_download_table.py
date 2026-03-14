"""create downloads table

Revision ID: a3f812bc9e21
Revises: d910295cd4bd
Create Date: 2026-03-14 16:00:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


revision: str = 'a3f812bc9e21'
down_revision: Union[str, Sequence[str], None] = 'd910295cd4bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "downloads",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("telegram_id", sa.String(), sa.ForeignKey("users.telegram_id", ondelete="CASCADE"), nullable=False),
        sa.Column("platform", sa.String(), nullable=False),
        sa.Column("media_type", sa.String(), nullable=False),
        sa.Column("url", sa.String(), nullable=False),
        sa.Column("downloaded_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_downloads_telegram_id", "downloads", ["telegram_id"])


def downgrade() -> None:
    op.drop_index("ix_downloads_telegram_id", table_name="downloads")
    op.drop_table("downloads")