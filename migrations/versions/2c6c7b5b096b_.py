"""empty message

Revision ID: 2c6c7b5b096b
Revises: 09171e213292
Create Date: 2022-06-29 22:41:09.272009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c6c7b5b096b'
down_revision = '09171e213292'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blocks', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_blocks_appearance_id_appearances'), 'appearances', ['appearance_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blocks', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_blocks_appearance_id_appearances'), type_='foreignkey')

    # ### end Alembic commands ###