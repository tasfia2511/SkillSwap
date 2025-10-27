from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CanTeach, Skill, CanLearn

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        CONTEXT = {
            'user': request.user,
            'page':'home'
        }
        return render(request, 'home.html', CONTEXT)

    CONTEXT = {
        'page':'home'
    }
    return render(request, 'home.html', CONTEXT)


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=email)
        user.save()
        messages.success(request, 'User created successfully')
        return redirect('login')
    else:
        CONTEXT = {
            'page':'signup'
        }
        return render(request, 'signup.html', CONTEXT)



# login with email and password
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        CONTEXT = {
            'page':'login'
        }
        return render(request, 'login.html', CONTEXT)


def signout(request):
    logout(request)
    return redirect('home')


def about_us(request):
    CONTEXT ={
        'page':'about_us'
    }
    return render(request, 'about_us.html', CONTEXT)

def services(request):
    CONTEXT ={
        'page':'services'
    }
    return render(request, 'services.html', CONTEXT)

def how_it_works(request):
    CONTEXT ={
        'page':'how_it_works'
    }
    return render(request, 'how_it_works.html', CONTEXT)

def faq(request):
    CONTEXT = {
        'page':'faq'
    }
    return render(request, 'faq.html', CONTEXT)

@login_required
def skill(request):
    if request.method == 'POST':
        skill_name = request.POST['skill_name']
        skill_description = request.POST['skill_description']

        skill = Skill.objects.create(name=skill_name, description=skill_description)
        skill.save()
        messages.success(request, 'Skill Created successfully')
        return redirect('teach')
    else:
        CONTEXT = {
            'page':'skill'
        }
        return render(request, 'skill.html', CONTEXT)


@login_required
def teach(request):
    if request.method == 'POST':
        skill_id = request.POST['skill']
        available_time = request.POST['available_time']
        description = request.POST['description']

        skill = Skill.objects.get(id=skill_id)

        try:
            CanTeach.objects.create(skill=skill, available_time=available_time, description=description, teacher=request.user)
            messages.success(request, 'Teaching skill added successfully')
            return redirect('teach')
        except Exception as e:
            messages.error(request, e)
            return redirect('teach')
    else:

        # Get skills that the user is already teaching
        user_teaching_skills = CanTeach.objects.filter(teacher=request.user).values_list('skill_id', flat=True)
        
        # Exclude skills that the user is already teaching
        available_skills = Skill.objects.exclude(id__in=user_teaching_skills)  

        CONTEXT = {
            'user': request.user,
            'can_teach': available_skills,
            'page':'teach'
        }
        return render(request, 'teach.html', CONTEXT)


@login_required
def learn(request):
    if request.method == 'POST':
        skill_id = request.POST['skill']
        skill = Skill.objects.get(id=skill_id)

        try:
            CanLearn.objects.create(skill=skill, learner=request.user)
            messages.success(request, 'Skill added to learning list for ' + request.user.username)
            return redirect('learn')
        except Exception as e:
            messages.error(request, e)
            return redirect('learn')
    else: 
        # Get skills that the user is already learning
        user_learning_skills = CanLearn.objects.filter(learner=request.user).values_list('skill_id', flat=True)

        print('user learning skills: ', user_learning_skills)
        
        # Exclude skills that the user is already learning
        available_skills = Skill.objects.exclude(id__in=user_learning_skills)

        print('available skills: ', available_skills)
        

        CONTEXT = {
            'user': request.user,
            'can_learn': available_skills,
            'page':'learn'
        }
        return render(request, 'learn.html', CONTEXT)



@login_required
def dashboard(request):
    # Get skills that the user is teaching
    teaching_skills = CanTeach.objects.filter(teacher=request.user).select_related('skill')
    
    # Get skills that the user is learning
    # user_learning_skills = CanLearn.objects.filter(learner=request.user).values_list('skill_id', flat=True)
    user_learning_skills = CanLearn.objects.filter(learner=request.user).select_related('skill')


    # print('user learning skills: ', user_learning_skills)

    # Get count of learners for each skill the user is teaching
    skill_learners_count = []
    for teaching_skill in teaching_skills:
        learners_count = CanLearn.objects.filter(skill=teaching_skill.skill).count()
        skill_learners_count.append({
            'skill': teaching_skill.skill.name,
            'learners_count': learners_count
        })

    CONTEXT = {
        'user': request.user,
        'user_teaching_skills': teaching_skills,
        'user_learning_skills': user_learning_skills,
        'skill_learners_count': skill_learners_count,
        'page':'dashboard'
    }
    return render(request, 'dashboard.html', CONTEXT)


@login_required
def profile(request, pk):
    user = User.objects.get(id=pk)

    # Get skills that the user is teaching
    teaching_skills = CanTeach.objects.filter(teacher=user).select_related('skill')

    # Get skills that the user is learning
    user_learning_skills = CanLearn.objects.filter(learner=user).select_related('skill')


    
    CONTEXT = {
        'user': user,
        'user_teaching_skills': teaching_skills,
        'user_learning_skills': user_learning_skills,
        'page':'profile'
    }
    return render(request, 'profile.html', CONTEXT)



@login_required
def browse_skills(request):
    # Get all users who are either teaching or learning skills
    teaching_users = User.objects.filter(
        id__in=CanTeach.objects.values_list('teacher_id', flat=True)
    )
    learning_users = User.objects.filter(
        id__in=CanLearn.objects.values_list('learner_id', flat=True)
    )
    users = (teaching_users | learning_users).distinct()
    
    skills_data = []
    
    for user in users:
        # Get teaching skills for the user
        # teaching_skills = list(CanTeach.objects
        #                      .filter(teacher=user)
        #                      .select_related('skill')
        #                      .values_list('skill__id', 'skill__name', flat=True))

        teaching_skills = list(CanTeach.objects
            .filter(teacher=user)
            .select_related('skill')
            .values('skill__id', 'skill__name', 'skill__description', 'available_time', 'description')
        )
                
        # Get learning skills for the user
        learning_skills = list(CanLearn.objects
                             .filter(learner=user)
                             .select_related('skill')
                             .values_list('skill__name', flat=True))
        
        # Only include users who have either teaching or learning skills
        if teaching_skills or learning_skills:
            skills_data.append({
                'user': f"{user.first_name} {user.last_name}",
                'user_id': user.id,  # Add user ID for potential profile links
                'teaching_skills': teaching_skills,
                'learning_skills': learning_skills
            })
    
    CONTEXT = {
        'skills': skills_data,
        'page':'browse_skills'
    }
    return render(request, 'browse_skills.html', CONTEXT)
