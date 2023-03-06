"""empty message

Revision ID: 1d5e39bc0c5f
Revises: a8ffba0df41a
Create Date: 2023-03-05 00:20:21.646602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d5e39bc0c5f'
down_revision = 'a8ffba0df41a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('certificate', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('parts', sa.String(length=250), nullable=True))
        batch_op.add_column(sa.Column('cars', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('cars')
        batch_op.drop_column('parts')
        batch_op.drop_column('certificate')

    # ### end Alembic commands ###
