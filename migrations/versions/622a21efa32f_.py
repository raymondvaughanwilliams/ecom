"""empty message

Revision ID: 622a21efa32f
Revises: 9a1fb05b1047
Create Date: 2023-03-06 00:02:00.520979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '622a21efa32f'
down_revision = '9a1fb05b1047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_review_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_review'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    # ### end Alembic commands ###
