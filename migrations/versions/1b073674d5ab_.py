"""empty message

Revision ID: 1b073674d5ab
Revises: e9aa581266e2
Create Date: 2022-06-30 19:37:39.489357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b073674d5ab'
down_revision = 'e9aa581266e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('webfeatures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=140), nullable=False),
    sa.Column('wtext', sa.Text(), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_webfeatures'))
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('therapist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['therapist_id'], ['webfeatures.id'], name=op.f('fk_bookings_therapist_id_webfeatures')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bookings'))
    )
    op.drop_table('web_feature')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('web_feature',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=140), nullable=False),
    sa.Column('wtext', sa.TEXT(), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=True),
    sa.Column('type', sa.VARCHAR(length=100), nullable=True),
    sa.Column('email', sa.VARCHAR(length=40), nullable=True),
    sa.Column('city', sa.VARCHAR(length=50), nullable=True),
    sa.Column('phone', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('bookings')
    op.drop_table('webfeatures')
    # ### end Alembic commands ###