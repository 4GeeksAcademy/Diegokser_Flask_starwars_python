"""empty message

Revision ID: 10f98b53315a
Revises: 8e69bbf9cc64
Create Date: 2023-06-06 21:58:22.377627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10f98b53315a'
down_revision = '8e69bbf9cc64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('appearances', sa.String(length=50), nullable=False),
    sa.Column('locations', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('dimensions', sa.String(length=50), nullable=True),
    sa.Column('species', sa.String(length=50), nullable=True),
    sa.Column('weapons', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('appearances', sa.String(length=150), nullable=False),
    sa.Column('affiliations', sa.String(length=150), nullable=True),
    sa.Column('climate', sa.String(length=150), nullable=True),
    sa.Column('terrain', sa.String(length=150), nullable=True),
    sa.Column('creature', sa.String(length=150), nullable=True),
    sa.Column('species', sa.String(length=150), nullable=True),
    sa.Column('vehicles', sa.String(length=150), nullable=True),
    sa.Column('weapons', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('name')
    )
    op.create_table('people_favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('people_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets_favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets_favorite')
    op.drop_table('people_favorite')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###