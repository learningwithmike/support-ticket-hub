from datetime import datetime
from app import db
from enum import Enum

class UserRole(Enum):
    """User role enumeration"""
    ADMIN = 'admin'
    AGENT = 'agent'
    USER = 'user'

class TicketStatus(Enum):
    """Ticket status enumeration"""
    OPEN = 'open'
    IN_PROGRESS = 'in_progress'
    ON_HOLD = 'on_hold'
    CLOSED = 'closed'
    RESOLVED = 'resolved'

class TicketPriority(Enum):
    """Ticket priority enumeration"""
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    CRITICAL = 'critical'

class User(db.Model):
    """User model"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120))
    role = db.Column(db.Enum(UserRole), default=UserRole.USER, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    created_tickets = db.relationship('Ticket', backref='creator', foreign_keys='Ticket.created_by', lazy=True)
    assigned_tickets = db.relationship('Ticket', backref='assignee', foreign_keys='Ticket.assigned_to', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Ticket(db.Model):
    """Ticket model"""
    __tablename__ = 'tickets'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(TicketStatus), default=TicketStatus.OPEN, nullable=False)
    priority = db.Column(db.Enum(TicketPriority), default=TicketPriority.MEDIUM, nullable=False)
    
    # Foreign keys
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    closed_at = db.Column(db.DateTime, nullable=True)
    
    # Relationships
    comments = db.relationship('Comment', backref='ticket', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Ticket {self.id}: {self.title}>'

class Comment(db.Model):
    """Comment model for ticket discussions"""
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    
    # Foreign keys
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Comment {self.id} on Ticket {self.ticket_id}>'
