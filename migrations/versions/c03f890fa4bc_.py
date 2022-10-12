"""empty message

Revision ID: c03f890fa4bc
Revises: 
Create Date: 2022-10-12 15:25:43.004454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c03f890fa4bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('short_urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=500), nullable=False),
    sa.Column('short_id', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('short_urls')
    # ### end Alembic commands ###
