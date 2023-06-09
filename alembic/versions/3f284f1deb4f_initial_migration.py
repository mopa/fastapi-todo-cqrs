"""initial migration

Revision ID: 3f284f1deb4f
Revises:
Create Date: 2023-03-20 23:22:25.560710

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3f284f1deb4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
        sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column('completed',
                  sa.BOOLEAN(),
                  server_default=sa.text('false'),
                  autoincrement=False,
                  nullable=False),
        sa.Column('created_at',
                  postgresql.TIMESTAMP(),
                  server_default=sa.text('CURRENT_TIMESTAMP'),
                  autoincrement=False,
                  nullable=False),
        sa.Column('updated_at',
                  postgresql.TIMESTAMP(),
                  server_default=sa.text('CURRENT_TIMESTAMP'),
                  autoincrement=False,
                  nullable=False),
        sa.PrimaryKeyConstraint('id', name='todos_pkey')
        )
    op.create_index(op.f("ix_todos_id"), "todos", ["id"], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_todos_id"), table_name="todos")
    op.drop_table("todos")
    # ### end Alembic commands ###
