"""Initial migration

Revision ID: 73797bd03e9f
Revises: 
Create Date: 2024-10-14 22:33:05.105120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73797bd03e9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('profile_image', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('difficulty', sa.String(length=10), nullable=False),
    sa.Column('origin', sa.String(length=100), nullable=True),
    sa.Column('ingredients', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=120), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe')
    op.drop_table('user')
    # ### end Alembic commands ###