"""Init

Revision ID: 257ce2735405
Revises: 
Create Date: 2020-08-03 15:58:54.398839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '257ce2735405'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('check_in', sa.Time(), nullable=True),
    sa.Column('check_out', sa.Time(), nullable=True),
    sa.Column('break_in', sa.Time(), nullable=True),
    sa.Column('break_out', sa.Time(), nullable=True),
    sa.Column('method', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_attendance_date'), 'attendance', ['date'], unique=False)
    op.create_index(op.f('ix_attendance_method'), 'attendance', ['method'], unique=False)
    op.create_index(op.f('ix_attendance_staff_id'), 'attendance', ['staff_id'], unique=False)
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('ip', sa.String(length=15), nullable=True),
    sa.Column('mac', sa.String(length=17), nullable=True),
    sa.Column('method', sa.String(length=5), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_staff_ip'), 'staff', ['ip'], unique=True)
    op.create_index(op.f('ix_staff_mac'), 'staff', ['mac'], unique=True)
    op.create_index(op.f('ix_staff_method'), 'staff', ['method'], unique=False)
    op.create_index(op.f('ix_staff_name'), 'staff', ['name'], unique=True)
    op.create_index(op.f('ix_staff_staff_id'), 'staff', ['staff_id'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_staff_staff_id'), table_name='staff')
    op.drop_index(op.f('ix_staff_name'), table_name='staff')
    op.drop_index(op.f('ix_staff_method'), table_name='staff')
    op.drop_index(op.f('ix_staff_mac'), table_name='staff')
    op.drop_index(op.f('ix_staff_ip'), table_name='staff')
    op.drop_table('staff')
    op.drop_index(op.f('ix_attendance_staff_id'), table_name='attendance')
    op.drop_index(op.f('ix_attendance_method'), table_name='attendance')
    op.drop_index(op.f('ix_attendance_date'), table_name='attendance')
    op.drop_table('attendance')
    # ### end Alembic commands ###