"""Initial migration

Revision ID: 531f29ddf15f
Revises: 
Create Date: 2022-01-20 13:05:16.384671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '531f29ddf15f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guest_group', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('attendance', sa.String(), nullable=True),
    sa.Column('menu', sa.String(), nullable=True),
    sa.Column('transportation', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guest')
    # ### end Alembic commands ###
