"""empty message

Revision ID: 0d399c5bbbae
Revises: 395df0feedd5
Create Date: 2022-12-23 00:31:31.435004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d399c5bbbae'
down_revision = '395df0feedd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('threads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_threads_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_threads'))
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('thread_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['thread_id'], ['threads.id'], name=op.f('fk_posts_thread_id_threads')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_posts_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_posts'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('threads')
    # ### end Alembic commands ###