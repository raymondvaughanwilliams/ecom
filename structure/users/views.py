# users/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint,session
from flask_login import login_user, current_user, logout_user, login_required
from structure import db
from structure.models import User, WebFeature
from structure.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from structure.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)

# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        print("df")
        user = User(email=form.email.data,
                    name=form.name.data,
                    username=form.username.data,
                    password=form.password.data,
                    last_name=form.last_name.data,role=form.role.data,
                    number=form.number.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))

    return render_template('web/register.html',form=form)




@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()
        session['email'] = form.email.data
        session['id'] = user.id
        
        userr = User.query.filter_by(email=form.email.data).first()
        session['name'] = userr.name
        session['role'] = userr.role
        print("session")
        print(session['name'])


        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None and user.role == 'admin':
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')



            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('userportal.userdash')

            return redirect(next)

        if user.check_password(form.password.data) and user is not None and user.role == 'user':
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')



            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('userportal.userdash')

            return redirect(next)


        if user.check_password(form.password.data) and user is not None and user.role == 'therapist':
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')



            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('therapistportal.therapistdash')

            return redirect(next)
    return render_template('web/login.html', form=form)

# logout
@users.route("/logout")
def logout():
    logout_user()
    session.pop('email',None)
    session.pop('name',None)
    session.pop('role',None)

    return redirect(url_for("core.index"))


# account (update UserForm)
@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    userinfo = User.query.filter_by(email=session["email"]).first_or_404()

    form = UpdateUserForm()

    if request.method == 'POST':

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.name = form.name.data
        current_user.number = form.number.data
        current_user.location = form.location.data
        current_user.pref_help = form.pref_help.data
        current_user.pref_therapistgender = form.pref_gender.data
        current_user.pref_medium = form.pref_medium.data
        

        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('userportal.uprofile'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('userportal/profile.html', profile_image=profile_image, form=form,userinfo=userinfo)

@users.route("/<username>")
def user_posts(username):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    web_features = WebFeature.query.filter_by(author=user).order_by(WebFeature.date.desc()).paginate(page=page,per_page=5)
    return render_template('user_web_features.html',web_features=web_features,user=user)




















# user's list of Blog posts
