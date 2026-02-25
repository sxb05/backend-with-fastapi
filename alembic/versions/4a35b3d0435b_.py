"""empty message

Revision ID: 4a35b3d0435b
Revises: 59e31ca66411
Create Date: 2026-02-25 23:48:02.530240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a35b3d0435b'
down_revision: Union[str, Sequence[str], None] = '59e31ca66411'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
