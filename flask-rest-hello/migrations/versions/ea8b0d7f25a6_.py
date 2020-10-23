"""empty message

Revision ID: ea8b0d7f25a6
Revises: 
Create Date: 2020-10-23 10:10:18.928163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea8b0d7f25a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.Column('role', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.Column('role', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('business_legal_name', sa.String(length=150), nullable=True),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.Column('card_name', sa.String(length=150), nullable=True),
    sa.Column('card_number', sa.Integer(), nullable=True),
    sa.Column('cvv', sa.Integer(), nullable=True),
    sa.Column('month', sa.String(length=50), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=True),
    sa.Column('comuna', sa.String(length=100), nullable=True),
    sa.Column('region', sa.String(length=100), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('business_id'),
    sa.UniqueConstraint('business_legal_name')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_number', sa.Integer(), nullable=True),
    sa.Column('payment_id', sa.Text(), nullable=True),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('sale_tax', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_number')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(length=600), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sku_id')
    )
    op.create_table('productorder',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productorder')
    op.drop_table('product')
    op.drop_table('order')
    op.drop_table('information')
    op.drop_table('supplier')
    op.drop_table('client')
    # ### end Alembic commands ###