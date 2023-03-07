"""empty message

Revision ID: 5286af681b46
Revises: af93a4de669e
Create Date: 2023-03-06 00:46:27.136500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5286af681b46'
down_revision = 'af93a4de669e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_review')
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('vendor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_review_vendor_id_users'), 'users', ['vendor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_review_vendor_id_users'), type_='foreignkey')
        batch_op.drop_column('vendor_id')
        batch_op.drop_column('date')

    op.create_table('_alembic_tmp_review',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('text', sa.VARCHAR(length=255), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('vendor_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_review_user_id_users'),
    sa.ForeignKeyConstraint(['vendor_id'], ['users.id'], name='fk_review_vendor_id_users'),
    sa.PrimaryKeyConstraint('id', name='pk_review')
    )
    # ### end Alembic commands ###