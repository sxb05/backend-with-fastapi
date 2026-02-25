"""create product table

Revision ID: 59e31ca66411
Revises: 
Create Date: 2026-02-24 23:44:52.767640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59e31ca66411'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.create_table('products', sa.Column('id', sa.Integer, primary_key=True),
                   sa.Column('name', sa.String, nullable=False))            
   



def downgrade() -> None:
    op.drop_table('products')
    pass
