"""empty message

Revision ID: 5daa53fd8965
Revises: 41ed54de54e4
Create Date: 2022-07-19 00:26:51.612821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5daa53fd8965'
down_revision = '41ed54de54e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('journals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_journals_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_journals'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journals')
    # ### end Alembic commands ###