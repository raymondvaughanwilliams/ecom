"""empty message

Revision ID: e1741ce758bf
Revises: de6d0583e158
Create Date: 2022-12-13 20:06:28.108413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1741ce758bf'
down_revision = 'de6d0583e158'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('therapists')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('specialty', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('phone_number', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('biography', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('qualifications', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('years_of_experience', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('license_number', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('insurance_provider', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('platforms', sa.String(), nullable=True))
        batch_op.drop_index('ix_users_email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('ix_users_email', ['email'], unique=False)
        batch_op.drop_column('platforms')
        batch_op.drop_column('insurance_provider')
        batch_op.drop_column('license_number')
        batch_op.drop_column('years_of_experience')
        batch_op.drop_column('qualifications')
        batch_op.drop_column('biography')
        batch_op.drop_column('phone_number')
        batch_op.drop_column('specialty')

    op.create_table('therapists',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('specialty', sa.VARCHAR(), nullable=True),
    sa.Column('location', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), nullable=True),
    sa.Column('biography', sa.VARCHAR(), nullable=True),
    sa.Column('qualifications', sa.VARCHAR(), nullable=True),
    sa.Column('years_of_experience', sa.INTEGER(), nullable=True),
    sa.Column('license_number', sa.VARCHAR(), nullable=True),
    sa.Column('insurance_provider', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_therapists')
    )
    # ### end Alembic commands ###