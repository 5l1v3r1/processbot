"""changes

Revision ID: cbbd30b1eb1b
Revises: 6d5e679817cf
Create Date: 2019-04-04 19:21:41.464555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbbd30b1eb1b'
down_revision = '6d5e679817cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('process_doc', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('process_doc', 'iduh')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('process_doc', sa.Column('iduh', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('process_doc', 'id')
    # ### end Alembic commands ###