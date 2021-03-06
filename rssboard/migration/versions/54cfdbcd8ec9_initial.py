"""initial

Revision ID: 54cfdbcd8ec9
Revises: None
Create Date: 2014-04-13 19:46:03.313595

"""

# revision identifiers, used by Alembic.
revision = '54cfdbcd8ec9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('feeds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('source', sa.String(length=240), nullable=False),
    sa.Column('scheme', sa.Enum('rss'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=60), nullable=False),
    sa.Column('author', sa.String(length=240), nullable=True),
    sa.Column('link', sa.String(length=240), nullable=True),
    sa.Column('summary', sa.String(length=240), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('content_type', sa.String(length=60), nullable=True),
    sa.Column('posted_at', sa.DateTime(), nullable=False),
    sa.Column('visit', sa.Integer(), nullable=False),
    sa.Column('up', sa.Integer(), nullable=False),
    sa.Column('down', sa.Integer(), nullable=False),
    sa.Column('feed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['feed_id'], ['feeds.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('feeds')
    op.drop_table('users')
    ### end Alembic commands ###
