from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import check_password_hash
from config import db
from models import User

class UserSignUp(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        
        if not email or not username or not password:
            return {'message': 'Missing email, username, or password'}, 400
        
        if User.query.filter_by(email=email).first():
            return {'message': 'Email already exists'}, 400
        
        new_user = User(email, username, password)
        db.session.add(new_user)
        db.session.commit()
        
        return {'message': 'User created successfully'}, 201

# Resource for user login
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return {'message': 'Missing email or password'}, 400
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            return {'message': 'Invalid credentials'}, 401
        
        access_token = create_access_token(identity=email)
        return {'access_token': access_token}, 200