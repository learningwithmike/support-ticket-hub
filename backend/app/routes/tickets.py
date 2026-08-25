from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Ticket, User, TicketStatus, TicketPriority
from app.routes import tickets_bp
from datetime import datetime

@tickets_bp.route('', methods=['GET'])
@jwt_required()
def get_tickets():
    """Get all tickets with optional filtering"""
    status = request.args.get('status')
    priority = request.args.get('priority')
    assigned_to = request.args.get('assigned_to')
    
    query = Ticket.query
    
    if status:
        try:
            query = query.filter_by(status=TicketStatus[status.upper()])
        except KeyError:
            return jsonify({'message': 'Invalid status'}), 400
    
    if priority:
        try:
            query = query.filter_by(priority=TicketPriority[priority.upper()])
        except KeyError:
            return jsonify({'message': 'Invalid priority'}), 400
    
    if assigned_to:
        query = query.filter_by(assigned_to=assigned_to)
    
    tickets = query.all()
    
    return jsonify({
        'tickets': [{
            'id': ticket.id,
            'title': ticket.title,
            'description': ticket.description,
            'status': ticket.status.value,
            'priority': ticket.priority.value,
            'created_by': ticket.creator.username,
            'assigned_to': ticket.assignee.username if ticket.assignee else None,
            'created_at': ticket.created_at.isoformat(),
            'updated_at': ticket.updated_at.isoformat()
        } for ticket in tickets]
    }), 200

@tickets_bp.route('', methods=['POST'])
@jwt_required()
def create_ticket():
    """Create a new ticket"""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data or not data.get('title') or not data.get('description'):
        return jsonify({'message': 'Missing required fields'}), 400
    
    try:
        priority = TicketPriority[data.get('priority', 'MEDIUM').upper()]
    except KeyError:
        return jsonify({'message': 'Invalid priority'}), 400
    
    ticket = Ticket(
        title=data['title'],
        description=data['description'],
        priority=priority,
        created_by=current_user_id
    )
    
    db.session.add(ticket)
    db.session.commit()
    
    return jsonify({
        'message': 'Ticket created successfully',
        'ticket': {
            'id': ticket.id,
            'title': ticket.title,
            'description': ticket.description,
            'status': ticket.status.value,
            'priority': ticket.priority.value,
            'created_at': ticket.created_at.isoformat()
        }
    }), 201

@tickets_bp.route('/<int:ticket_id>', methods=['GET'])
@jwt_required()
def get_ticket(ticket_id):
    """Get a specific ticket"""
    ticket = Ticket.query.get_or_404(ticket_id)
    
    return jsonify({
        'ticket': {
            'id': ticket.id,
            'title': ticket.title,
            'description': ticket.description,
            'status': ticket.status.value,
            'priority': ticket.priority.value,
            'created_by': ticket.creator.username,
            'assigned_to': ticket.assignee.username if ticket.assignee else None,
            'created_at': ticket.created_at.isoformat(),
            'updated_at': ticket.updated_at.isoformat(),
            'closed_at': ticket.closed_at.isoformat() if ticket.closed_at else None
        }
    }), 200

@tickets_bp.route('/<int:ticket_id>', methods=['PUT'])
@jwt_required()
def update_ticket(ticket_id):
    """Update a ticket"""
    ticket = Ticket.query.get_or_404(ticket_id)
    data = request.get_json()
    
    if 'title' in data:
        ticket.title = data['title']
    if 'description' in data:
        ticket.description = data['description']
    if 'status' in data:
        try:
            ticket.status = TicketStatus[data['status'].upper()]
            if ticket.status == TicketStatus.CLOSED or ticket.status == TicketStatus.RESOLVED:
                ticket.closed_at = datetime.utcnow()
        except KeyError:
            return jsonify({'message': 'Invalid status'}), 400
    if 'priority' in data:
        try:
            ticket.priority = TicketPriority[data['priority'].upper()]
        except KeyError:
            return jsonify({'message': 'Invalid priority'}), 400
    if 'assigned_to' in data:
        if data['assigned_to']:
            user = User.query.get(data['assigned_to'])
            if not user:
                return jsonify({'message': 'User not found'}), 404
            ticket.assigned_to = data['assigned_to']
        else:
            ticket.assigned_to = None
    
    ticket.updated_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({
        'message': 'Ticket updated successfully',
        'ticket': {
            'id': ticket.id,
            'title': ticket.title,
            'description': ticket.description,
            'status': ticket.status.value,
            'priority': ticket.priority.value,
            'assigned_to': ticket.assignee.username if ticket.assignee else None,
            'updated_at': ticket.updated_at.isoformat()
        }
    }), 200

@tickets_bp.route('/<int:ticket_id>', methods=['DELETE'])
@jwt_required()
def delete_ticket(ticket_id):
    """Delete a ticket"""
    ticket = Ticket.query.get_or_404(ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    
    return jsonify({'message': 'Ticket deleted successfully'}), 200
