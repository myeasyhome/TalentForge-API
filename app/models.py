from app import db
from sqlalchemy.sql import func
class JobSeeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    token = db.Column(db.String(512))
    education = db.Column(db.Text)
    skills = db.Column(db.String(255))
    address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    pincode = db.Column(db.String(10))
    applications = db.relationship('Application', backref='job_seeker', lazy=True)

class Recruiter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    token = db.Column(db.String(255))
    company_name = db.Column(db.String(255))
    company_address = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    pincode = db.Column(db.String(10))
    job_postings = db.relationship('JobPosting', backref='recruiter', lazy=True)

class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(255))
    description = db.Column(db.Text)
    salary = db.Column(db.String(50))
    skills = db.Column(db.String(255))
    qualification = db.Column(db.Text)
    location = db.Column(db.String(255))
    role_category = db.Column(db.String(255))
    department = db.Column(db.String(255))
    experience = db.Column(db.String(50))
    required_skills = db.Column(db.String(255))
    employment_type = db.Column(db.String(50))
    company_name = db.Column(db.String(255))
    company_info = db.Column(db.Text)
    openings = db.Column(db.Integer)
    timestamp = db.Column(db.TIMESTAMP, server_default=func.now())
    recruiter_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'))
    applications = db.relationship('Application', backref='job_posting', lazy=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50))
    timestamp = db.Column(db.TIMESTAMP, server_default=func.now())
    job_seeker_id = db.Column(db.Integer, db.ForeignKey('jobseeker.id'))
    job_posting_id = db.Column(db.Integer, db.ForeignKey('jobposting.id'))

class SkillSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skills = db.Column(db.String(255))
