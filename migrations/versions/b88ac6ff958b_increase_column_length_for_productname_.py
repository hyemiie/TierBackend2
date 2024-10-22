"""Increase column length for productName, productImage, and productDesc

Revision ID: b88ac6ff958b
Revises: c98763b7ba46
Create Date: 2024-08-19 17:08:58.757373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b88ac6ff958b'
down_revision = 'c98763b7ba46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_products', schema=None) as batch_op:
        batch_op.alter_column('productName',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=80),
               existing_nullable=False)
        batch_op.alter_column('productImage',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=225),
               existing_nullable=False)
        batch_op.alter_column('productDesc',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=225),
               existing_nullable=False)
        batch_op.alter_column('productPrice',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=225),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cart_products', schema=None) as batch_op:
        batch_op.alter_column('productPrice',
               existing_type=sa.String(length=225),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('productDesc',
               existing_type=sa.String(length=225),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('productImage',
               existing_type=sa.String(length=225),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
        batch_op.alter_column('productName',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###