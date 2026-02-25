"""add user table

Revision ID: 7fb9d89afce5
Revises: 4a35b3d0435b
Create Date: 2026-02-26 00:25:04.455315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fb9d89afce5'
down_revision: Union[str, Sequence[str], None] = '4a35b3d0435b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column(
            'created_at',
            sa.TIMESTAMP(),
            server_default=sa.text('now()'),
            nullable=False
        ),
        sa.UniqueConstraint('username'),
        sa.UniqueConstraint('email')
    )
                    

def downgrade() -> None:
    op.drop_table('users')
    pass
