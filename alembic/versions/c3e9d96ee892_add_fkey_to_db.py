"""add fkey to db

Revision ID: c3e9d96ee892
Revises: 7fb9d89afce5
Create Date: 2026-02-26 00:34:29.143410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3e9d96ee892'
down_revision: Union[str, Sequence[str], None] = '7fb9d89afce5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'products',
        sa.Column('o-user_id', sa.Integer(), nullable=True)
    )
    op.create_foreign_key('fk_user_product', 'products', 'users', ['o-user_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('fk_user_product', 'products', type_='foreignkey')
    op.drop_column('products', 'o-user_id')
    pass
