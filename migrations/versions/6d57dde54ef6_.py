"""empty message

Revision ID: 6d57dde54ef6
Revises: 3804b0e9fd0e
Create Date: 2023-01-21 18:45:22.141285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d57dde54ef6'
down_revision = '3804b0e9fd0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('deliveries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('arrival_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('ticket', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('deliveries', schema=None) as batch_op:
        batch_op.drop_column('ticket')
        batch_op.drop_column('arrival_date')

    # ### end Alembic commands ###
