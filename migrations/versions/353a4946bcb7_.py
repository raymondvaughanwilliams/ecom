"""empty message

Revision ID: 353a4946bcb7
Revises: 0d399c5bbbae
Create Date: 2022-12-23 10:29:49.446040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '353a4946bcb7'
down_revision = '0d399c5bbbae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('threads', schema=None) as batch_op:
        batch_op.add_column(sa.Column('anonymous', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('threads', schema=None) as batch_op:
        batch_op.drop_column('anonymous')

    # ### end Alembic commands ###
