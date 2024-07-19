from flask_restful import Resource, Api
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from flask import request
from models import *
from genai_utils import StoryGenerate, GenerateImage, SketchGenerator
from PIL import Image

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {'message': f'Hello, {current_user}! This is a protected resource.'}, 200


class StoryGenerator(Resource):
    def post(self):
        if 'image_file' in request.files:
            image_file = request.files['image_file']
            img = Image.open(image_file.stream)
            gen = StoryGenerate(img)
            data = gen.generate()
            return {'story': f'{data}'}, 200
        else:
            return {'error': 'No image file provided'}, 400
    
class Fill(Resource):
    def post(self):
        data = request.get_json()
        prompt = data.get('prompt')
        gen = GenerateImage(prompt)
        img = gen.generate()

class Sketch(Resource):
    pass


class ProjectQueryResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user_projects = Project.query.filter_by(user_id=current_user.id).all()
        return user_projects

class ProjectCreationResource(Resource):
    @jwt_required()
    def post(self):
        # Get the current user's identity
        current_user_id = get_jwt_identity()
        
        # Get data from the request
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')
        image_file = data.get('image_file', None)  # Optional field

        # Validate required fields
        if not title or not description:
            return {'message': 'Title and description are required'}, 400

        # Create a new Project instance
        new_project = Project(
            title=title,
            description=description,
            user_id=current_user_id,
            image_file=image_file
        )

        # Add and commit the new project to the database
        try:
            db.session.add(new_project)
            db.session.commit()
            return {
                'message': 'Project created successfully',
                'project': {
                    'id': new_project.id,
                    'title': new_project.title,
                    'description': new_project.description,
                    'user_id': new_project.user_id
                }
            }, 201
        except Exception as e:
            db.session.rollback()
            return {'message': f'An error occurred: {str(e)}'}, 500